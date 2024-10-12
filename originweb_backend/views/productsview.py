import json
from django.shortcuts import render


from ..models.productsmodel import Productsmodel
from django.http import JsonResponse
from rest_framework.views import APIView 
from rest_framework.parsers import JSONParser
from drf_spectacular.utils import extend_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, action, permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from ..serializers import ProductSerializer
from django.core.exceptions import FieldError
from django.utils import timezone


# @extend_schema(request={
#     'query_params': {
#         'action': openapi.Parameter('action', openapi.IN_QUERY, description="option to the database", type=openapi.TYPE_STRING),
#     }
# })
# @extend_schema(request={
#     'body': openapi.Schema(
#         type=openapi.TYPE_OBJECT,
#         properties={
#             'username': openapi.Schema(type=openapi.TYPE_STRING),
#             'password': openapi.Schema(type=openapi.TYPE_STRING),
#         }
#     )
# })
@extend_schema(responses={200: 'OK'})
class ProductsView(APIView):   
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'action',
                openapi.IN_QUERY,
                description="action for db",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'id',
                openapi.IN_QUERY,
                description="item id",
                type=openapi.TYPE_STRING
            )
        ],      
    )
    # @swagger_auto_schema(request_body=Productsmodel)
    @permission_classes([AllowAny])
    @action(detail=False, methods=['get'])
    def get(self, request, *args, **kwargs):
        action = request.GET.get('action', None)  
        productid = request.GET.get('id', None)                
        # 使用data字典中的数据       
        if action == 'selectbyid':     
            # return JsonResponse({'result': 'OK'})    
            items = self.selectById(productid)
            try:
                error = items["error"]
                return JsonResponse(items, status=400,safe=False)
            except Exception as e:
                error = ""
                return JsonResponse(items, safe=False)  

        elif action == 'selectall':
            items = self.selectAll()
            return JsonResponse(items, safe=False)

        else:
            return JsonResponse({'ok': 'no action specific'}, status=200, safe=False)
            # return self.get_detail(request, *args, **kwargs)
        
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'action',
                openapi.IN_QUERY,
                description="action for db",
                type=openapi.TYPE_STRING
            )
        ],
        request_body=ProductSerializer
        # request_body=openapi.Schema(
        #     type=openapi.TYPE_OBJECT,
        #     additionalProperties=True
        # ),
    )
    @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):
        action = request.GET.get('action', None) 
        if action == 'selectbyfilters':     
            # return JsonResponse({'result': 'OK'})   
            items = self.selectByFilters(request) 
            try:
                error = items["error"]
                return JsonResponse(items, status=400,safe=False)
            except Exception as e:
                error = ""
                return JsonResponse(items, safe=False) 
                           
        elif action == 'insertitem':
            items = self.insertProduct(request)  
            return JsonResponse(items, status=201, safe=False)
        else:
            return JsonResponse({'ok': 'no action specific'}, status=200, safe=False)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'action',
                openapi.IN_QUERY,
                description="action for db",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'productcode',
                openapi.IN_QUERY,
                description="product code",
                type=openapi.TYPE_STRING
            )
        ],
        request_body=ProductSerializer
        # request_body=openapi.Schema(
        #     type=openapi.TYPE_OBJECT,
        #     additionalProperties=True
        # ),
    )
    @action(detail=False, methods=['put'])
    def put(self, request, *args, **kwargs):
        action = request.GET.get('action', None) 
        productcode = request.GET.get('productcode', None) 
        if action == 'updateitem':     
            # return JsonResponse({'result': 'OK'})            
            items = self.updateItem(productcode, request) 
            return JsonResponse(items, status=201, safe=False)    
        elif action == 'updateorinsertitem':     
            # return JsonResponse({'result': 'OK'})            
            items = self.updateorinsertItem(productcode, request) 
            return JsonResponse(items, status=201, safe=False)   
        else:
            return JsonResponse({'ok': 'no action specific'}, status=200, safe=False)
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'action',
                openapi.IN_QUERY,
                description="action for db",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'productcode',
                openapi.IN_QUERY,
                description="product code",
                type=openapi.TYPE_STRING
            )
        ],      
    )
    @action(detail=False, methods=['delete'])
    def delete(self, request, *args, **kwargs):
        action = request.GET.get('action', None) 
        productcode = request.GET.get('productcode', None) 
        if action == 'deletebylogic':     
            # return JsonResponse({'result': 'OK'})            
            items = self.deleteItembyLogic(productcode) 
            return JsonResponse(items, status=201, safe=False)    
        elif action == 'deletefromdb':     
            # return JsonResponse({'result': 'OK'})            
            items = self.deleteItemfromDB(productcode) 
            return JsonResponse(items, status=201, safe=False)   
        else:
            return JsonResponse({'ok': 'no action specific'}, status=200, safe=False)

    #get methods
    def selectAll(self):        
        items = list(Productsmodel.objects.filter(isdel=0).values())
        return items   
    
    def selectById(self, productid:int):       
        try:
            items = Productsmodel.objects.get(id=productid)
            serializer = ProductSerializer(items) 
            return serializer.data 
            
        except Productsmodel.DoesNotExist as e:
            return {"error":str(e)}
    def selectByProductCode(self, code):       
        try:
            items = Productsmodel.objects.get(productcode=code)    
            return items 
            
        except Productsmodel.DoesNotExist:
            return ""
    
    #post methods
    def selectByFilters(self, request):       
        # 从请求体中解析JSON数据
        data = request.data
        # 初始化查询集,isdel不等于0
        products = Productsmodel.objects.filter(isdel=0)

        # 动态过滤查询集
        for key, value in data.items():
            # 这里同样需要对key进行验证，确保它是模型的一个字段
            if hasattr(Productsmodel, key):
                try:
                    products = products.filter(**{f"{key}": value})
                except FieldError:
                # 处理无效字段
                    pass
            else:
                return {"error":"no column found in table"}
        # 序列化查询结果
        serializer = ProductSerializer(products, many=True)
        return serializer.data
    
    def insertProduct(self, request):  
        data = request.data
        product = Productsmodel(**data)
        product.save()
        return data
    
    #put methods
    def updateItem(self, code, request):  
        item = self.selectByProductCode(code)         
        if(item != ""):
            # serializer = ProductSerializer(item, data=request.data)
            for key,value in request.data.items():
                setattr(item, key, value)
            item.save()
            return {"result":"update"}
            # if serializer.is_valid() :
            #     serializer.save()
            #     return "update"
            # else:
            #     return "not update"
        else:
            return {"result":"item not found"}
       
    def updateorinsertItem(self, code, request):  
        created = Productsmodel.objects.update_or_create(defaults=request.data, productcode=code)
        if created:
            return {"result":"create"}
        else:
            return {"result":"update"}

    #delete methods
    def deleteItembyLogic(self, code):  
        item = self.selectByProductCode(code)         
        if(item != ""):
            setattr(item, "isdel", 1)
            setattr(item, "deltime", timezone.now())
            print(timezone.now())
            item.save()
            return {"result":"update"}
            # if serializer.is_valid() :
            #     serializer.save()
            #     return "update"
            # else:
            #     return "not update"
        else:
            return {"result":"item not found"}
    def deleteItemfromDB(self, code):  
        item = self.selectByProductCode(code)         
        if(item != ""):
            item.delete()
            return {"result":"delete"}
            # if serializer.is_valid() :
            #     serializer.save()
            #     return "update"
            # else:
            #     return "not update"
        else:
            return {"result":"item not found"}

from rest_framework import serializers
from .models.productsmodel import Productsmodel  # 确保从您的 models.py 文件中导入 Item 模型

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productsmodel  # 指定关联的模型
        fields = '__all__'
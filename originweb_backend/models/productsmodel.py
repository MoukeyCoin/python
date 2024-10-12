from django.db import models

# Create your models here.


class Productsmodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    productcode = models.CharField(db_column='productCode', unique=True, max_length=255)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=255)  # Field name made lowercase.
    category = models.CharField(max_length=50, blank=True, null=True, db_comment='商品分类')
    title = models.CharField(max_length=300, blank=True, null=True)
    cover = models.CharField(max_length=1000, blank=True, null=True)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    link = models.CharField(max_length=2000, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime',auto_now_add=True)  # Field name made lowercase. auto_now_add新增时自动填写当前时间
    modifytime = models.DateTimeField(db_column='modifyTime',auto_now=True)  # Field name made lowercase.auto_now 更新时填写当前时间
    isdel = models.IntegerField(db_column='isDel')  # Field name made lowercase.
    deltime = models.DateTimeField(db_column='delTime', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='createUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifyuser = models.CharField(db_column='modifyUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deluser = models.CharField(db_column='delUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'originweb_backend_productsmodel'

# Generated by Django 5.1 on 2025-01-10 07:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("originweb_backend", "0005_alter_productsmodel_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="productsmodel",
            name="category",
            field=models.CharField(
                blank=True, db_comment="商品分类", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="productsmodel",
            name="createtime",
            field=models.DateTimeField(
                auto_now_add=True,
                db_column="createTime",
                default=django.utils.timezone.now,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productsmodel",
            name="createuser",
            field=models.CharField(
                blank=True, db_column="createUser", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="productsmodel",
            name="deltime",
            field=models.DateTimeField(blank=True, db_column="delTime", null=True),
        ),
        migrations.AddField(
            model_name="productsmodel",
            name="deluser",
            field=models.CharField(
                blank=True, db_column="delUser", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="productsmodel",
            name="isdel",
            field=models.IntegerField(db_column="isDel", default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productsmodel",
            name="modifytime",
            field=models.DateTimeField(auto_now=True, db_column="modifyTime"),
        ),
        migrations.AddField(
            model_name="productsmodel",
            name="modifyuser",
            field=models.CharField(
                blank=True, db_column="modifyUser", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="productsmodel",
            name="productcode",
            field=models.CharField(
                db_column="productCode", default=200, max_length=255, unique=True
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productsmodel",
            name="productname",
            field=models.CharField(
                db_column="productName", default="new", max_length=255
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="productsmodel",
            name="cover",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="productsmodel",
            name="description",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="productsmodel",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="productsmodel",
            name="link",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="productsmodel",
            name="subtitle",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="productsmodel",
            name="title",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

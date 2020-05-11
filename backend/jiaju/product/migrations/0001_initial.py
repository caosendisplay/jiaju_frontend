# Generated by Django 3.0.3 on 2020-05-09 22:28

from django.db import migrations, models
import django.db.models.deletion
import jiaju.product.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0003_article_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '产品类型',
                'verbose_name_plural': '产品类型',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=80, verbose_name='名称')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.Category')),
            ],
            options={
                'verbose_name': '现货产品',
                'verbose_name_plural': '现货产品',
            },
        ),
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('image', models.ImageField(upload_to=jiaju.product.models.upload_and_rename_product_detail, verbose_name='图片')),
                ('description', models.CharField(blank=True, max_length=80, null=True, verbose_name='描述')),
                ('featured', models.BooleanField(default=False, verbose_name='是否首页展示')),
                ('cover', models.BooleanField(default=False, verbose_name='是否作为封面')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='product.Product', verbose_name='现货产品')),
            ],
            options={
                'verbose_name': '产品图片',
                'verbose_name_plural': '产品图片',
            },
        ),
        migrations.CreateModel(
            name='ProductDetailedDescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('article', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Article')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': '产品详情描述',
                'verbose_name_plural': '产品详情描述',
            },
        ),
    ]

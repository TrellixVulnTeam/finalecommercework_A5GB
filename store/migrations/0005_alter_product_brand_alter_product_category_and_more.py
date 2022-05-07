# Generated by Django 4.0.4 on 2022-05-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_brand_product_category_product_imageurl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=200, verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=2000, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imageurl',
            field=models.CharField(max_length=500, verbose_name='imageurl'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=200, verbose_name='anufacturer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(max_length=200, verbose_name='weight'),
        ),
    ]

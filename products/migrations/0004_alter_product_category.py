# Generated by Django 5.0.4 on 2024-05-06 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men Shirts', 'Men Shirts'), ('Men T-Shirts', 'Men T-Shirts'), ('Ladies Dresses', 'Ladies Dresses'), ('Children dresses', 'Children dresses'), ('MObiles', 'MObiles'), ('Watches', 'Watches')], default='Others', max_length=100),
        ),
    ]

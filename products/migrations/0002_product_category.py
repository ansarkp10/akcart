# Generated by Django 5.0.4 on 2024-05-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men Shirts', 'Men Shirts'), ('Ladies Dresses', 'Ladies Dresses'), ('Others', 'Others')], default='Others', max_length=100),
        ),
    ]

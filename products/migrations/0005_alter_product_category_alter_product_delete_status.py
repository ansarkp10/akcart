# Generated by Django 5.0.4 on 2024-05-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men Shirts', 'Men Shirts'), ('Men T-Shirts', 'Men T-Shirts'), ('Ladies Dresses', 'Ladies Dresses'), ('Children dresses', 'Children dresses'), ('Mobiles', 'Mobiles'), ('Watches', 'Watches')], default='Others', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='delete_status',
            field=models.IntegerField(choices=[(1, 'Live'), (0, 'Delete')], default=1),
        ),
    ]
# Generated by Django 4.2.2 on 2023-09-01 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_alter_product_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-05 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_product_category_of_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_of_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Products.product_category'),
        ),
    ]

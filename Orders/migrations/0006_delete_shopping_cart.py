# Generated by Django 4.2.5 on 2023-09-06 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0005_alter_order_status_alter_shopping_cart_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shopping_Cart',
        ),
    ]

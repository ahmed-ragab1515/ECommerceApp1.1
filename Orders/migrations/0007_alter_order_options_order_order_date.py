# Generated by Django 4.2.5 on 2023-09-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_delete_shopping_cart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['order_date']},
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

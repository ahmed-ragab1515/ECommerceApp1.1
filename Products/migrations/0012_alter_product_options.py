# Generated by Django 4.2.5 on 2023-09-06 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_delete_review_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
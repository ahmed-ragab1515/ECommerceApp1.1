# Generated by Django 4.2.5 on 2023-09-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_review_product_review_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review_product',
            options={'ordering': ['review_date']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default=1, upload_to='photos/%y/%m/%d'),
            preserve_default=False,
        ),
    ]

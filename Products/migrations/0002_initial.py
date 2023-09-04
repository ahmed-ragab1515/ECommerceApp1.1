# Generated by Django 4.2.2 on 2023-09-01 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_product',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_of_product',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to='Products.product_category'),
        ),
    ]
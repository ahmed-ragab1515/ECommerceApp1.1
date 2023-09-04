# Generated by Django 4.2.2 on 2023-09-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('admin', 'Admin')], default='customer', max_length=20),
        ),
    ]
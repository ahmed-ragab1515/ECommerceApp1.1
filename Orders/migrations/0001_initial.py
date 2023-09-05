# Generated by Django 4.2.5 on 2023-09-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending', max_length=10)),
                ('products', models.ManyToManyField(default=True, to='Products.product')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Status_History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('new_status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], max_length=10)),
                ('status_time', models.DateTimeField()),
                ('order_id', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Orders.order')),
            ],
        ),
    ]

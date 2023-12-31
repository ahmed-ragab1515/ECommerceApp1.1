# Generated by Django 4.2.2 on 2023-09-01 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending', max_length=10),
        ),
        migrations.CreateModel(
            name='OrderStatusHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('new_status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], max_length=10)),
                ('status_time', models.DateTimeField(auto_now=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.order')),
            ],
        ),
    ]

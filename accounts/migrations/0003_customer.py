# Generated by Django 4.2.2 on 2023-09-01 14:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2021-07-17 08:51

import apps.order.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210514_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='ord',
            name='wid',
            field=models.CharField(default=apps.order.models.increment_wait_number, max_length=20, verbose_name='侯位編號'),
        ),
    ]
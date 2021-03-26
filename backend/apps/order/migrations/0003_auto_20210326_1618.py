# Generated by Django 3.1.7 on 2021-03-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210326_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordinfo',
            name='ordice',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='冰塊'),
        ),
        migrations.AlterField(
            model_name='ordinfo',
            name='ordsua',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='甜度'),
        ),
        migrations.AlterField(
            model_name='ordinfo',
            name='ordtip',
            field=models.TextField(blank=True, default='', verbose_name='備註'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-08-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_ord_ordtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='ord',
            name='changetime',
            field=models.DateTimeField(auto_now=True, verbose_name='變更時間'),
        ),
        migrations.AlterField(
            model_name='ord',
            name='ordtime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='訂單時間'),
        ),
    ]

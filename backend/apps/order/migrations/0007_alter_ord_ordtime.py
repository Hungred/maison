# Generated by Django 3.2.4 on 2021-08-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20210801_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ord',
            name='ordtime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='日期時間'),
        ),
    ]

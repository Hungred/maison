# Generated by Django 3.1.7 on 2021-05-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210326_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ord',
            name='ordcheck',
            field=models.IntegerField(default=0, verbose_name='處理狀態'),
        ),
        migrations.AlterField(
            model_name='ord',
            name='ordtime',
            field=models.DateTimeField(auto_now=True, verbose_name='日期時間'),
        ),
    ]

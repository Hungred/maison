# Generated by Django 3.2.4 on 2021-07-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210507_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_data',
            name='empid',
            field=models.CharField(default='員工不存在', max_length=5, unique=True, verbose_name='員工編號'),
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20210413_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksche',
            name='offhour',
            field=models.CharField(max_length=2, verbose_name='退勤時'),
        ),
        migrations.AlterField(
            model_name='worksche',
            name='offmin',
            field=models.CharField(max_length=2, verbose_name='退勤分'),
        ),
        migrations.AlterField(
            model_name='worksche',
            name='workmin',
            field=models.CharField(max_length=2, verbose_name='出勤分'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20210323_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksche',
            name='workdate',
            field=models.DateField(auto_now_add=True, verbose_name='出勤日期'),
        ),
    ]
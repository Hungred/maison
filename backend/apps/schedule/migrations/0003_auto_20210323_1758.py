# Generated by Django 3.1.7 on 2021-03-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20210323_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('B', '老闆'), ('M', '管理人員'), ('E', '一般員工')], max_length=1, verbose_name='職位'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-03 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20210413_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksche',
            name='empid',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Worksche',
        ),
    ]
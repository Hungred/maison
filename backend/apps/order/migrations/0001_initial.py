# Generated by Django 3.1.7 on 2021-03-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('fid', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='餐點編號')),
                ('foodtype', models.CharField(choices=[('A', '主餐'), ('B', '副餐'), ('C', '甜點'), ('D', '飲料')], max_length=1, verbose_name='餐點類型')),
                ('foodname', models.CharField(max_length=10, verbose_name='餐點名稱')),
                ('foodprice', models.IntegerField(verbose_name='餐點價錢')),
                ('foodtag', models.TextField(verbose_name='餐點特徵')),
            ],
        ),
        migrations.CreateModel(
            name='Ord',
            fields=[
                ('serno', models.AutoField(primary_key=True, serialize=False)),
                ('ordtime', models.DateTimeField(verbose_name='日期時間')),
                ('tabnum', models.CharField(max_length=3, verbose_name='桌號')),
                ('ordcheck', models.IntegerField(verbose_name='處理狀態')),
            ],
        ),
        migrations.CreateModel(
            name='ordinfo',
            fields=[
                ('serno', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]

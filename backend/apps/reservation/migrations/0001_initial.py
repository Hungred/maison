# Generated by Django 3.1.7 on 2021-03-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('serno', models.AutoField(primary_key=True, serialize=False, verbose_name='流水號')),
                ('bookname', models.CharField(max_length=2, verbose_name='姓')),
                ('booktel', models.CharField(max_length=10, verbose_name='電話號碼')),
                ('bookadt', models.IntegerField(default=0, verbose_name='大人數量')),
                ('bookchd', models.IntegerField(default=0, verbose_name='小孩數量')),
                ('booktime', models.DateTimeField(verbose_name='時間')),
                ('remark', models.TextField(verbose_name='備注')),
                ('systime', models.DateTimeField(auto_now_add=True, verbose_name='系統時間')),
            ],
        ),
        migrations.CreateModel(
            name='Wt',
            fields=[
                ('serno', models.AutoField(primary_key=True, serialize=False, verbose_name='流水號')),
                ('wid', models.IntegerField(verbose_name='侯位編號')),
                ('wtname', models.CharField(max_length=2, verbose_name='姓')),
                ('wtadt', models.IntegerField(default=0, verbose_name='大人數量')),
                ('wtchd', models.IntegerField(default=0, verbose_name='小孩數量')),
                ('wtcheck', models.IntegerField(choices=[('0', '等待中'), ('1', '已帶位')], verbose_name='處理狀態')),
            ],
        ),
    ]

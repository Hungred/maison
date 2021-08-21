# Generated by Django 3.2.6 on 2021-08-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=50, verbose_name='活動名稱')),
                ('on_going', models.BooleanField(default=True, verbose_name='是否顯示在官網')),
                ('hyperlink', models.TextField(verbose_name='FB貼文連結')),
                ('coverimage', models.ImageField(blank=True, default='eventimage/default.png', upload_to='eventimage', verbose_name='活動封面')),
            ],
        ),
    ]
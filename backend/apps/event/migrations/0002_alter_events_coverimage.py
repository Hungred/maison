# Generated by Django 3.2.6 on 2021-08-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='coverimage',
            field=models.ImageField(default='eventimage/default.png', upload_to='eventimage', verbose_name='活動封面'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_events_coverimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='coverimage',
            field=models.ImageField(blank=True, default='eventimage/default.png', null=True, upload_to='eventimage', verbose_name='活動封面'),
        ),
    ]

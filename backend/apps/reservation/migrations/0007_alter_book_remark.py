# Generated by Django 3.2.4 on 2021-07-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_alter_book_booktime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='remark',
            field=models.TextField(null=True, verbose_name='備註'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-08 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_alter_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, default='foodimage/default.png', upload_to='foodimage', verbose_name='餐點圖片'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-10-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_employee_data_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_data',
            name='status',
            field=models.CharField(choices=[('在職', '在職'), ('離職', '離職'), ('暫休', '暫休'), ('其他', '其他')], default='在職', max_length=10, verbose_name='員工狀態'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-10-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnsApp', '0004_auto_20211010_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driveraccount',
            name='cityCode',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='passengeraccount',
            name='cityCode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

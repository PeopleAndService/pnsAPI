# Generated by Django 3.2.6 on 2021-10-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnsApp', '0009_alter_queuedata_createat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuedata',
            name='boardingCheck',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.6 on 2021-10-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnsApp', '0007_routeperbus_nodeord'),
    ]

    operations = [
        migrations.AddField(
            model_name='queuedata',
            name='createAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

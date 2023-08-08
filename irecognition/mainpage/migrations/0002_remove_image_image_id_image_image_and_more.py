# Generated by Django 4.1 on 2023-08-08 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_id',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='hours_active',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_class',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
# Generated by Django 3.1.3 on 2021-09-20 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210920_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos/%y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['mp4', 'avi', 'flv', '3gp', 'vob', 'wmv', 'm4p', 'mpg', 'mp2', 'mpeg', 'webm', 'mkv'])]),
        ),
    ]

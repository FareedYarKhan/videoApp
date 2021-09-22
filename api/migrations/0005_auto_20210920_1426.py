# Generated by Django 3.1.3 on 2021-09-20 09:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210920_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos/%y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['mp4', 'pdf'])]),
        ),
    ]
# Generated by Django 3.1.3 on 2021-09-21 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210921_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processedfiles',
            old_name='file',
            new_name='fileJson',
        ),
    ]
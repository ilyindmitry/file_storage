# Generated by Django 2.0.3 on 2019-02-09 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_remove_userfile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='size',
        ),
    ]

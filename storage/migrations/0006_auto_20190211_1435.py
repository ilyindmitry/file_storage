# Generated by Django 2.0.3 on 2019-02-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_remove_userfile_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]

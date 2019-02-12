# Generated by Django 2.0.3 on 2019-02-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('upload_datetime', models.DateTimeField()),
                ('size', models.IntegerField()),
                ('status', models.CharField(choices=[('r', 'ready'), ('p', 'pending')], max_length=1)),
            ],
            options={
                'ordering': ['upload_datetime'],
            },
        ),
    ]
# Generated by Django 3.2 on 2021-05-07 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210507_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dept',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
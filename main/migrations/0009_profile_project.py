# Generated by Django 3.2 on 2021-04-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210429_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='project',
            field=models.CharField(default='', max_length=75),
        ),
    ]
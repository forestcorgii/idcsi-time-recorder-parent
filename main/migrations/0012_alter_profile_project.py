# Generated by Django 3.2 on 2021-05-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_delete_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='project',
            field=models.CharField(blank=True, default='', max_length=75),
        ),
    ]
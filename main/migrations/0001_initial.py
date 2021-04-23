# Generated by Django 3.2 on 2021-04-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=4)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(max_length=75)),
                ('company', models.CharField(max_length=75)),
                ('schedule', models.CharField(max_length=5)),
                ('active', models.BooleanField(default=True)),
                ('admin', models.BooleanField()),
                ('face_data1', models.BinaryField()),
                ('face_data2', models.BinaryField()),
                ('face_data3', models.BinaryField()),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-04-22 14:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('last_synced', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='profile',
            name='employee_id',
            field=models.CharField(blank=True, max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='schedule',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.terminal'),
        ),
    ]

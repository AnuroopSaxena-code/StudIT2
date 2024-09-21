# Generated by Django 5.1.1 on 2024-09-21 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_session_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='session',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='session',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='session',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='session',
            name='user',
        ),
        migrations.AddField(
            model_name='session',
            name='end_datetime',
            field=models.DateTimeField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='start_datetime',
            field=models.DateTimeField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='purpose',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]

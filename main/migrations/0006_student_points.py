# Generated by Django 5.1.1 on 2024-09-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_profile_enrollment_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]

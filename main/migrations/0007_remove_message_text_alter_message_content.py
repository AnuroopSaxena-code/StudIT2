# Generated by Django 5.1.1 on 2024-09-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_message_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='text',
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(),
        ),
    ]

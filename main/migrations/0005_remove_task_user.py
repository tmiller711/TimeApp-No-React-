# Generated by Django 4.1.1 on 2022-09-22 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
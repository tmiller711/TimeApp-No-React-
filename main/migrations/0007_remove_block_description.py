# Generated by Django 4.1.1 on 2022-09-25 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_block_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='description',
        ),
    ]
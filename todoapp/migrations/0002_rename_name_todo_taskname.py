# Generated by Django 4.1.4 on 2022-12-08 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='taskname',
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-05 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200306_0046'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Consumer',
        ),
        migrations.RemoveField(
            model_name='task',
            name='customer',
        ),
    ]

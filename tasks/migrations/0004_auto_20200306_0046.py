# Generated by Django 3.0.3 on 2020-03-05 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200306_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Customer'),
        ),
    ]
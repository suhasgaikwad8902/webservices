# Generated by Django 2.2.6 on 2019-11-20 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentsinfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='spic',
        ),
    ]

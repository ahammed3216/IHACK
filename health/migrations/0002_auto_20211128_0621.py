# Generated by Django 2.2.20 on 2021-11-28 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='date',
        ),
    ]

# Generated by Django 4.0.8 on 2022-12-07 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='profile',
            new_name='profiles',
        ),
    ]

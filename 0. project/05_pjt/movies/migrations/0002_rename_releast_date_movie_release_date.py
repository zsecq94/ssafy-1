# Generated by Django 3.2.13 on 2022-10-07 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='releast_date',
            new_name='release_date',
        ),
    ]
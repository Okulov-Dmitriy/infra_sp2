# Generated by Django 2.2.16 on 2022-07-20 13:51

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('reviews', '0010_auto_20220720_1843'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Genres',
            new_name='Genre',
        ),
        migrations.RenameModel(
            old_name='Titles',
            new_name='Title',
        ),
    ]

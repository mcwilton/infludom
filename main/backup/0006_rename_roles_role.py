# Generated by Django 4.1 on 2022-08-25 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_status_talent_gender_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Roles',
            new_name='Role',
        ),
    ]

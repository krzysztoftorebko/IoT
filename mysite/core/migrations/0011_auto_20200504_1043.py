# Generated by Django 2.1.3 on 2020-05-04 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_about'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Connection',
        ),
    ]
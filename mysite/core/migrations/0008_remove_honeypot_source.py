# Generated by Django 2.1.3 on 2020-05-03 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200502_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='honeypot',
            name='source',
        ),
    ]

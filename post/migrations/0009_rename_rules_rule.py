# Generated by Django 4.2.7 on 2023-11-30 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_rules'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rules',
            new_name='Rule',
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_merge_20231130_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=255)),
            ],
        ),
    ]
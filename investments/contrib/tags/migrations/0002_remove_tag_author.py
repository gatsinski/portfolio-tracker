# Generated by Django 4.0.8 on 2022-11-20 13:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tags", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="author",
        ),
    ]

# Generated by Django 3.2 on 2024-04-30 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_ingredient_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
    ]

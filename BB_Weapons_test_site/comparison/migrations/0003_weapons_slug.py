# Generated by Django 4.2 on 2023-05-02 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0002_alter_weapons_weapon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapons',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
# Generated by Django 4.2.7 on 2024-02-22 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('troops_calculator', '0008_alter_category_name_alter_troop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='troop',
            name='battle_power',
            field=models.FloatField(),
        ),
    ]

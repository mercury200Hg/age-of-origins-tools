# Generated by Django 4.2.7 on 2023-11-27 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('troops_calculator', '0007_remove_troop_city_level_required_category_building_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='troop',
            name='name',
            field=models.TextField(max_length=100, unique=True),
        ),
    ]

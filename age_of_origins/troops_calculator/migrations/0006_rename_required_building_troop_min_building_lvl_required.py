# Generated by Django 4.2.7 on 2023-11-27 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('troops_calculator', '0005_rename_lane_category_row'),
    ]

    operations = [
        migrations.RenameField(
            model_name='troop',
            old_name='required_building',
            new_name='min_building_lvl_required',
        ),
    ]

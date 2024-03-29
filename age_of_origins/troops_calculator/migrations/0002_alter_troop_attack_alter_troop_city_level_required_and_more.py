# Generated by Django 4.2.7 on 2023-11-27 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('troops_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='troop',
            name='attack',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='troop',
            name='city_level_required',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='troop',
            name='level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='troop',
            name='load_capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='troop',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='troop',
            name='units',
            field=models.IntegerField(),
        ),
    ]

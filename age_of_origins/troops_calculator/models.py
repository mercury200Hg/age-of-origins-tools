from django.db import models


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=40, unique=True)
    row = models.TextField(max_length=20)
    building = models.TextField(max_length=40, default=None)


class Troop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, unique=True)
    level = models.IntegerField()
    battle_power = models.FloatField()
    load_capacity = models.IntegerField()
    attack = models.IntegerField()
    units = models.IntegerField()
    min_building_lvl_required = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


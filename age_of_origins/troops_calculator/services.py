import math

from troops_calculator.models import Troop, Category
from django.db.models.functions import RowNumber
from django.db.models.expressions import Window
from django.db.models import F
from django.db.models import Max


class ComputeTroops:
    @staticmethod
    def compute_city_attack(city_level: int, max_troops_capacity: int, shredder_count: int):
        troops_computed = []
        capacity_left = max_troops_capacity
        troops_set1 = Troop.objects.filter(min_building_lvl_required__lte=city_level).values()
        print(troops_set1.query)
        troops_set2 = troops_set1.annotate(row_number=Window(
            expression=RowNumber(),
            partition_by=[F('category__name')],
            order_by=F('attack').desc()
        )).filter(row_number=1).values('category__name', 'units', 'battle_power', 'attack',
                                       'name', 'level', 'min_building_lvl_required',
                                       'category__row')
        print(troops_set2.query)
        print(troops_set2.values())
        sniper_min_building_lvl_required = 1
        cannon_min_building_lvl_required = 1
        for troop in troops_set2:
            category_name = troop.get('category__name')
            unit = troop.get('units')
            row = troop.get('category__row')
            attack = troop.get('attack')
            battle_power = troop.get('battle_power')
            min_building_lvl_required = troop.get('min_building_lvl_required')
            if str(category_name).lower() == 'shredder':
                troop_count = shredder_count
            elif str(category_name).lower() == 'sniper':
                sniper_min_building_lvl_required = min_building_lvl_required
                continue
            elif str(category_name).lower() == 'cannon':
                cannon_min_building_lvl_required = min_building_lvl_required
                continue
            else:
                troop_count = 1
            capacity_left -= (troop_count * unit)
            troops_computed.append({
                "row": row,
                "category": category_name,
                "count": troop_count,
                "attack": attack * troop_count,
                "battle_power": battle_power * troop_count
            })
        for troop in troops_set2:
            category_name = troop.get('category__name')
            unit = troop.get('units')
            row = troop.get('category__row')
            attack = troop.get('attack')
            battle_power = troop.get('battle_power')
            if str(category_name).lower() == 'cannon':
                if cannon_min_building_lvl_required > sniper_min_building_lvl_required:
                    troop_count = math.floor(0.8 * capacity_left)
                    capacity_left -= troop_count
                else:
                    troop_count = math.floor(0.2 * capacity_left)
                    capacity_left -= troop_count
            elif str(category_name).lower() == 'sniper':
                if sniper_min_building_lvl_required > cannon_min_building_lvl_required:
                    troop_count = math.floor(0.8 * capacity_left / unit)
                    capacity_left -= troop_count
                else:
                    troop_count = math.floor(0.2 * capacity_left / unit)
                    capacity_left -= troop_count
            else:
                continue
            troops_computed.append({
                "row": row,
                "category": category_name,
                "count": math.floor(troop_count / unit),
                "attack": attack,
                "battle_power": battle_power
            })
        for troop in troops_computed:
            if troop.get('category').lower() == 'sniper':
                troop["count"] += capacity_left
            troop["attack"] *= troop["count"]
            troop["battle_power"] *= troop["count"]
        return troops_computed

    @staticmethod
    def compute_medici(city_level: int, max_troops_capacity: int):
        troops_computed = []
        capacity_left = max_troops_capacity
        troops_set1 = Troop.objects.filter(min_building_lvl_required__lte=city_level).values()
        print(troops_set1.query)
        troops_set2 = troops_set1.annotate(row_number=Window(
            expression=RowNumber(),
            partition_by=[F('category__name')],
            order_by=F('attack').desc()
        )).filter(row_number=1).values('category__name', 'units', 'battle_power', 'attack',
                                       'name', 'level',
                                       'category__row')
        print(troops_set2.query)
        print(troops_set2.values())
        front_troops_count = math.floor(max_troops_capacity * 0.1) / 4
        mid_troops_count = math.floor(max_troops_capacity * 0.1) / 4
        back_troops_count = math.floor(max_troops_capacity * 0.8) / 4
        for troop in troops_set2:
            category_name = troop.get("category__name")
            unit = troop.get("units")
            row = troop.get("category__row")
            attack = troop.get('attack')
            battle_power = troop.get('battle_power')
            row_troops_count = 0
            match row:
                case "Front":
                    row_troops_count = front_troops_count
                case "Middle":
                    row_troops_count = mid_troops_count
                case "Back":
                    row_troops_count = back_troops_count
            troop_count = math.floor(row_troops_count / unit)
            capacity_left -= (troop_count * unit)
            troops_computed.append({
                "row": row,
                "category": category_name,
                "count": troop_count,
                "attack": attack,
                "battle_power": battle_power
            })

        for troop in troops_computed:
            if troop.get('category') == 'Sniper':
                troop["count"] += capacity_left
            troop["attack"] *= troop["count"]
            troop["battle_power"] *= troop["count"]
        return troops_computed

    @staticmethod
    def compute_triangle_war_or_dod(city_level: int, max_troops_capacity: int):
        return []

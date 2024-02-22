from django.shortcuts import render
from troops_calculator.services import ComputeTroops
from enum import Enum
from django import template

register = template.Library()


class Events(Enum):
    CITY_ATTACK = "City attack"
    TRIANGLE_WAR_OR_DOD = "Triangle War or Duel of Dominance"
    MEDICI = "Medici"


events = []
for item in Events:
    events.append({
        "name": item.name,
        "value": item.value
    })


def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{} {}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])





def index(request):
    context = {
        "data": {
            "events": events
        }
    }
    if request.method != 'POST':
        return render(request, template_name="troops_calculator/index.html", context=context,
                      status=200)

    city_level = request.POST.get("city_level")
    max_troops_capacity = int(request.POST.get("max_troops_capacity"))
    event_name = request.POST.get("event_name")
    shredder_count = int(request.POST.get('shredder_count'))
    print(city_level, max_troops_capacity, event_name, shredder_count)
    computed_troops = {'data': {}}
    if event_name == Events.CITY_ATTACK.value:
        computed_troops = {
            'data': {
                'troops': ComputeTroops.compute_city_attack(city_level=city_level,
                                                            max_troops_capacity=max_troops_capacity,
                                                            shredder_count=shredder_count),
                'message': 'City attack with max cannons and snipers and rest 1 of each'
            }
        }
    elif event_name == Events.MEDICI.value:
        computed_troops = {
            'data': {
                'troops': ComputeTroops.compute_medici(city_level=city_level, max_troops_capacity=max_troops_capacity),
                'message': 'Medici formation with 10% front, 10% mid and 80% back formation'
            }
        }
    elif event_name == Events.TRIANGLE_WAR_OR_DOD.value:
        computed_troops = {
            'data': {
                'troops': ComputeTroops.compute_triangle_war_or_dod(city_level=city_level,
                                                                    max_troops_capacity=max_troops_capacity),
                'message': 'Feature coming soon'
            }
        }
    troops_total_attack_power = 0
    for troop in computed_troops.get('data').get('troops', []):
        troops_total_attack_power += troop.get('attack')
    troops_total_battle_power = 0
    for troop in computed_troops.get('data').get('troops', []):
        troops_total_battle_power += troop.get('battle_power')
        troop['battle_power'] = human_format(troop['battle_power'])
    computed_troops['data']['troops_total_attack_power'] = human_format(troops_total_attack_power)
    computed_troops['data']['troops_total_battle_power'] = human_format(troops_total_battle_power)
    computed_troops['data']['events'] = events
    computed_troops['data']['city_level'] = city_level
    computed_troops['data']['max_troops_capacity'] = max_troops_capacity
    computed_troops['data']['event_name'] = event_name
    if shredder_count is None:
        computed_troops['data']['shredder_count'] = 1
    else:
        computed_troops['data']['shredder_count'] = shredder_count

    return render(request, template_name="troops_calculator/index.html", context=computed_troops,
                  status=200)

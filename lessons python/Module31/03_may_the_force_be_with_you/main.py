import json
import requests
from pprint import pprint

if __name__ == '__main__':

    def search_ship(file, ship):
        for key, value in file.items():
            if value == ship:
                result = file
            if isinstance(value, dict):
                search_ship(value, ship)
            if isinstance(value, list):
                for i_value, j_value in enumerate(value):
                    for key, value in j_value.items():
                        if value == ship:
                            result = j_value
        return result


    my_req = requests.get('https://swapi.dev/api/starships/')
    res = json.loads(my_req.text)
    right_ship = 'X-wing'
    result_ship = search_ship(res, right_ship)

    starships = {'name': result_ship['name'],
                 'max_atmosphering_speed': result_ship['max_atmosphering_speed'],
                 'starship_class': result_ship['starship_class'],
                 'pilots': []}
    for i in result_ship['pilots']:
        pilot = requests.get(i)
        json_pilot = json.loads(pilot.text)
        planet = requests.get(json_pilot['homeworld'])
        json_planet = json.loads(planet.text)
        info_pilot = {'name': json_pilot['name'],
                      'height': json_pilot['height'],
                      'mass': json_pilot['mass'],
                      'homeworld': json_planet['name'],
                      'homeworld_url': json_pilot['homeworld']}
        starships['pilots'].append(info_pilot)
    pprint(starships)

    with open('X_wing.json', 'w') as file:
        json.dump(starships, file, indent=4)

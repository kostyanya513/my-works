import json
import requests

if __name__ == '__main__':

    my_req = requests.get('https://swapi.dev/api/starships/12/')
    res = json.loads(my_req.text)

    starships = {'name': res['name'],
                 'max_atmosphering_speed': res['max_atmosphering_speed'],
                 'starship_class': res['starship_class'],
                 'pilots': []}
    for i in res['pilots']:
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
    print(starships)

    with open('X_wing.json', 'w') as file:
        json.dump(starships, file, indent=4)

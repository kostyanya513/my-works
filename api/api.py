import requests

from typing import Dict
from config_data.config import API_KEY, API_GEO, API_TEMP, API_COORD


def api_request(endpoint: str, params=None) -> requests.Response:
    if params is None:
        params = {}
    params['appid'] = API_KEY
    return requests.get(
        f'{endpoint}',
        params=params
    )


def get_location(q: str, limit: int = 5) -> Dict:
    response = api_request(endpoint=f'{API_GEO}', params={
        'q': q,
        'limit': limit
    })
    if response.status_code == requests.codes.ok:
        return response.json()


def get_coord(lat: str, lon: str, units: str = 'metric', lang: str = 'ru') -> Dict:
    response = api_request(f'{API_COORD}', params={
        'lat': lat,
        'lon': lon,
        'units': units,
        'lang': lang
    })
    if response.status_code == requests.codes.ok:
        return response.json()


def get_temp(lat: str, lon: str, units: str = 'metric') -> Dict:
    response = api_request(f'{API_TEMP}', params={
        'lat': lat,
        'lon': lon,
        'units': units
    })
    if response.status_code == requests.codes.ok:
        return response.json()

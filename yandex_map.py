import requests

map_file = 'static/img/map_file.png'


def get_image(city: str):
    bbox = get_cords_bbox_city(city)
    return from_cords_to_map(bbox)


def get_cords_bbox_city(city: str) -> str:
    """INPUT CITY AND GIVE BBOX CORDS"""
    bbox = ''
    server = 'https://geocode-maps.yandex.ru/v1/?'
    params = {
        'apikey': '8013b162-6b42-4997-9691-77b7074026e0',
        'geocode': city,
        'lang': 'ru-RU',
        'kind': 'locality',
        'format': 'json'
    }
    response = requests.get(server, params=params)
    if response.status_code == 200:
        envelope = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy'][
            'Envelope']
        bbox += envelope['lowerCorner'].replace(' ', ',')
        bbox += '~' + envelope['upperCorner'].replace(' ', ',')
        return bbox


def from_cords_to_map(bbox):
    """GIVE MAP IMAGE BYTE"""
    server = 'https://static-maps.yandex.ru/v1'
    params = {
        'apikey': 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13',
        'bbox': bbox,
    }
    response = requests.get(server, params=params)
    if response.status_code == 200:
        with open(map_file, 'wb') as file:
            file.write(response.content)
        return True
    return False


if __name__ == '__main__':
    bbox = get_cords_bbox_city('Россошь')
    from_cords_to_map(bbox)

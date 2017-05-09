import requests
from keys import API_key
from texts import none_rating


def info_about_place(description, lat, lng):
    i = 0
    location_parsed = str(lat) + ',' + str(lng)
    places = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?name='+description
                          + '&language=ru&location=' + location_parsed + '&radius=1000&key=' + API_key[0])
    while places.json()['status'] == 'OVER_QUERY_LIMIT':
        places = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?name=' + description
                              + '&language=ru&location=' + location_parsed + '&radius=1000&key=' + API_key[i])
        i += 1
        if i == 9:
            break
    return places.json()


def open_hours(call_data):
    i = 0
    place_id = call_data[1:len(call_data)]
    place = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='
                         + place_id + '&language=ru&key=' + API_key[0])
    while place.json()['status'] == 'OVER_QUERY_LIMIT':
        place = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='
                             + place_id + '&language=ru&key=' + API_key[i])
        i += 1
        if i == 9:
            break
    place_parsed = place.json()
    open_info = place_parsed['result']['name'] + '\n' + '📌 Режим работы 📌'
    for week_day in place_parsed['result']['opening_hours']['weekday_text']:
        open_info += '\n' + week_day
    return open_info


def address_info(place_id):
    i = 0
    place = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='
                         + place_id + '&language=ru&key=' + API_key[0])
    while place.json()['status'] == 'OVER_QUERY_LIMIT':
        place = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='
                             + place_id + '&language=ru&key=' + API_key[i])
        i += 1
        if i == 9:
            break
    place_parsed = place.json()
    address = str(place_parsed['result']['formatted_address'])
    return address


def rating_info(call_data):
    i = 0
    place_id = call_data[1:len(call_data)]
    place = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='
                         + place_id + '&language=ru&key=' + API_key[0])
    while place.json()['status'] == 'OVER_QUERY_LIMIT':
        place = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='
                             + place_id + '&language=ru&key=' + API_key[i])
        i += 1
        if i == 9:
            break
    place_parsed = place.json()
    try:
        str(place_parsed['result']['rating']) == ''
    except KeyError:
        return none_rating
    rating = 'Рейтинг: '
    stars = int(place_parsed['result']['rating'])
    for i in range(stars):
        rating += '⭐'
    return rating
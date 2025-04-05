from xml.etree.ElementTree import tostring

import requests

ACCESS_TOKEN = 'a06933fa84f3d9af1810338a6744a1a1c6ef955f'
CLUB_ID = '1446329'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

params = {
    'per_page': 100,
    'page': 1
}

class osoba:
    imie = ""
    dystans_caly = 0


osoby_id = {}

with open("indextemp.html", "r+", encoding="utf-8") as file:
    html = file.read()


response = requests.get(f'https://www.strava.com/api/v3/clubs/{CLUB_ID}/activities', headers=headers, params=params)

if response.status_code == 200:
    activities = response.json()
    for activity in activities:
        athlete = activity['athlete']
        first_name = athlete['firstname']
        last_initial = athlete['lastname']
        distance = activity['distance'] / 1000
        # print(first_name,distance)
        if(first_name in osoby_id):
            osoby_id[first_name].dystans_caly += distance
        else:
            osoby_id[first_name] = osoba()
            osoby_id[first_name].imie = first_name
            osoby_id[first_name].dystans_caly = distance
else:
    print(f'Błąd: {response.status_code}, {response.text}')

a = 1

for i in sorted(osoby_id.values(), key=lambda x: x.dystans_caly,reverse=True):
    print(i.imie, " ", str(round(i.dystans_caly,2)))
    html = html.replace("NAME"+ str(a), str(i.imie))
    html = html.replace("DISTANCE"+ str(a), str(round(i.dystans_caly,3)))
    a += 1


with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)

import requests
from bs4 import BeautifulSoup


def data_extraction():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        datetime = soup.find('span', {'class': 'waktu'})
        datetime = datetime.text.split(', ')
        date = datetime[0]
        time = datetime[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitude = None
        depth = None
        ls = None
        bt = None
        epicenter = None
        mmI_scale = None

        for res in result:
            if i == 1:
                magnitude = res.text
            elif i == 2:
                depth = res.text
            elif i == 3:
                location = res.text.split(' - ')
                ls = location[0]
                bt = location[1]
            elif i ==4:
                epicenter = res.text
            elif i == 5:
                mmI_scale = res.text
            i = i + 1

        hasil = dict()
        hasil['date'] = date
        hasil['time'] = time
        hasil['magnitude'] = magnitude
        hasil['depth'] = depth
        hasil['location'] = {'ls': ls, 'bt': bt}
        hasil['epicenter'] = epicenter
        hasil['mmI_scale'] = mmI_scale
        return hasil
    else:
        return None

def display_data(result):
    if result is None:
        print('Unable to find recent earthquake data')
        return
    print("Latest Earthquake based on BMKG")
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Depth: {result['depth']}")
    print(f"Location: {result['location']['ls']} - {result['location']['bt']}")
    print(f"Epicenter {result['epicenter']}")
    print(f"MMI Scale: {result['mmI_scale']}")


"""
Recent Earthquake Detection Application
MODULARIZATION WITH FUNCTION
"""


def data_extraction():
    """
    Date: 21 September 2023
    Time: 15:14:35 WIB
    Magnitude: 3.6
    Depth: 3 km
    Location: LS = 8.31 BT = 123.56
    Epicenter: Pusat gempa berada di laut 19 km TimurLaut Lembata
    MMI Scale: II Lembata
    :return:
    """
    hasil = dict()
    hasil['date'] = '21 September 2023'
    hasil['time'] = '15:14:35 WIB'
    hasil['magnitude'] = 3.6
    hasil['depth'] = '3 km'
    hasil['location'] = {'ls': 8.31, 'bt': 123.56}
    hasil['epicenter'] = 'Pusat gempa berada di laut 19 km TimurLaut Lembata'
    hasil['mmI_scale'] = 'II Lembata'

    return hasil

def display_data(result):
    print("Latest Earthquake based on BMKG")
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Depth: {result['depth']}")
    print(f"Location: LS: {result['location']['ls']}, BT: {result['location']['bt']}")
    print(f"Epicenter {result['epicenter']}")
    print(f"MMI Scale: {result['mmI_scale']}")


if __name__ == '__main__':
    print("Main Application")
    result = data_extraction()
    display_data(result)
    
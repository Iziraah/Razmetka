import requests
import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

client_id = 'SecondKey'
client_secret = 'fsq3IjUrLao8dFwY4sPnCNnAFiNY1fSsPOWafjzqBD0ae0w=='
version = '20180605'

category = input("Введите интересующую вас категорию (например, 'кофейни', 'музеи', 'парки'): ")


url = 'https://api.foursquare.com/v2/venues/search?near=Москва&query={}&client_id={}&client_secret={}&v={}'.format(category, client_id, client_secret, version)


response = requests.get(url)
data = json.loads(response.text)

for venue in data['response']['venues']:
    name = venue['name']
    address = ', '.join(venue['location']['formattedAddress'])
    
    # Запрос на получение деталей места
    url_detail = 'https://api.foursquare.com/v2/venues/{}?&client_id={}&client_secret={}&v={}'.format(venue['id'], client_id, client_secret, version)
    response_detail = requests.get(url_detail)
    data_detail = json.loads(response_detail.text)
    
    rating = data_detail['response']['venue'].get('rating', 'Рейтинг отсутствует')

    print('Название: {}, Адрес: {}, Рейтинг: {}'.format(name, address, rating))
import requests

ngrok_url = 'https://0e4939430e14.ngrok.io/'
endpoint = f'{ngrok_url}box-office-mojo-scrapper'

r = requests.post(endpoint, json={})
print(r.text)
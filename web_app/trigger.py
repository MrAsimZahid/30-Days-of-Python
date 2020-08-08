import requests

ngrok_url = 'https://6e7da3c80771.ngrok.io/'
endpoint = f'{ngrok_url}box-office-mojo-scrapper'

r = requests.post(endpoint, json={})
print(r.text)
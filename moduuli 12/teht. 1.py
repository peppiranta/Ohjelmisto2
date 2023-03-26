import requests

# Hae satunnainen vitsi rajapinnasta
response = requests.get('https://api.chucknorris.io/jokes/random')
data = response.json()

# Tulosta vitsin teksti
print(data['value'])

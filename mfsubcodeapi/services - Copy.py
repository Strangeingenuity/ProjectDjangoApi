import requests
from requests.exceptions import RequestException
from requests.auth import HTTPBasicAuth
import json

def get_animals(name):
	url = 'https://th-apex-http-callout.herokuapp.com/animals' 
	head = {'Content-type':'application/json',
             'Accept':'application/json'}
	#params = {'name': name}
	#r = requests.post(url, params=params)
	resp = requests.get(url)
	#books = resp.json()
	#data = json.loads(resp);
	animal_list = resp.text
	print(animal_list);
	#animal_list = {'animalname':books['results']}

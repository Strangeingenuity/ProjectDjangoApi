import requests
from requests.exceptions import RequestException
from requests.auth import HTTPBasicAuth
import json

def get_animals():
	url = 'http://205.174.35.1:3427/hbscript/addSubscriber' 
	head = {'Content-type':'application/json',
			 'Accept':'application/json'}
	payload  = {
			"preamble":"tca1",
			"kindOfBusiness":"bb",
			"subType":"s",
			"status":"n",
			"companyID":"782",
			"businessName":"Bobs Burgers",
			"primaryServiceArea":"S66",
			"address":{
						"name":"Bobby B",
						"attn":"Hey Bob Alexander",
						"street":"51 E 7th Ave",
						"city":"Stillwater",
						"state":"ok",
						"zip":"74074",
						"country":"",
						"phone":"4055332900"
			},
			"billcode":"355",
			"serviceRules": [
						{
									"type":"40",
									"id": "400",
									"select": "Y"
						},{
									"type":"10",
									"id":"131",
									"select": "Y"
						}
			]           
	}
	response = requests.post(url, json=payload,auth=HTTPBasicAuth('dir01tp','$Lik2w3e'))		 
	animal_list = response.text
	animal_list = json.loads(response.text)
	return animal_list
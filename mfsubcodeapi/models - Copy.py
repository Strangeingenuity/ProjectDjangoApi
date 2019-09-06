from django.db import models
import requests
from requests.exceptions import RequestException
from requests.auth import HTTPBasicAuth
import json

# Create your models here.
class Subcode(models.Model):	
		#something = models.CharField(max_length=500)
		#json = JSONField()
		
	def get_something(self):
			try:
				print('Tyaga here 11111');
				url = 'http://205.174.35.1:3427/hbscript/addSubscriber'
				head = {'Content-type':'application/json','Accept':'application/json'}
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

				response = requests.post(url, json=payload,auth=HTTPBasicAuth('dir01tp','$Lik1q2w'))
					
			except RequestException as e:
				return {'success': False, 'error': 'Other service unavailable!'}

			if response.status_code not in [200, 201, 202, 203, 204, 205]:
				return {'success': False, 'error': 'Something went wrong ({}): {}'.format(response.status_code, response.content)}
			data = json.load(response.content)
			data['success'] = True
			print('Tyaga here 11111');
			return data

	def something(self):
			 self.get_something()
			
			
	#def __str__(self):
	#		return '%s %s' % (self.body)
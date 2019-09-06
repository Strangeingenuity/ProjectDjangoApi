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
				url = 'https://th-apex-http-callout.herokuapp.com/animals'
				head = {'Content-type':'application/json','Accept':'application/json'}
				payload  = {
							"name":"mighty moose1111"         
				}

				response = requests.post(url, json=payload)
					
			except RequestException as e:
				return {'success': False, 'error': 'Other service unavailable!'}

			if response.status_code not in [200, 201, 202, 203, 204, 205]:
				return {'success': False, 'error': 'Something went wrong ({}): {}'.format(response.status_code, response.content)}
			data = json.load(response.content)
			assert False
			data['success'] = True
			print('Tyaga here 11111');
			return data

	#def something(self):
	#		 self.get_something()
			
			
	#def __str__(self):
	#		return '%s %s' % (self.body)
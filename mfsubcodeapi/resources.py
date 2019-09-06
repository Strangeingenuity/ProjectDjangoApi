from tastypie.resources import ModelResource
from tastypie.resources import Resource
from mfsubcodeapi.models import Subcode
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
#added these lines to fetch data from the mainframe API
import requests
from requests.auth import HTTPBasicAuth
import json


class SbCodeResource(ModelResource):
	class Meta:	
		queryset = Subcode.objects.all()
		#allowed_methods = ['get']
		resource_name  ='subcode'

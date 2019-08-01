from tastypie.resources import ModelResource
from pyapisubcode.models import Note
from tastypie import fields
from tastypie.authorization import DjangoAuthorization

class NoteResource(ModelResource):
	class Meta:
		queryset = Note.objects.all()
		resource_name  ='note'

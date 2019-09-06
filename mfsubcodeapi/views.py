from django.shortcuts import render
from django.views import generic
#assert False
# Create your views here.
from . import services
#class AnimalPage(generic.TemplateView):
def get(request):
	animal_list = services.get_animals()
	return render(request,'mfsubcodeapi/basic.html',{'array1':animal_list})
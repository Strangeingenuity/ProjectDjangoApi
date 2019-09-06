"""pyrestapimnframe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from pyapisubcode.resources import NoteResource
from mfsubcodeapi.resources import SbCodeResource

note_resources = NoteResource()
print('tyaga here')
subcode_resource = SbCodeResource()
urlpatterns = [
    path(r'^admin/', admin.site.urls),
	url(r'^pyapisubcode/',include(note_resources.urls)),
	url(r'^mfsubcodeapi/', include('mfsubcodeapi.urls')),
	#url(r'^mfsubcodeapi/',include(subcode_resource.urls))
	
]

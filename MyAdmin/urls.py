from MyAdmin.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns=[
			
url(r'^Form_View/$', Form_View),
url(r'^save/$', Save),
url(r'^showform/$', showforms),
url(r'^show2form/$', show2form),
url(r'^feedbackform/$', feedbackform),
url(r'^detailform/$', detailform),
			
]

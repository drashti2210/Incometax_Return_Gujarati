from django.urls import path
from income_tax.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [

url(r'^Form_View/$', Form_View),
url(r'^save/$', Save),
url(r'^showform/$', showforms),
url(r'^show2form/$', show2form),
url(r'^feedbackform/$', feedbackform),
url(r'^itr2/$', itr2),
url(r'^itr21/$', itr21),
url(r'^itr21/$', itr21),
url(r'^change_password/$', change_password),
url(r'^change_password1/$', change_password1),
path('delete/<int:id>', delete),
path('delete1/<int:id>', delete1),
url(r'^detailform/$', detailform),
url(r'^login/$', login),
url(r'^auth_view/$', auth_view),
url(r'^try1/$', try1),
url(r'^logout/$', logout),
url(r'^loggedin/$', loggedin),
url(r'^invalidlogin/$', invalidlogin),
url(r'^registration/$', registration),
url('itr1bform1',itr1bform1),
url('home',home),
url('show',show),
url('home1',home1),
url('welcome',welcome),

url('itr1dform1',itr1dform1),
url(r'^itr1form/$', itr1form),
url(r'^itr1form1/$', itr1form1),
url(r'^itr1bform/$', itr1bform),
url(r'^itr1dform/$', itr1dform),
url(r'^new_registration/$', new_registration),
url(r'^cgi/$', cgi),
url(r'^index/$', index),
url(r'^UpdateInfo/$', UpdateInfo),
url(r'^updateIn/$', updateIn),
url(r'^profile2/$',profile2),
url(r'^useinfo/$',useinfo),
url(r'^useinfo1/$',useinfo1),
]
from . import views
from django.urls import path,include
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns=[
path("hospitallogin/",views.hospitallogin,name="hospitallogin"),
path("hospitalhome/",views.home,name="hospitalhome"),
url(r'^ajax/validateqrcode/$', views.validate_qrcode, name='validate_qrcode'),
]
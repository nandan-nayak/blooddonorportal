from . import views
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
path("donorlogin/",views.donorlogin,name="donorlogin"),
path("donorhome/",views.donorhome,name="donorhome"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
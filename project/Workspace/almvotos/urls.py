from django.conf.urls import url, include
from django.contrib import admin
from api.resources import VotoResource

voto_resource = VotoResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(voto_resource.urls)),
]
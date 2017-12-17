from django.conf.urls import url, include
from django.contrib import admin
from api.resources import VoteResource

vote_resource = VoteResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(vote_resource.urls)),
]
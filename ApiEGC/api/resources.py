from tastypie.resources import ModelResource
from api.models import Voto
from tastypie.authorization import Authorization

class VotoResource(ModelResource):
    class Meta:
        queryset = Voto.objects.all()
        resource_name = 'voto'
        authorization = Authorization()
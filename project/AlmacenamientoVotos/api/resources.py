from tastypie.resources import ModelResource
from api.models import Vote
from tastypie.authorization import Authorization

class VoteResource(ModelResource):
    class Meta:
        queryset = Vote.objects.all()
        resource_name = 'vote'
        authorization = Authorization()

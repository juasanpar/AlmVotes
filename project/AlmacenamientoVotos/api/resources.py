from tastypie.resources import ModelResource
from api.models import vote
from tastypie.authorization import Authorization

class VoteResource(ModelResource):
    class Meta:
        queryset = vote.objects.all()
        resource_name = 'vote'
        authorization = Authorization()
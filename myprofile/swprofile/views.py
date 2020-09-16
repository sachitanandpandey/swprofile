from rest_framework import viewsets
from swprofile.serializers import homeSerializer, postme
from swprofile .models import homemsg, posts


class msg(viewsets.ReadOnlyModelViewSet):
    serializer_class = homeSerializer
    queryset = homemsg.objects.all()
 #   lookup_field = 'id'

class postblog(viewsets.ReadOnlyModelViewSet):
    serializer_class = postme
    queryset = posts.objects.all()
 #   lookup_field = 'id'





from rest_framework import serializers
from .models import homemsg, posts

class homeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = homemsg
        fields = ['homemessage']

class postme(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = posts
        fields = ['title', 'Image', 'description']
from django.contrib.auth.models import User, Group
from waterfall_wall.models import Image
from rest_framework import serializers


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('path', 'url', 'nude_percent')

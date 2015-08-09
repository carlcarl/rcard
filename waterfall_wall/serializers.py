from django.contrib.auth.models import User, Group
from waterfall_wall.models import Image
from rest_framework import serializers


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.path.url

    class Meta:
        model = Image
        fields = ('url', 'nude_percent')

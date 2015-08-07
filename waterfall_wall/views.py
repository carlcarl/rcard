from django.shortcuts import render
from rest_framework import viewsets
from waterfall_wall.serializers import ImageSerializer
from waterfall_wall.models import Image

def index(request):
    context = {}
    return render(request, 'waterfall_wall/index.html', context)


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import ImageAnnotator

import json

@api_view(['GET', 'PATCH'])
@permission_classes((AllowAny, ))
def image_annotator(request):
    """
    Return image metadata.
    """
    if request.method == 'GET':
        try:
            image_annotator = ImageAnnotator.objects.get(pk=1)
            return Response(image_annotator.content)
        except ImageAnnotator.DoesNotExist:
            return Response({})

    elif request.method == 'PATCH':
        print(type(request.data['content']))
        try:
            image_annotator = ImageAnnotator.objects.get(pk=1)
        except ImageAnnotator.DoesNotExist:
            image_annotator = ImageAnnotator()
        image_annotator.content = request.data['content']
        image_annotator.save()
        return Response(image_annotator.content, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def handle_annotation(request):
    print ('------------ fsdfa: {}'.format(request.body))
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print ('---- JSON DATA ----\nDATA: {}'.format(json_data))
    return Response({})

def index(request):
    return render(request, 'index.html')

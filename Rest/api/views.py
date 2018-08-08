# third party lib  imports
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

# core django imports
from django.shortcuts import render

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    '''
    Class that defines the create behaviour of the API view
    '''

    queryset = Bucketlist.objects.all()
    serializer_class  = BucketlistSerializer

    def perform_create(self,serializer):
        '''
        Save the post data when creating a new bucketlist
        '''
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    '''
    This is the class that handles the GET, PUT  and DELETE requests
    '''

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

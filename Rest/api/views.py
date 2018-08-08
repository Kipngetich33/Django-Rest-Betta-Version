# third party lib  imports
from rest_framework import generics
from .permissions import IsOwner
from .serializers import BucketlistSerializer
from .models import Bucketlist
from rest_framework import permissions

# core django imports
from django.shortcuts import render

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    '''
    Class that defines the create behaviour of the API view
    '''

    queryset = Bucketlist.objects.all()
    serializer_class  = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    

    def perform_create(self,serializer):
        '''
        Save the post data when creating a new bucketlist
        '''
        serializer.save(owner=self.request.user) 
        permission_classes = (permissions.IsAuthenticated,)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    '''
    This is the class that handles the GET, PUT  and DELETE requests
    '''
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

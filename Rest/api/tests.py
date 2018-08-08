
# third party library imports
from rest_framework.test import APIClient
from rest_framework import status

# local app imports e.g. models
from django.test import TestCase
from .models import Bucketlist
from django.core.urlresolvers import reverse


class ModelTestCase(TestCase):
    '''
    Defines tests for the model test case
    '''
    
    def setUp(self):
        '''
        Runs at the beggging of every test
        '''

        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name = self.bucketlist_name)
        self.bucketlist = Bucketlist(name = self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        '''
        tests if the models can create a bucketlist
        '''

        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count,new_count)


class ViewTestCase(TestCase):
    '''
    Test suite for the api views
    '''

    def setUp(self):
        '''
        Defines the test client and other test varibles
        '''

        self.client = APIClient()
        self.bucketlist_data = {'name':'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format = "json"
        )


    def test_api_can_create_a_bucketlist(self):
        '''
        Tests the capability of the Api to create a bucket list
        '''
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)
        

    def test_api_can_get_a_bucketlist(self):
        '''
        Tests if the API can get a given bucketlist
        '''
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': bucketlist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        '''
        Test the api can update a given bucketlist 
        '''
        bucketlist = Bucketlist.objects.first()
        change_bucketlist = {'name':'Something new'}
        res = self.client.put(
            reverse('details', kwargs ={'pk':bucketlist.id}),
            change_bucketlist, format='json'

        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_api_can_delete_bucketlist(self):
        '''
        Test if the API can delete a bucketlist
        '''

        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details',
            kwargs = {'pk':bucketlist.id}),
            format = 'json',
            follow = True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


    

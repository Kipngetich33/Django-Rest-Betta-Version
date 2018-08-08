
# third party library imports
from rest_framework.test import APIClient
from rest_framework import status

# local app imports e.g. models
from django.test import TestCase
from .models import Bucketlist
from django.core.urlresolvers import reverse
# rest_api/tests.py
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    '''
    Defines tests for the model test case
    '''
    
    def setUp(self):
        '''
        Runs at the beggging of every test
        '''

        user = User.objects.create(username="nerd") 
        self.name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.name, owner=user)

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
        user = User.objects.create(username = "nerd")

        #Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user = user)

        # since user model is not serializable use its ID or PK
        self.bucketlist_data = {'name':'Go to Ibiza', 'owner':user.id}
        self.response =self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format = "json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/bucketlists/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = Bucketlist.objects.get(id=1)
        response = self.client.get(
            '/bucketlists/',
            kwargs={'pk': bucketlist.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    

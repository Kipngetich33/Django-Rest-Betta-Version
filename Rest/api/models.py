from django.db import models

# Create your models here.
class Bucketlist(models.Model):
    '''
    This class represents the bucketlist model
    '''

    name = models.CharField(max_length = 225, blank = False, unique = True )
    owner = models.ForeignKey('auth.User',  # ADD THIS FIELD
    related_name='bucketlists', 
    on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add = True)
    date_modified = models.DateField(auto_now = True)

    def __str__(self):
        '''
        Return a human readable representation of the model 
        instance
        '''
        return "{}".format(self.name)


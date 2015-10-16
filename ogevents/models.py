import datetime
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author       = models.ForeignKey('auth.User')
    author_name  = models.CharField(max_length=20,default="schememanager")
    title        = models.DateField('Event date in the format yyyy-mm-dd, e.g for the 24th of August 2015, enter 2015-08-24',max_length=10)
    text         = models.TextField('Event details')
    created_date = models.DateTimeField(default=timezone.now)
    status       = models.BooleanField(default=True)
    def __str__(self):               
        return self.text
    def publish(self):
        self.save()

  

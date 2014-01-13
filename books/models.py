from django.db import models
import datetime

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __unicode__(self):
        #return u'%s %s' % (self.title,self.authors)
        return self.title

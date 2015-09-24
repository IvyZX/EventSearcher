from django.db import models


class Event(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, max_length=20)
    name = models.CharField(max_length=5000)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    latitude = models.DecimalField(max_digits=14, decimal_places=10)
    longitude = models.DecimalField(max_digits=14, decimal_places=10)
    def __unicode__(self):
        return str(self.name) + " - " + str(self.event_id)


class Tweet(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    text = models.CharField(max_length=5000)
    author = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField(blank=True)
    event = models.ForeignKey(Event)
    num_retweet = models.IntegerField()
    pic_url = models.URLField()
    def __unicode__(self):
        return self.author + " " + self.text[:10]

'''
class Fbpost(models.Model):
    postid = models.IntegerField(primary_key=True, editable=False)
    text = models.CharField(max_length=5000)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    event = models.ForeignKey(Event)
    def __unicode__(self):
        return self.author + " " + self.text[:10]
        '''

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length = 100)
    news_text = models.TextField()
    date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    cat = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title  

    def get_absolute_url(self):
        return reverse('detailnews', kwargs = {'pk': self.pk})

class Borderlandspatch(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    cat = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forumpagepatch', kwargs = {'pk': self.pk})

class Discussions(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    field_text = models.TextField()
    date = models.DateTimeField(auto_now = True)
    distop = models.ForeignKey('DiscussionTopic', on_delete = models.CASCADE)

    def __str__(self):
        return self.field_text

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index = True)

    def __str__(self):
        return self.name

class DiscussionTopic(models.Model):
    name = models.CharField(max_length = 150, db_index = True)

    def __str__(self):
        return self.name
    
class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now = True)

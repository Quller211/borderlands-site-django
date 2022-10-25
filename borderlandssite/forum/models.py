from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length = 100)
    news_text = models.TextField()
    date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    cat = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title  

class Borderlandspatch(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    cat = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index = True)

    def __str__(self):
        return self.name
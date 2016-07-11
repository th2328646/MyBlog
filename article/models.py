from django.db import models

# Create your models here.


class User(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.user


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class Comment(models.Model):
    tourist = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    comment = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tourist

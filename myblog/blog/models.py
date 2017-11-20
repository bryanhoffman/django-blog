# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=600)
    post_subtitle = models.CharField(max_length=1000)
    post_pub_date = models.DateTimeField('date published')
    post_author = models.CharField(max_length=100)
    post_text = models.TextField()
    
    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        return self.post_pub_date >= timezone.now() - datetime.timedelta(days=14)

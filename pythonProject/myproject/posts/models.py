from __future__ import unicode_literals

from django.db import models
from rest_framework.reverse import reverse


class Post(models.Model):
    name = models.CharField(max_length=224, null=False, blank=False)
    content = models.TextField(max_length=254, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content

    @staticmethod
    def get_absolute_url():
        return reverse('posts:list-posts', kwargs={})

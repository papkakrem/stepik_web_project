# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):

    def new(self):
        return self.get_queryset().order_by('-id')

    def popular(self):
        return self.get_queryset().order_by('-rating')


class Question(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='q_id_like')

    objects = QuestionManager()

    def __unicode__(self):
        return self.title


class Answer(models.Model):

    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

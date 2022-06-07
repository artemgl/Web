from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name="question_author", on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def get_url(self):
        return '/question/' + str(self.pk)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="answer_author", on_delete=models.CASCADE)

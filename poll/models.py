from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Questions(models.Model):
    q_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')

    def __str__(self):
        return self.q_text

    def was_published_recently(self):
        return self.publication_date >= (timezone.now() - datetime.timedelta(days=1))


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer


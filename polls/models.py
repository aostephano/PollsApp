import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        was_published_in_24_hours = bool
        was_published_in_future = bool
        now = timezone.now()

        was_published_in_24_hours = True if self.pub_date >= now - \
            datetime.timedelta(days=1) else False
        was_published_in_future = True if self.pub_date >= now else False

        return was_published_in_24_hours and not was_published_in_future


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

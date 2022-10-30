from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()


class Rating(models.Model):
    post = models.ForeignKey(Post, related_name='rating',
                             on_delete=models.CASCADE)
    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['post']

    def __str__(self):
        rating_list = {
            '1': self.one,
            '2': self.two,
            '3': self.three,
            '4': self.four,
            '5': self.five
        }
        return str(max(rating_list, key=rating_list.get))

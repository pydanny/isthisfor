import datetime

from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _


class Pitch(models.Model):
    """
        Pitch model
    """

    name = models.CharField(_('Name'), max_length=200)
    email = models.EmailField()
    pitch = models.TextField()
    slug = models.SlugField()
    pub_date = models.DateField(_('Date Published'), default=datetime.date.today)

    def __unicode__(self):
        return u'%s' % self.name

    def total_votes(self):
        return Comment.objects.filter(pitch=self).aggregate(agg_votes=Sum("votes"))["agg_votes"]

    def negative_votes(self):
        return Comment.objects.filter(pitch=self, vote=-1).count()

    def positive_votes(self):
        return Comment.objects.filter(pitch=self, vote=1).count()

    def negative_comments(self):
        return Comment.objects.filter(pitch=self, vote=-1)

    def positive_comments(self):
        return Comment.objects.filter(pitch=self, vote=1)

class CommentManager(models.Manager):
    def user_comments(self, user):
        return self.filter(user=user)


class Comment(models.Model):
    """
    Comments 0..n per Pitch
    """

    VOTE_CHOICES = (
        (-1, "SUCKS!"),
        (0, "No vote"),
        (1, "ROCKS!"),
    )
    comment  = models.TextField(null=True, blank=True)
    user     = models.CharField(max_length=128)
    vote     = models.IntegerField(choices=VOTE_CHOICES, default=0)
    pitch    = models.ForeignKey(Pitch)
    pub_date = models.DateField(default=datetime.date.today)

    objects = CommentManager()

    class Meta:
        ordering = ["pub_date"]


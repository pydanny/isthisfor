import datetime

from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class PitchManager(models.Manager):
    def top_pitches(self):
        #FIXME Use correct number of pitches
        top_ids = [c['pitch_id'] for c in
            Comment.objects.values("pitch_id").aggregate(agg_votes=Sum("votes")).order_by("-agg_votes")[:10]
        ]
        return self.filter(id__in=top_ids)

    def recent_pitches(self):
        self.order_by("pub_date")


class Pitch(models.Model):
    """
        Pitch model
    """

    name = models.CharField(_('Name'), max_length=200)
    email = models.EmailField()
    pitch = models.TextField()
    slug = models.SlugField()
    pub_date = models.DateField(_('Date Published'), default=datetime.date.today)
    related_pitch = models.TextField()
    tc_related_pitches = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        order = ["-pub_date"]

    def total_votes(self):
        return Comment.objects.filter(pitch=self).aggregate(agg_votes=Sum("votes"))["agg_votes"]

    def negative_votes(self):
        return Comment.objects.filter(pitch=self, vote=-1).count()

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

@receiver(pre_save, sender=Pitch)
def pitch_pre_save(sender, instance, *args, **kwargs):
    if instance.name:
        instance.slug = slugify(instance.name)


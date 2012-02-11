import datetime
import json

import requests

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
        pitches = self.filter(id__in=top_ids).in_bulk()
        return map(lambda x: pitches[x], top_ids)

    def recent_pitches(self):
        self.order_by("-pub_date")


class Pitch(models.Model):
    """
        Pitch model
    """

    name = models.CharField(_('Name of your pitch'), max_length=200)
    email = models.EmailField(_("Email"), help_text=_("Where you want the PayPal money during buyout sent!"))
    pitch = models.TextField()
    slug = models.SlugField()
    pub_date = models.DateField(_('Date Published'), default=datetime.date.today)
    related_pitch = models.CharField(_("Related Email"), help_text=_("Provide up to three companies with a similiar concept"), max_length=255, blank=True, null=True)
    related_pitch_1 = models.TextField(blank=True, null=True)
    related_pitch_2 = models.TextField(blank=True, null=True)
    related_pitch_3 = models.TextField(blank=True, null=True)        

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ["-pub_date",]

    def total_votes(self):
        return Comment.objects.filter(pitch=self).aggregate(agg_votes=Sum("vote"))["agg_votes"]

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
        (1, 'ROCKS!'), 
        (0, "Meh"),           
        (-1, "SUCKS!"),
    )
    comment  = models.TextField(null=True, blank=True)
    user     = models.CharField(_("Your name"), max_length=128, help_text="Be an uber-troll and use your real world name!")
    
    vote     = models.IntegerField(choices=VOTE_CHOICES, default=0)
    pitch    = models.ForeignKey(Pitch)
    pub_date = models.DateField(default=datetime.date.today)

    objects = CommentManager()

    class Meta:
        ordering = ["-pub_date"]


@receiver(pre_save, sender=Pitch)
def pitch_pre_save(sender, instance, *args, **kwargs):
    if instance.name:
        instance.slug = slugify(instance.name)

    if instance.related_pitch:
        try:
            pitches = instance.related_pitches.split(",")
        except:
            pass
        else:
            for i, rp in enumerate(pitches[:3]):
                resp = requests.get("http://api.crunchbase.com/v/1/company/{0}.js".format(slugify(rp)))
                try:
                    resp = json.loads(resp.text)
                except:
                    pass
                else:
                    try:
                        setattr(instance, "related_pitch_{0}".format(i + 1), resp['overview'])
                    except:
                        pass 



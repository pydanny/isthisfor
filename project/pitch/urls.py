from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from pitch.models import Pitch

urlpatterns = patterns('pitch.views',
    url(regex=r'^$',
        view=ListView.as_view(
            queryset=Pitch.objects.order_by('-pub_date'),
            context_object_name='latest_pitch_list',
            template_name='pitch/pitch_list.html'),
        name='pitch_list',
    ),
    url(regex=r'^(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(
            model=Pitch,
            template_name='pitch/pitch_detail.html'),
        name='pitch_detail',
    ),
)

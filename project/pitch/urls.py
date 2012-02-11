from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView

from pitch import views

urlpatterns = patterns('pitch.views',
    url(regex=r'^$',
        view=views.PitchDetailView.as_view(),
        name='pitch_list',
    ),
    url(regex=r'^(?P<slug>[-\w]+)/$',
        view=views.PitchListView.as_view(),
        name='pitch_detail',
    ),
)

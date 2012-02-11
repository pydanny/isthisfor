from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView

from pitch import views

urlpatterns = patterns('pitch.views',
    url(regex=r'^$',
        view=views.PitchListView.as_view(),
        name='pitch_list',
    ),
    url(regex=r'^add-pitch/$',
        view=views.PitchAddView.as_view(),
        name='pitch_add',
    ),
    url(regex=r'^(?P<slug>[-\w]+)/$',
        view=views.PitchDetailView.as_view(),
        name='pitch_detail',
    ),
    url(regex=r'^(?P<slug>[-\w]+)/add-comment$',
        view=views.comment_add_form,
        name='comment_add_form',
    ),    

)

from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from pitch.forms import PitchForm, CommentForm
from pitch.models import Pitch

class PitchListView(ListView):    
    queryset=Pitch.objects.order_by('-pub_date')
    context_object_name='latest_pitch_list'
    template_name='pitch/pitch_list.html'
    
class PitchDetailView(DetailView):
    model=Pitch
    template_name='pitch/pitch_detail.html'
    name='pitch_detail'

class PitchAddView(CreateView):
    
    form = PitchForm
    template_name='pitch/pitch_add_form.html'
    model=Pitch    
    
class PitchEditView(UpdateView):

    form = PitchForm
    template_name='pitch/pitch_edit_form.html'
    model=Pitch    
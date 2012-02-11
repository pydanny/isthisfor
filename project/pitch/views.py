from django.core.urlresolvers import reverse
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
    
    def get_success_url(self):
        return reverse('pitch_detail', kwargs={'slug':self.object.slug})
    
    model = Pitch    
    form_class = PitchForm
    template_name='pitch/pitch_add_form.html'
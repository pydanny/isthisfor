from django.views.generic import DetailView, ListView

from pitch.models import Pitch

class PitchDetailView(DetailView):
    
    queryset=Pitch.objects.order_by('-pub_date')
    context_object_name='latest_pitch_list'
    template_name='pitch/pitch_list.html')
    
class PitchListView(ListView):
    

    model=Pitch,
    template_name='pitch/pitch_detail.html')
    name='pitch_detail'
    

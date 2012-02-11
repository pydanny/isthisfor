from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView


from pitch.forms import PitchForm, CommentForm
from pitch.models import Pitch, Comment

class PitchListView(ListView):    
    queryset=Pitch.objects.top_pitches()
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

def comment_add_form(request, slug, template_name="pitch/comment_add_form.html"):
    
    pitch = get_object_or_404(Pitch, slug=slug)
    
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.pitch = pitch
        comment.save()
        return HttpResponseRedirect(reverse('pitch_detail', kwargs={'slug':pitch.slug}))
    
    context = {
        'pitch': pitch,
        'form':form
    }

    return render(request, template_name, context)

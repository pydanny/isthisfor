from django import forms

from pitch.models import Pitch
from pitch.models import Comment

class PitchForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PitchForm, self).__init__(*args, **kwargs)
        self.fields['pitch'].max_length = 90

        
    class Meta:
        
        model = Pitch
        fields = ('name', 'email', 'related_pitch', 'pitch',)
                        
class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ('user','vote', 'comment',)
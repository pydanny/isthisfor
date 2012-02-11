import floppyforms as forms

from pitch.models import Pitch
from pitch.models import Comment

class PitchForm(forms.ModelForm):
    
    class Meta:
        
        model = Pitch
        
class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment        
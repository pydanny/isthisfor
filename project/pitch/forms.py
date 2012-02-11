from django import forms


from pitch.models import Pitch
from pitch.models import Comment

class PitchForm(forms.ModelForm):
        
    class Meta:
        
        model = Pitch
        exclude = ('slug', 'pub_date',)
        
class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ('vote', 'comment',)
        exclude = ('user', 'pitch', 'pub_date')        
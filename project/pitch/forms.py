from django import forms


from pitch.models import Pitch
from pitch.models import Comment

class PitchForm(forms.ModelForm):
        
    class Meta:
        
        model = Pitch
        fields = ('name', 'email', 'related_pitch', 'pitch',)
        exclude = ('slug', 'pub_date', 'tc_related_pitches')
                        
class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ('vote', 'comment',)
        exclude = ('user', 'pitch', 'pub_date')        
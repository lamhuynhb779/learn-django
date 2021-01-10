from django import forms
from .models import Question


# Class extends ModelForm
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)


# Class extends Form
class SendMail (forms.Form):
    title = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    cc = forms.BooleanField(required=False)

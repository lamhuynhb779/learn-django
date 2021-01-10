from django import forms
from .models import Question


# Class extends ModelForm
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question_text",)
        # Add widgets
        widgets = {
            "question_text": forms.TextInput(attrs={"id": "question-text"}),
        }


# Class extends Form
class SendMail (forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "mail-item", "id": "mail-title"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "mail-item"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "mail-item", "id": "mail-content"}))
    cc = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"checked": True, "data-cc": "cc"}))

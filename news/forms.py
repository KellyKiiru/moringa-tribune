from django import forms
from .models import Article

class NewsLetterForm(forms.Form):
    your_name=forms.CharField(max_length=30,label="Your Name")
    email=forms.EmailField(label="Email")
    
class NewArticleForm(forms.ModelForm):
    class Meta:
        model= Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
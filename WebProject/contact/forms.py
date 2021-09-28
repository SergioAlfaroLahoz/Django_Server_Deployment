from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100)
    email = forms.EmailField(label='Email', required=True)
    content = forms.CharField(label='Content', widget=forms.Textarea, required=False)
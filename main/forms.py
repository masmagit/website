from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Your name")
    email = forms.EmailField(label="Your email address")
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        for field in self: 
            field.field.widget.attrs['class'] = 'form-control'
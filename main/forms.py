from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Your name")
    email = forms.EmailField(label="Your email address")
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.assign_attr_valid()  

    def _post_clean(self):
        self.assign_attr_valid()

    def assign_attr_valid(self):
        for field in self:
            field.field.widget.attrs['class'] = 'form-control' if not field.errors else 'form-control is-invalid'
from django import forms
from .models import Content

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


class ContentForm(forms.ModelForm):
   def __init__(self,*args,**kwargs):
      super(ContentForm, self).__init__(*args, **kwargs)
      self.fields['content'].widget.attrs['class'] = 'tiny-class'
   
   class Meta:
      model = Content
      fields = ('page', 'param1', 'param2', 'content')
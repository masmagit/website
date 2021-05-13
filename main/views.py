from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.utils.timezone import localtime
from os import getenv as os_getenv
from .forms import ContactForm
from .utils import recaptcha_validate

def index(request):
    return render(request, "main/index.html")

# Contact form view
def contact(request):
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            ''' reCaptcha validation '''
            recaptcha_response = request.POST.get('grecaptcha-response')
            result = recaptcha_validate(recaptcha_response)           
            if result["success"]:
                body = {
                    "Sender": cform.cleaned_data['name'],
                    "Email": cform.cleaned_data['email'],
                    "Date": str(localtime()),
                    "Subject": cform.cleaned_data['subject'],
                    "Message": cform.cleaned_data['message']
                }
                email_message = "\n".join(': '.join((key,val)) for (key,val) in body.items())
                ses_email = os_getenv("SES_EMAIL")
                send_subject = "WebsiteContact"
                try:
                    send_mail(send_subject, email_message, ses_email, [ses_email])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request, "Thank you for contacting us, your message was successfully sent!")
            else:
                messages.error(request, "reCaptcha response validation failed, please try again.")
            return redirect(reverse("main:contact"))
    else:
        cform = ContactForm()
    
    return render(request, "main/contact.html", {
        "cform" : cform,
        "recaptcha_site_key" : os_getenv("RECAPTCHA_SITE_KEY")
    })
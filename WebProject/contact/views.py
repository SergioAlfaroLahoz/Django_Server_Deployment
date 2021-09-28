from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

from .forms import ContactForm
from .models import Contact

# Create your views here.


def contact(request):
    contact_form = ContactForm()
    if request.method=="POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            email = EmailMessage("Message from Django app", 
                                    "User {} with the direction {} is sending you:\n\n {}".format(name, email, content),
                                    "", 
                                    ["seralfa_9@hotmail.com"],
                                    reply_to=[email]
                                )

            try: 
                email.send()
                return redirect("/contact/?valid")

            except:
                return redirect("contact/?novalid")

    return render(request, "contact/contact.html", {'contact_form': contact_form})

def contact2(request):
    contact_form = ContactForm()
    if request.method=="POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            cName = request.POST.get("name")
            cEmail = request.POST.get("email")
            cContent = request.POST.get("content")

            ct = Contact(name=cName, email=cEmail, date="")
            ct.save()

    return render(request, "contact/contact.html", {'contact_form': contact_form})

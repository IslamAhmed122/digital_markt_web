from django.core import mail
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from app.models import Aboutus, Service, Team, contactus, footer, imagelist, imagelistportfolio,  ourclients, web, whychooseus




from django.conf import settings
# html email required stuff

from django.utils.html import strip_tags


from .forms import CustomerForm
# Create your views here.




def home(request):
    Web= web.objects.last()
    About=Aboutus.objects.last()
    serv=Service.objects.all()
    choo=whychooseus.objects.all()
    webimage=imagelist.objects.all()
    team=Team.objects.all()[:6] 
    client=ourclients.objects.all()[:8]
    foot=footer.objects.last()
    contact=contactus.objects.all()
    image=imagelistportfolio.objects.all()[0:6] 
    form=CustomerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        sendemail(request)
        return redirect("/") 
    else:
        form=CustomerForm()
    
    context = {
        "web":Web,
        "about":About,
        "service":serv,
        "chose":choo,
        "form":form,
        "team":team,
        "client":client,
        "footer":foot,
        "contact":contact,
        "image":image,
        "webimage":webimage

        
    }

    



    return render(request,"index.html",context)

def sendemail(request):
    form=CustomerForm(request.POST or None)
    if request.method == 'POST': 
        name = request.POST['name']
        email = request.POST['email'] 
        subject = request.POST['subject'] 
        message = request.POST['message'] 
    
    subject = subject
    html_message = render_to_string('mail.html', {'name': name})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = email
    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    
    context={
        "form":form,
 
    }

    return render(request,"mail.html",context)
    
        


    
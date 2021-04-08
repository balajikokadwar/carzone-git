from django.shortcuts import render,redirect
from pages.models import Team
from cars.models import car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def home(request):
    teams = Team.objects.all()
    featured_cars = car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = car.objects.order_by('-created_date')
    #search_fields = car.objects.values('model','city','year','body_style')
    model_search = car.objects.values_list('model',flat=True).distinct()
    city_search = car.objects.values_list('city',flat=True).distinct()
    year_search = car.objects.values_list('year',flat=True).distinct()
    body_style_search = car.objects.values_list('body_style',flat=True).distinct()

    data = {
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        #email_subject = "you have new message from carzone website regarding " + subject
       # email_body = "Name: " + name + " Email: " + email + " phone: " + phone + " Message: " + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail("email_subject","email_body","pythononlineclasses1@gmail.com",["balajikokadwar19@gmail.com"])
        messages.success(request,"Thank You for contacting us we will get back to you")
        return redirect('contact')
    return render(request,'pages/contact.html')

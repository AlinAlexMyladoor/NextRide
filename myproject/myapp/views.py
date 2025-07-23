
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Bus, Booking
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def user_login(request):
    form1=LoginForm(request.POST,request.FILES)
    if request.method == 'POST':
        form1 = LoginForm(request.POST, request.FILES)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            password=form1.cleaned_data['password']
            print(username,password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)  
                data=Register.objects.get(username=username)
                if data.is_superuser:
                    data.usertype ='admin'
                    data.save()
                request.session['ut'] = data.usertype
                
                return redirect('home')
            else:
                
                messages.error(request, "Invalid username or password!")
                return redirect('login')
                     
    else:
         form1 = LoginForm()
    
    return render(request, "login.html", {"form": form1})

def register(request):
    if request.method == 'POST':
        form2 = RegisterForm(request.POST, request.FILES)
        if form2.is_valid():
            k = form2.save(commit=False)
            k.usertype = "user"
            # Set password using set_password to ensure hashing and compatibility
            k.set_password(form2.cleaned_data['password'])
            k.save()
            return redirect('login')
    else:
        form2 = RegisterForm()
    return render(request, 'register.html', {'form': form2})


def logout_view(request):
    logout(request)
    return redirect('home')


def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)
            messages.success(request, 'Subscribed successfully!')
        return redirect('subscribe_newsletter')
    return render(request, 'home.html')



def bus_ticket(request):
    buses = []
    travel_date = None

    if request.GET.get('from') and request.GET.get('to') and request.GET.get('date'):
        source = request.GET['from']
        destination = request.GET['to']
        travel_date = request.GET['date']

        buses = Bus.objects.filter(source=source, destination=destination)
        schedules = Schedule.objects.filter(bus__in=buses, travel_date=travel_date)

        bus_info = []
        for schedule in schedules:
            booked_seats = Booking.objects.filter(schedule=schedule).values_list('seat_number', flat=True)
            available_seats = [seat for seat in range(1, schedule.bus.total_seats + 1) if seat not in booked_seats]
            bus_info.append({'schedule': schedule, 'available_seats': available_seats})

        return render(request, 'bus_ticket.html', {
            'bus_info': bus_info,
            'travel_date': travel_date,
        })

    return render(request, 'bus_ticket.html')

@login_required
def book_seat(request):
    if request.method == 'POST':
        schedule_id = request.POST['schedule_id']
        seat_number = int(request.POST['seat_number'])

        schedule = Schedule.objects.get(id=schedule_id)
        existing_booking = Booking.objects.filter(schedule=schedule, seat_number=seat_number)

        if existing_booking.exists():
            messages.error(request, "Seat already booked.")
        else:
            Booking.objects.create(user=request.user, schedule=schedule, seat_number=seat_number)
            messages.success(request, f"Seat {seat_number} booked successfully!")

    return redirect('bus_ticket')




from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User


class Register(AbstractUser):
    usertype=models.CharField(max_length=10,null=True)
    contact = models.CharField(max_length=10, null=True)


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class Bus(models.Model):
    name = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null=True)
    total_seats = models.PositiveIntegerField(default=40, null=True)

    def __str__(self):
        return f"{self.name} ({self.source} → {self.destination})"

class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
    travel_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.bus.name} on {self.travel_date}"

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
    seat_number = models.PositiveIntegerField(null=True)
    booked_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Seat {self.seat_number} - {self.user.username if self.user else 'Unknown'} ({self.schedule})"

    

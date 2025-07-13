from django.db import models
from django.contrib.auth.models import User

class Bus(models.Model):
    operator = models.CharField(max_length=100, null=True)
    origin = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null=True)
    departure_time = models.DateTimeField(null=True)
    seats_available = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.operator}: {self.origin} ➝ {self.destination} at {self.departure_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
    seat_count = models.PositiveIntegerField(null=True)
    booking_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        if self.user:
            username = self.user.username
        else:
            username = "Unknown user"
        return f"{username}'s booking on {self.bus}"
    
class NewRoute(models.Model):
    origin = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null=True)
    distance_km = models.PositiveIntegerField(null=True)
    route_code = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.origin} ➝ {self.destination} ({self.route_code})"
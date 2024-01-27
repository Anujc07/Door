from django.db import models
from django.contrib.auth.models import User


class Detail(models.Model):
    CHOICE = {
        ('Sell', 'Sell'),
        ('Rent', 'Rent'),
    }

    CITY = {
        ('Bhopal', 'Bhopal'),
        ('Indore', 'Indore'),
        ('Jablpur', 'Jablpur'),
        ('Gwalior', 'Gwalior'),
    }
    PROPERY_TYPE = {
        ('SingleRoom', 'SingleRoom'),
        ('Single+Kitchen', 'Single+Kitchen'),
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    }
    
    Listingtype = models.CharField(choices=CHOICE, max_length=50, default='Sell')   #choices=CHOICE
    City = models.CharField(choices=CITY, max_length=10, default='Bhopal')
    Ownername = models.CharField(max_length=25, default=None)
    Email = models.EmailField(blank=True, null=True)
    Address = models.CharField(max_length=60, default="")
    Pincode = models.IntegerField(default=0)
    Contactnumber = models.IntegerField( default=0)
    Image = models.ImageField(upload_to='images/', default='default.jpg', blank=True, null=True)
    Property_id = models.AutoField
    Room_var = models.CharField(choices=PROPERY_TYPE, max_length=20, default=None)
    Price = models.PositiveBigIntegerField(default=0)
    Area = models.PositiveBigIntegerField(default=0)
    Bath_room = models.IntegerField(default=0)
    Room_description = models.TextField(max_length=100, default="")
    Number_of_rooms = models.IntegerField(default=0)
    Propert_age = models.PositiveBigIntegerField(default=0)
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return self.Room_var
    

    
class Booking(models.Model):
    email = models.EmailField(default="example@example.com")  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room_book = models.ForeignKey(Detail, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.user.username} booked Property #{self.room_book.id} on {self.booking_date}"




from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.
class Hotel( models.Model ):
    hotel_name = models.CharField( max_length = 20 )
    country    = models.CharField( max_length = 15 )
    city       = models.CharField( max_length = 15 )
    address    = models.CharField( max_length = 25 )
    hotel_type = models.CharField( max_length = 20 )
    room_type  = models.CharField( max_length = 15 )
    room_num   = models.PositiveIntegerField()
    room_price = models.PositiveIntegerField()

class Flight( models.Model ):
    flight_number = models.CharField( max_length = 5 )
    flight_price  = models.PositiveIntegerField()
    country_from  = models.CharField( max_length = 15 )
    country_to    = models.CharField( max_length = 15 )
    city_from     = models.CharField( max_length = 15 )
    city_to       = models.CharField( max_length = 15 )
    tr_type       = models.CharField( max_length = 1 )
    tr_pos        = models.PositiveIntegerField()
    tr_pos_type   = models.CharField( max_length = 15 )

class Permit( models.Model ):
    departure_date = models.DateTimeField()
    arrival_date   = models.DateTimeField()
    permit_type    = models.CharField( max_length = 15 )
    permit_price   = models.PositiveIntegerField()
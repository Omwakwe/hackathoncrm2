from django.db import models
from django.utils import timezone
from decimal import Decimal


class RoomType(models.Model):
    '''
    model for storing room types
    '''
    type_name = models.CharField(max_length=50)  # paid
    cost_per_night = models.DecimalField(
        max_digits=20, decimal_places=2, default=Decimal('0.00'))
    room_numbers = models.IntegerField()  # maximum number of rooms
    # the following is for auding
    created_by = models.IntegerField(null=True)  # user who created
    created_date = models.DateTimeField(default=timezone.now)
    updated_by = models.IntegerField(default=0)
    updated_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    deleted_by = models.IntegerField(default=0)
    deleted_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.type_name


class Booking(models.Model):
    '''
    model for storing room types
    '''
    room = models.ForeignKey('RoomType',
                             on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    huduma_number = models.CharField(max_length=50)  # huduma number
    gender = models.CharField(max_length=20, blank=True, null=True)
    booking_date = models.DateField()
    checkout_date = models.DateField()
    status = models.IntegerField(default=0)  # 0 not cancelled,1 cancelled
    disabled = models.BooleanField(default=False)
    # the following is for auding
    created_by = models.IntegerField(null=True)  # user who created
    created_date = models.DateTimeField(default=timezone.now)
    updated_by = models.IntegerField(default=0)
    updated_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    deleted_by = models.IntegerField(default=0)
    deleted_on = models.DateTimeField(null=True, blank=True)

    unique_together = ['huduma_number', 'booking_date', 'room']

    def __str__(self):
        return self.huduma_number

    @property
    def real_price(self):
        ''' apply discount if disabled'''
        if self.disabled:
            return self.room.cost_per_night*Decimal(0.4)
        else:
            return self.room.cost_per_night

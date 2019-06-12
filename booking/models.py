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

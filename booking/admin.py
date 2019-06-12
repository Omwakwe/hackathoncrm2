from django.contrib import admin

from booking.models import RoomType


class RoomTypeAdmin(admin.ModelAdmin):
    fields = ('type_name', 'cost_per_night', 'room_numbers')


admin.site.register(RoomType, RoomTypeAdmin)

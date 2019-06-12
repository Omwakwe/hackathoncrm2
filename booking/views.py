from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from booking.forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from booking.models import Booking
from django.db.models import Avg, Count, Min, Sum
from decimal import Decimal


class Home(View):
    '''
    a view for all users even anonymous
    '''
    template_name = 'booking/home.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {})


class BookingView(LoginRequiredMixin, View):
    '''
    a view for booking rooms
    '''
    form_class = BookingForm
    template_name = 'booking/booking.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        responsedata = {}
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print("cant save booking ", e)

            responsedata['success'] = 'yes'
            responsedata['success_msg'] = "Booked room successfully"
        else:
            responsedata['success'] = 'no'
            responsedata['success_msg'] = "Form has errors"
            print('errors ', form.errors)
        return JsonResponse(responsedata)


class ShowBookingView(LoginRequiredMixin, View):
    '''
    a view for showing booked rooms
    '''
    # form_class = BookingForm
    template_name = 'booking/show_booking.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class
        booking = Booking.objects.all()
        return render(request, self.template_name, {'bookings': booking})

    def post(self, request, *args, **kwargs):
        cancelid = request.POST['cancelid']
        print('request.POST ', request.POST)
        responsedata = {}
        if Booking.objects.filter(id=cancelid).exists():
            try:
                booking = Booking.objects.filter(id=cancelid)[0]
                booking.status = 1
                booking.save()
            except Exception as e:
                print("cant cancel booking ", e)

            responsedata['success'] = 'yes'
            responsedata['success_msg'] = "Cancelled room successfully"
        else:
            responsedata['success'] = 'no'
            responsedata['success_msg'] = "Error Cancelling room"
            print('errors ', form.errors)
        return JsonResponse(responsedata)


class BookingReport(LoginRequiredMixin, View):
    '''
    a view for showing booked rooms report
    '''
    # form_class = BookingForm
    template_name = 'booking/report.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class
        booked = Booking.objects.filter().count()
        booked_exec = Booking.objects.filter(room_id=1).count()
        booked_stand = Booking.objects.filter(room_id=2).count()
        booked_economy = Booking.objects.filter(room_id=3).count()
        revenue = 0
        bookings = Booking.objects.filter(deleted=False)
        for booking in bookings:
            cost_is = 0
            if booking.disabled:
                cost_is = booking.room.cost_per_night*Decimal(0.4)
                if booking.status == 0:
                    cost_is = cost_is * Decimal(0.6)
                # revenue = revenue + (booking.room.cost_per_night*Decimal(0.4))
            else:
                cost_is = booking.room.cost_per_night
                if booking.status == 0:
                    cost_is = cost_is * Decimal(0.6)
                # revenue = revenue + booking.room.cost_per_night
            revenue = revenue + cost_is
        return render(request, self.template_name, {'revenue': revenue, 'booked': booked, 'booked_exec': booked_exec, 'booked_stand': booked_stand, 'booked_economy': booked_economy})

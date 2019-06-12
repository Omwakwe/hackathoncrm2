from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from booking.forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from booking.models import Booking


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

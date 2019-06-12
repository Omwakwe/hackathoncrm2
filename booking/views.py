from django.shortcuts import render
from django.views import View


class BookingView(View):
    # form_class = MyForm
    template_name = 'booking/booking.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {})

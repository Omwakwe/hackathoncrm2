from django.urls import path
from .views import BookingView, ShowBookingView

urlpatterns = [
    path('', BookingView.as_view()),
    path('view/', ShowBookingView.as_view()),
]

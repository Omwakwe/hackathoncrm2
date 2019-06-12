from django.urls import path
from .views import BookingView, ShowBookingView, BookingReport

urlpatterns = [
    path('', BookingView.as_view()),
    path('view/', ShowBookingView.as_view()),
    path('report/', BookingReport.as_view()),
]

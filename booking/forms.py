
from django import forms
from booking.models import Booking, RoomType

GENDER_CHOICES = (
    ('', '-----------------------'),
    ('FEMALE', 'Female',),
    ('MALE', 'Male',),
)

DISABILITY_CHOICES = (
    ('', '-----------------------'),
    (0, 'No',),
    (1, 'Yes',),
)


STATUS_CHOICES = (
    ('', '-----------------------'),
    (0, 'Active',),
    (1, 'Cancelled',),
)


class BookingForm(forms.ModelForm):
    '''
    a form for room booking
    '''
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Customer Name', 'class': "form-control input-sm", }))
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': "form-control input-sm", }))
    huduma_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Huduma number', 'class': "form-control input-sm", }))
    booking_date = forms.DateField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Booking date', 'class': "form-control input-sm datepicker2", }))
    checkout_date = forms.DateField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Checkout date', 'class': "form-control input-sm datepicker2", }))
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES, widget=forms.Select(
        attrs={'placeholder': 'gender', 'class': "form-control input-sm", }))
    disabled = forms.ChoiceField(required=True, choices=DISABILITY_CHOICES, widget=forms.Select(
        attrs={'placeholder': 'disability status', 'class': "form-control input-sm", }))
    status = forms.ChoiceField(required=False, choices=DISABILITY_CHOICES, widget=forms.Select(
        attrs={'placeholder': 'disability status', 'class': "form-control input-sm", }))
    room = forms.ModelChoiceField(required=True, empty_label=None, queryset=RoomType.objects.filter(deleted=False), widget=forms.Select(
        attrs={'required': 'required', 'data-placeholder': "", 'class': "form-control input-sm chosen-select", }))

    class Meta:
        model = Booking
        fields = ['gender', 'huduma_number', 'booking_date',
                  'checkout_date', 'disabled', 'status', 'name', 'email', 'room', ]

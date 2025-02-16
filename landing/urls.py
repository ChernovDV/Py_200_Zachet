
from django.urls import path
from landing.view import ContactFormView

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact_form'),
]
from django.urls import path
from .views import submit_response

urlpatterns = [
    path('submit/', submit_response, name='submit_response'),
]

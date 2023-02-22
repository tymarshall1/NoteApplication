from django.urls import path
from .views import *

urlpatterns = [
    
    path('all_notes', all_notes.as_view(), name='all_notes'),
]
from django.urls import path
from .views import form_example_view  

urlpatterns = [
    path('form/', form_example_view, name='form_example'),
]
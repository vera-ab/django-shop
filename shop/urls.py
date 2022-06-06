from django.urls import path

from .views import my_first_view

app_name = 'shop'

urlpatterns = [
    path('', my_first_view)
]
from django.urls import path

from shop.views import MyView, MovieRetrieveUpdateView

app_name = "shop"

urlpatterns = [
    path('', MyView.as_view()),
    path("api/<str:pk>/", MovieRetrieveUpdateView.as_view()),
]

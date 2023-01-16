
from django.urls import path, include
from django.views.static import serve 

urlpatterns = [
    path('', include('myApp.urls')),
]

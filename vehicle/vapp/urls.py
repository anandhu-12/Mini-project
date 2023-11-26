from django.urls import path
from .import views

urlpatterns = [
    path('frontend',views.frontend),
    path('reg',views.register),
    path('del',views.delete),
    path('dat',views.registerdata)
]
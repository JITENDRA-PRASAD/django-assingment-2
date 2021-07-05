from django.urls import path
from . import views


urlpatterns = [
    path("", views.display, name='first'),
    path("allfriend/",views.buddy, name='second'),
    path('<str:Name>',views.F_name),
]




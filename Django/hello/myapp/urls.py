from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.index,name='index'),#veiw ke index vale fun ko run kr
    path("about/",views.about,name='about')
]
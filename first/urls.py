from django.urls import path

from first import views

urlpatterns = [

    path('', views.hi,name="hi"),
path('add', views.add,name="add")

]
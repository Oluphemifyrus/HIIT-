from django.urls import path
from . import views

# write the name of your django application
app_name = 'HiiTApp'

# define the urls to each of your templates here

urlpatterns = [
    path('', views.index, name='index'),
]
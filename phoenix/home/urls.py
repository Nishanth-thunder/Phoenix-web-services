from django.urls import path
from . import views
urlpatterns = [path(route='',view=views.home,name='home'),
               path(route='career/',view=views.career,name='career'),
               path(route='career/success/',view=views.new,name='success')]
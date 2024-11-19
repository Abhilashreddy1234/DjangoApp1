from django.urls import path
from . import views
urlpatterns=[
    path('',views.main,name='main'),
    path('app1/',views.app1,name='app1'),
    path('app1/details/<int:id>',views.details,name='details'),
    ]
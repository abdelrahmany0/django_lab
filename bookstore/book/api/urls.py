from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('book', views.index),
    path('book/<int:id>', views.show),
    path('book/create', views.create),
    path('book/delete/<int:id>', views.delete),
    path('book/update/<int:id>', views.edit),


    path('login', obtain_auth_token),
    path('signup', views.api_signup),

]

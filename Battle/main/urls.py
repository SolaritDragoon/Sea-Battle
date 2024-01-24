from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('prizes', views.prizes, name='prizes'),
    #path('reg', RegisterUser.views, name='registration'),
    path('login', views.login, name='login'),
    path('reg', views.registration, name='registration')
]

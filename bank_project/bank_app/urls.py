from django.urls import path

from bank_app import views

app_name='bank'
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('form/',views.finaltask,name='finaltask'),
path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

]
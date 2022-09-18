from django.urls import path
from webprojectapp import views

urlpatterns = [
    path('', views.main),
    path('home/', views.home, name="homepage"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logut_user),
    path('register/', views.apr_register),
    path('register/apartment/', views.FormApartmentView.register_form, name="register_apartment"),
]
from django.urls import path
from webprojectapp import views

urlpatterns = [
    # Sections.
    path('', views.main),
    path('home/', views.home, name="homepage"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logut_user, name="logout"),
    path('register/apartment/', views.FormApartmentView.register_form, name="register_apartment"),
    path('details_apartment/<int:id>', views.detailsApartment, name="details"),
    # Actions
    path('update/apartment/<int:id>/state/<slug:state>', views.ApartamentActions.updateApartamentState)
]
"""Users urls."""

# Django
from django.urls import path

# Views
from users import views


urlpatterns = [

    path(
        route='login/',
        view=views.login_view,
        name='login'),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'),
    path(
        route='signup/',
        view=views.signup,
        name='signup'),
    path(
        route='me/profile',
        view=views.update_profile,
        name='update_profile'),

]

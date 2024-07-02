from django.urls import path
from .views import create_user, login_user, logout_user

urlpatterns=[
    path("create_user/", create_user, name="create_user"),
    path("login_user/", login_user, name="login_user"),
    path("logout_user/", logout_user, name="logout_user")

]
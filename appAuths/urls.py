from django.urls import path,include
from . import views

urlpatterns=[
    path('register/',views.RegistrationAPIView.as_view()),
    path('login/',views.LoginAPIView.as_view()),
    path('logout/',views.LogoutAPIView.as_view()),
    path('changepassword/',views.ChangePasswordAPIView.as_view()),
    path('userprofile/',views.ManageUserView.as_view()),
]
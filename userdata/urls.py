from django.urls import path
from userdata.views import (
    index,
    signUpView,
    loginView,
    logoutView,
    userProfileView,
    userMessage,
)


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signUpView, name='signup'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('message/', userMessage, name='message'),
    path('<str:link>/', userProfileView, name='userprofile'),
]

"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# from django.contrib.auth import views as auth_view
from .views import Registration,Login,Logout,CreateProfile,Details

urlpatterns = [
            path('registration',Registration.as_view(),name="registration"),
            path('details',Details.as_view(),name="details"),
            path('login',Login.as_view(),name="login"),
            path('createprofile',CreateProfile.as_view(),name="createprofile"),
            path('logout',Logout.as_view(),name="logout"),
]
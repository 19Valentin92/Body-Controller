"""calories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from app import views
from django.contrib import admin
from django.urls import include, path
from app.views import LoginPage, LogOutPage, RegisterPage, bmi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',LoginPage,name='login'),
	path('logout/',LogOutPage,name='logout'),
    path('signup/',RegisterPage,name='signup'),
    path('bmi/', views.bmi, name='bmi'),
    path('calorie/', views.calorie, name='calorie'),
    path('details/',views.detail,name='detail'),
    path('deleteall', views.deleteAll, name='deleteall')
]

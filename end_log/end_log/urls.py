"""end_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login.as_view(),name='login'),
    url(r'^register/', views.register.as_view(),name='register'),
    url(r'^userinfo/', views.UserinfoView.as_view(),name='userinfo'),
    # url(r'^home/', views.home.as_view(),name='home'),
    url(r'^home/', views.home,name='home'),
    url(r'^test/', views.test,name='test'),

]
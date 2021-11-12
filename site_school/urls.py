from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('finance/', include('finance.urls')),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutSite, name="logout"),
    path('', views.home, name="home"),
    path('password_reset/', views.password_reset, name="reset_password"),
    path('',include('pwa.urls')),
]

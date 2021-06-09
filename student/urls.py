from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_student"),
    path('pagos/', views.pagos, name="pagos_student"),
    path('reset_password/', views.reset_password, name="password_student"),
]
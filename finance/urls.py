from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_finance"),
    path('student/', views.estudiantes, name="student_finance"),
    path('student/add/', views.estudiantes_regist, name="studentadd_finance"),
    path('student/next/<int:id_alumno>/', views.student_regist_next, name="studeregist_finance"),
    path('payments/', views.pagos, name="payments_finance"),
    path('report/', views.reporte, name="report_finance"),
    path('reset_password/', views.cambiar_password, name="password_finance"),
    path('payments/add/<int:id_alumno>/', views.pagos_registrar, name="payadd_finance"),
    path('payments/next/<int:id_tramite>/<int:id_pago>/', views.pagos_registro, name="paynext_finance"),
    # path('payments/pdf_download/<int:pk>', views.DownloadPDF.as_view(), name="pdf_download_payments"),
    path('report/add/<int:id_tramite>/', views.cobro_registrar, name="chargeadd_finance"),
    path('payments/detail/<int:id_pago>/', views.pagos_detalle, name="paydetail_finance"),
    path('student/profile/<int:id_alumno>/', views.perfil_alumno, name="profile_student"),
    path('student/payments/<int:id_alumno>/', views.pagos_alumno, name="payments_student"),
    path('student/password_reset/<int:id_alumno>/', views.reset_alumno, name="password_reset_student"),
]
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from core.decorators import unauthenticated_user, allowed_users
from pagos.models import *

@login_required(login_url='login')
@allowed_users(allowed_roles=['alumnos'])
def home(request):
    perfil = request.user.alumno
    pagos = Tramite.objects.filter(clave_alumno=perfil.matricula)
    grupoAcade = Historial_Grupo.objects.filter(clave_alumno=perfil.matricula)
    return render(request,'student/deshboard_student.html',{'perfil':perfil, 'pagos':pagos, 'grupoAcade':grupoAcade})

@login_required(login_url='login')
@allowed_users(allowed_roles=['alumnos'])
def pagos(request):
    perfil = request.user.alumno
    pagos = Tramite.objects.filter(clave_alumno=perfil.matricula)
    return render(request, 'student/pagos.html',{'perfil':perfil, 'pagos':pagos})

@login_required(login_url='login')
@allowed_users(allowed_roles=['alumnos'])
def reset_password(request):
    perfil = request.user.alumno
    user_alumno = User.objects.get(username=perfil.matricula)
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if str(password1) != str(password2):
            messages.info(request, f'Las Contraseñas No Coinciden')
        elif str(password1) == str(password2):
            user_alumno.set_password(password1)
            user_alumno.save()
            messages.success(request, f'Contraseña Modificada')
            return redirect('home_student')

    return render(request, 'student/reset_password.html',{'perfil':perfil})
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

# Create your views here.
from pagos.models import *
from core.decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *


@login_required(login_url='login')
@admin_only
def home(request):
    perfil = request.user.finanza
    return render(request,'finance/dashboard_admin.html',{'perfil':perfil})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def estudiantes(request):
    busqueda = request.GET.get('buscar')
    perfil = request.user.finanza
    students = Alumno.objects.all()
    if busqueda:
        students = Alumno.objects.filter( Q(matricula=busqueda) | Q(nombre=busqueda)).distinct()
    
    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'finance/estudiantes.html',{'perfil':perfil, 'page_obj': page_obj})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def estudiantes_regist(request):
    perfil = request.user.finanza
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='alumnos')
            user.groups.add(group)

            alumnocrear = Alumno.objects.create(matricula=user.username, user=user, nombre=user.first_name, apellido=user.last_name)
            alumnocrear.save()

            messages.success(request, 'Cuenta creada ' + username)
            
            return redirect('studeregist_finance', id_alumno=user.username)
            
    return render(request,'finance/estudiantes_regist.html', {'perfil':perfil,'form':form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def student_regist_next(request, id_alumno):
    perfil = request.user.finanza
    form = AlumnoForm()
    students = Alumno.objects.get(matricula=id_alumno)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=students)
        if form.is_valid():
            form.save()
            messages.success(request, f"Alumno Registrado")
            return redirect('student_finance')
    
    return render(request,'finance/estudiantesnext_regist.html',{'perfil':perfil, 'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def pagos(request):
    busqueda = request.GET.get('buscar')
    perfil = request.user.finanza
    pago = Tramite.objects.all()
    if busqueda:
        pago = Tramite.objects.filter(clave_alumno=busqueda)

    paginator = Paginator(pago, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'finance/pagos.html',{'perfil':perfil, 'page_obj': page_obj})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def reporte(request):
    busqueda = request.GET.get('buscar')
    perfil = request.user.finanza
    pago = Tramite.objects.all()
    if busqueda:
        pago = Tramite.objects.filter(clave_alumno=busqueda)
    
    paginator = Paginator(pago, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'finance/reportes.html',{'perfil':perfil, 'page_obj': page_obj})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def cambiar_password(request):
    perfil = request.user.finanza
    return render(request,'finance/reset_password.html',{'perfil':perfil})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def cobro_registrar(request,id_tramite):
    perfil = request.user.finanza
    tramiteget = Tramite.objects.get(id=id_tramite)
    if request.method == 'POST':
        pago_realizado = request.POST.get('pago_monto')
        
        if tramiteget.monto_adeudo > int(pago_realizado):
            tramiteget.estado = "En Progreso"
            tramiteget.monto_adeudo = tramiteget.monto_adeudo - int(pago_realizado)
            tramiteget.save()
            pagoAgregar = Cobro.objects.create(clave_tramite=tramiteget, monto=pago_realizado)
            pagoAgregar.save()
            messages.success(request, f"Cobro Registrado")
            
            return redirect('report_finance')
        elif tramiteget.monto_adeudo < int(pago_realizado):
            messages.info(request, f'Introduzca correctamente Monto a Pagar')

        else:
            tramiteget.estado = "Completado"
            tramiteget.save()
            pagoAgregar = Cobro.objects.create(clave_tramite=tramiteget, monto=pago_realizado)
            pagoAgregar.save()
            messages.success(request, f"Pago Registrado")
            return redirect('payments_finance')
    
    return render(request,'finance/cobro_registrar.html', {'perfil':perfil, 'tramiteget':tramiteget})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def pagos_registrar(request, id_alumno):
    perfil = request.user.finanza
    students = Alumno.objects.get(matricula=id_alumno)
    tipo_pago = Pago.objects.all()
    if request.method == 'POST':
        idtramite = request.POST.get('pago_tipo')
        pagoParcial = request.POST.get('pago_opcion')
        
        ti_pago = Pago.objects.get(id=idtramite)
        tramiteCrear = Tramite.objects.create(clave_alumno=students, clave_pago=ti_pago, encargado_tramite=perfil, pago_parcial=pagoParcial)
        tramiteCrear.save()
        
        return redirect('paynext_finance', id_tramite=tramiteCrear.id, id_pago=ti_pago.id)
    
    return render(request,'finance/pagos_registrar.html',{'perfil':perfil, 'students':students, 'tipo_pago':tipo_pago})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def pagos_registro(request, id_tramite, id_pago):
    perfil = request.user.finanza
    data_tramite = Tramite.objects.get(id=id_tramite)
    pagoSelect = Pago.objects.get(id=id_pago)
    if request.method == 'POST':
        pago_realizado = request.POST.get('pago_efectivo')
        fecha_plazo = request.POST.get('fecha_plazo')
        if fecha_plazo is not None:
            data_tramite.proximo_pago = fecha_plazo
            data_tramite.estado = "En Progreso"
            data_tramite.monto_adeudo = pagoSelect.monto - int(pago_realizado)
            data_tramite.save()
            pagoAgregar = Cobro.objects.create(clave_tramite=data_tramite, monto=pago_realizado)
            pagoAgregar.save()
            messages.success(request, f"Cobro Registrado")
            return redirect('report_finance') 
        elif int(pago_realizado) == pagoSelect.monto:
            data_tramite.estado = "Completado"
            data_tramite.save()
            pagoAgregar = Cobro.objects.create(clave_tramite=data_tramite, monto=pago_realizado)
            pagoAgregar.save()
            messages.success(request, f"Pago Registrado")
            return redirect('payments_finance')  
        else:
            messages.info(request, f'Introduzca correctamente pago en efectivo')

    return render(request,'finance/pagosnext_registrar.html',{'perfil':perfil,'pagoSelect':pagoSelect, 'data_tramite':data_tramite})

# def render_to_pdf(template_src, context_dict={}):
# 	template = get_template(template_src)
# 	html  = template.render(context_dict)
# 	result = BytesIO()
# 	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
# 	if not pdf.err:
# 		return HttpResponse(result.getvalue(), content_type='application/pdf')
# 	return None

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['finanza'])
# class DownloadPDF(View):
#     model = Tramite
# 	def get(self, request, *args, **kwargs):
# 		pdf = render_to_pdf('finance/pdf_template.html', data)
# 		response = HttpResponse(pdf, content_type='application/pdf')
# 		filename = "Invoice_%s.pdf" %("12341231")
# 		content = "attachment; filename='%s'" %(filename)
# 		response['Content-Disposition'] = content
# 		return response

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def pagos_detalle(request, id_pago):
    perfil = request.user.finanza
    detalle_pago = Tramite.objects.get(id=id_pago)
    return render(request,'finance/pagos_detalle.html',{'perfil':perfil, 'detalle_pago':detalle_pago})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def perfil_alumno(request, id_alumno):
    perfil = request.user.finanza
    alumno_perfil = Alumno.objects.get(matricula=id_alumno)
    pagos = Tramite.objects.filter(clave_alumno=id_alumno)
    grupoAcade = Historial_Grupo.objects.filter(clave_alumno=id_alumno)
    return render(request,'finance/perfil_alumno.html',{'perfil':perfil, 'alumno_perfil':alumno_perfil, 'pagos':pagos, 'grupoAcade':grupoAcade})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def pagos_alumno(request, id_alumno):
    perfil = request.user.finanza
    alumno_perfil = Alumno.objects.get(matricula=id_alumno)
    pagos = Tramite.objects.filter(clave_alumno=id_alumno)
    return render(request,'finance/pagos_alumno.html',{'perfil':perfil, 'alumno_perfil':alumno_perfil, 'pagos':pagos})

@login_required(login_url='login')
@allowed_users(allowed_roles=['finanza'])
def reset_alumno(request, id_alumno):
    perfil = request.user.finanza
    alumno_perfil = Alumno.objects.get(matricula=id_alumno)
    user_alumno = User.objects.get(username=id_alumno)
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if str(password1) != str(password2):
            messages.info(request, f'Las Contraseñas No Coinciden')
        elif str(password1) == str(password2):
            user_alumno.set_password(password1)
            user_alumno.save()
            messages.success(request, f'Contraseña Modificada')
            return redirect('profile_student', id_alumno)

    return render(request,'finance/reset_password_alumno.html',{'perfil':perfil, 'alumno_perfil':alumno_perfil})

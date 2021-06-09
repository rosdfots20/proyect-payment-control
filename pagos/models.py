from django.db import models
from django.contrib.auth.models import User

class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=100)

    def __str__(self):
        return 'Carrera: '+self.nombre_carrera

class Grupo(models.Model):
    PARCIAL = (
			('Cuatrimestre', 'Cuatrimestre'),
			('Semestre', 'Semestre'),
			)
    ciclo = models.CharField(max_length=100)
    grado = models.CharField(max_length=5)
    grupo = models.CharField(max_length=5)
    parcial = models.CharField(max_length=100, choices=PARCIAL)

    def __str__(self):
        return 'Grupo: '+self.grupo+' | Grado: '+self.grado
class Plantel(models.Model):
    ubicacion = models.CharField(max_length=100)
    reactor = models.CharField(max_length=250)

    def __str__(self):
        return 'Plantel: '+self.ubicacion

class Alumno(models.Model):
    ESTATUS = (
			('Activo', 'Activo'),
			('Baja', 'Baja'),
            ('Graduado', 'Graduado'),
			)
    matricula = models.CharField(max_length=100, primary_key=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=100,null=True, blank=True)
    nombre = models.CharField(max_length=100,null=True, blank=True)
    apellido = models.CharField(max_length=150, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=12, null=True, blank=True)
    clave_carrera = models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)
    clave_plantel = models.ForeignKey(Plantel, null=True, blank=True, on_delete=models.CASCADE)
    estatus = models.CharField(max_length=100, choices=ESTATUS, default=ESTATUS[0][0])

    def __str__(self):
        return '{}'.format(self.matricula)

class Historial_Grupo(models.Model):
    clave_alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
    clave_grupo = models.ForeignKey(Grupo, null=True, blank=True, on_delete=models.CASCADE)

class Finanza(models.Model):
    ESTATUS = (
			('Activo', 'Activo'),
			('Inactivo', 'Inactivo'),
			)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    clave_plantel = models.ForeignKey(Plantel, null=True, blank=True, on_delete=models.CASCADE)
    estatus = models.CharField(max_length=100, choices=ESTATUS)

    def __str__(self):
        return self.nombre+' '+self.apellido_paterno

class Pago(models.Model):
    tipo_pago = models.CharField(max_length=200)
    monto = models.IntegerField(null=True)

    def __str__(self):
        return self.tipo_pago+'-$'+str(self.monto)

class Tramite(models.Model):
    ESTADO = (
			('Completado', 'Completado'),
			('En Progreso', 'En Progreso'),
            ('Deuda', 'Deuda'),
			)
    clave_alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
    clave_pago = models.ForeignKey(Pago, null=True, blank=True, on_delete=models.CASCADE)
    fecha_tramitado = models.DateTimeField(auto_now_add=True, null=True)
    encargado_tramite = models.ForeignKey(Finanza, null=True, blank=True, on_delete=models.CASCADE)
    pago_parcial = models.CharField(max_length=100)
    proximo_pago = models.DateField(auto_now_add=False, null=True, blank=True)
    monto_adeudo = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=100, choices=ESTADO)

class Cobro(models.Model):
    clave_tramite = models.ForeignKey(Tramite, null=True, blank=True, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True, null=True)
    monto = models.CharField(max_length=150)


    

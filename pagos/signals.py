# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Group


# from .models import Alumno

# def student_profile(sender, instance, created, **kwargs):
# 	if created:
# 		group = Group.objects.get(name='alumnos')
# 		instance.groups.add(group)
# 		Alumno.objects.create(
# 			user=instance,
# 			nombre=instance.first_name,
# 		)
# 		print('Perfil Creado!')

# post_save.connect(student_profile, sender=User)
from django.db.models import CharField,IntegerField,EmailField,Model

# Create your models here.
class Teacher(Model):
	name=CharField(max_length=30)
	email=EmailField()
	qualification=CharField(max_length=10)
	experience=IntegerField()


class Student(Model):
	name=CharField(max_length=30)
	email=EmailField()
	degree=CharField(max_length=10)
	branch=CharField(max_length=10)
	semester=CharField(max_length=10)


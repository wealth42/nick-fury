from django import forms

from app.models import *

class TeacherForm(forms.ModelForm):
	class Meta:
		model=Teacher
		fields='__all__'


class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields='__all__'

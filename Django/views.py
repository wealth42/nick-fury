from django.shortcuts import render

from app.forms import StudentForm,TeacherForm

from app.models import Student,Teacher

# Create your views here.
def home_view(request):
	return render(request, 'app/home.html')


def student_view(request):
	
	if request.method=='POST':
		sf=StudentForm(request.POST)
		if sf.is_valid():
			sf.save()
			sf=StudentForm()
	else:
		sf=StudentForm()
	
	st_data=Student.objects.all()

	return render(request, 'app/student.html', {'form':sf,'data':st_data})


def teacher_view(request):

	if request.method=='POST':
		tf=TeacherForm(request.POST)
		if tf.is_valid():
			tf.save()
			tf=TeacherForm()
	else:
		tf=TeacherForm()

	th_data=Teacher.objects.all()	

	return render(request, 'app/teacher.html', {'form':tf,'data':th_data})
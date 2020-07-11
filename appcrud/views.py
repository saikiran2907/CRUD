from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/std/view/')
            except:
                pass
    else:
        form = StudentForm()
        return render(request, 'index.html', {'form':form})
def list_user(request):

    return render(request, 'views.html',{'list_user':Student.objects.all()})

def delete_list(request,id):
    list = Student.objects.get(id=id)
    list.delete()
    return redirect('/std/view/')
def update_list(request,id):
    
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None,instance=student)
    if form.is_valid():
        form.save()
        return redirect('/std/view/')
    return render(request, 'index.html', {'form':form,'users':Student.objects.all()})
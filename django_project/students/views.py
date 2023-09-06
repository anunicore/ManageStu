from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm


# Create your views here.
def index(request):
    return render(request, 'student/index.html', {
        'students': Student.objects.all() 
        # the Student.objects.all() it is the value that the variable students takes on, so django has access to this variable name=> give all of the students
    })

def view_student(request, id):
    # student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

# The add funct called as an agrument a request that represent the http request  that the user made to access our web server. There are multiple request: many difference https methods could be use, 
# which means we would like to simply retreive this page the get request method is used for viewing a web page without => send data to this page "POST" method 
# def add(request):
#     # When the route being called the the request method is POST. In Django a Form can either be unbound or bound, these term describe whether or not the form has had the submitted post data 
#     # sent to it for validation an unbound form is instantiated without any agruments with empty parentheses after the name of our form class
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid(): # Django run the data cleaning process in this context cleaning up data means converiting it from string to object
#             new_student_number = form.cleaned_data['student_number']
#             new_first_name = form.cleaned_data['first_name']
#             new_last_name = form.cleaned_data['last_name']
#             new_email = form.cleaned_data['email']
#             new_field_of_study = form.cleaned_data['field_of_study']
#             new_gpa = form.cleaned_data['gpa']
            
#             # Save method to save the student model instance this is done by calling the save method which return s the model instance that was saved
#             new_student = Student(
#                 student_number = new_student_number,
#                 first_name = new_first_name,
#                 last_name = new_last_name,
#                 email = new_email,
#                 field_of_study = new_field_of_study,
#                 gpa = new_gpa
#             )
            
#             # here the save method will atuo create the intanceof our student model and what do we want to return from this function. We want to render a new template called students slash add.html to display student form
#             new_student.save()
#             return render(request, 'student/add.html', 
#             {
#                 'form': StudentForm(),
#                 'success': True # If everything goes fine our student form sent via post was valid and a new student was added to the database we can then use the flag
#                                 # in our template to commnuicate with the user to show them a confirmation message that the new student was success add.
#                                 # And the else case when the request method is not post. We simply create a blank form and render a new template that would displayt our student form
#             })
#         else:
#             form = StudentForm()
#             return render(request, 'student/add.html',
#             {
#                 'form': StudentForm()
#             })

# NEW ADD

def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'student/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'student/add.html', {
    'form': StudentForm()
  })
  
# Edit Modal View
def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'student/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'student/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))
            
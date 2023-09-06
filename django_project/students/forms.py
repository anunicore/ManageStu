from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        labels = {
            'student_number': 'Student number',
            'first_name': 'First Name', 
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study',
            'gpa': 'Personnel GPA'
        }
        # Widget's attribute to solve, it is django's reprenstation of an html input element the widget handles the rendering of the html and the extraciton of data from a "GET" 
        # or "POST" dictionary that coresspon  
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form_control'}),
            'first_name': forms.TextInput(attrs={'class': 'form_control'}),
            'last_name': forms.TextInput(attrs={'class': 'form_control'}),
            'email': forms.EmailInput(attrs={'class': 'form_control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form_control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form_control'}),
        }
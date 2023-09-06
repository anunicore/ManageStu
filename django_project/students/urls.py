from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # the '<int:id>' is a path converter that allows us to create dynamic urls int mathces an integer. Example: slash 5 django puts the integer 5 into the variable id
    path('<int:id>', views.view_student, name='view_student'), 
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
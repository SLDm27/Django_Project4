from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    all_students = Student.objects.order_by(ordering)
    context = {
        'object_list': all_students
    }

    return render(request, template, context)
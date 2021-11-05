from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Project, Galery, Courses, Educations, Skill, MainContent


class IndexView(ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        m = MainContent.objects.all()
        santi = m[0]
        courses = Courses.objects.all()
        educations = Educations.objects.all()
        context = {
            'santi': santi,
            'courses': courses,
            'educations': educations,
        }
        return super().get_context_data(**context)

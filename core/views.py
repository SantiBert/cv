from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from .models import Project, Galery, Courses, Educations, Skill, MainContent


class IndexView(ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        try:
            m = MainContent.objects.all()
            santi = m[0]
            courses = Courses.objects.all()
            educations = Educations.objects.all()
            galery = Galery.objects.filter(destacted=True)
            context = {
                'santi': santi,
                'courses': courses,
                'educations': educations,
                'galery': galery
            }
        except:
            context = {}
        return super().get_context_data(**context)

class GaleryView(View):
    def get(self, request, *args, **kwargs):
        try:
            galery = Galery.objects.all()
            context = {
            "galery":galery,
            }
        except:
            context = {}
        return render(request, 'galery.html', context)
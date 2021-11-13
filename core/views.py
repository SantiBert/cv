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


class GalleryView(View):
    def get(self, request, slug, *args, **kwargs):
        project = Project.objects.get(slug=slug)
        galery = Galery.objects.filter(project=project)
        m = MainContent.objects.all()
        santi = m[0]
        context = {
            "project": project,
            "galery": galery,
            'santi': santi,
        }
        return render(request, 'galery.html', context)


class AllProjectsView(ListView):
    template_name = 'allprojects.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        m = MainContent.objects.all()
        santi = m[0]
        context = {
            'santi': santi,
        }
        return super().get_context_data(**context)

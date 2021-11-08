from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from .models import Project, Galery, Courses, Educations, Skill, MainContent


class IndexView(View):
    def get(self, request, *args, **kwargs):
        m = MainContent.objects.all()
        santi = m[0]
        courses = Courses.objects.all()
        educations = Educations.objects.all()
        galery = Galery.objects.filter(destacted=True)
        try:
            context = {
            "galery":galery,
            'santi': santi,
            'courses': courses,
            'educations': educations,
            }
        except:
            context = {}
        return render(request, 'index.html', context)
    
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
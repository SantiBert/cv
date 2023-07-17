from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View

from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response

from .models import Project, Galery, Courses, Educations, Skill, MainContent
from .serializer import MainContentSerializer, CoursesSerializer, GalerySerializer, EducationsSerializer, SkillSerializer, ProjectSerializer, ProjectSmallSerializer


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


class IndexAPIView(GenericAPIView):
     def get(self, request):
        try:
            santi = MainContent.objects.all().first()
            courses = Courses.objects.all()
            educations = Educations.objects.all()
            projects = Project.objects.filter(is_active=True)
            
            data = {
                'santi': MainContentSerializer(santi).data,
                'courses': CoursesSerializer(courses, many=True).data,
                'educations': EducationsSerializer(educations, many=True).data,
                'projects': ProjectSmallSerializer(projects, many=True).data
            }
            return Response({"data": data}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class AllProjectsAPIView(GenericAPIView):
     def get(self, request):
        try:
            projects = Project.objects.filter(is_active=True)
            serializer = ProjectSerializer(projects,many=True)
            
            return Response({"data": serializer.data}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class ProjectDetailAPIView(GenericAPIView):
     def get(self, request, slug):
        try:
            project = Project.objects.get(slug=slug)
            serializer = ProjectSerializer(project)
            
            return Response({"data": serializer.data}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
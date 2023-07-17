from rest_framework import serializers

from .models import Project, Galery, Courses, Educations, Skill, MainContent, Experience

class MainContentSerializer (serializers.ModelSerializer):
    class Meta:
        model = MainContent
        fields = [
            "id",
            "shorName",
            "fullName",
            "email",
            "nacionalty",
            "phone",
            "address",
            "github",
            "cv"
            ]
        
class SkillSerializer (serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id",
            "name",
            "image",
            "percentage",
            ]
        
class ProjectSerializer (serializers.ModelSerializer):
    skils =  SkillSerializer(many=True)
    
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "image" ,
            "url",
            "skils",
            "repo",
            "is_active"
            ]
        
class ProjectSmallSerializer (serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "image"
            ]
        

class ExperienceSerializer (serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "title",
            "start_at",
            "end_at",
            "description"
            ]

class EducationsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Educations
        fields = [
            "id",
            "title",
            "name",
            "address",
            "startdate",
            "enddate",
            "area",
            "level",
            ]
        
class CoursesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = [
            "id",
            "title",
            "image",
            "url",
            ]
        
class GalerySerializer (serializers.ModelSerializer):
    project =  ProjectSmallSerializer()
    
    class Meta:
        model = Galery
        fields = [
            "id",
            "image",
            "slug",
            "project",
            ]
        
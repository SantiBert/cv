from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField


class MainContent(models.Model):
    id = models.AutoField(primary_key=True)
    shorName = models.CharField(max_length=100)
    fullName = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    nacionalty = models.CharField(max_length=150)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=150, null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    cv = models.FileField(upload_to='cv/', default=None, null=True,
                          blank=True, max_length=150)

    def __str__(self):
        return self.fullName


class Educations(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150, null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    area = models.CharField(max_length=150, null=True, blank=True)
    level = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.title


class Courses (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='porfolio/images/courses')
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    image = models.URLField(max_length=200)
    percentage = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()
    image = models.ImageField(upload_to='porfolio/images/')
    url = models.URLField(null=True, blank=True)
    skils = models.ManyToManyField(Skill, null=True, blank=True)
    repo = models.URLField(null=True, blank=True)
    show_in_index = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Galery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(
        upload_to='porfolio/galery/', null=True, blank=True)
    slug = AutoSlugField(populate_from='id', default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.project.title + str(self.created_date))


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    start_at = models.DateField(default=timezone.now)
    end_at = models.DateField(default=timezone.now)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.project.title + str(self.created_date))

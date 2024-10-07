from django.db import models

# Create your models here.
class UserModel(models.Model):
    user_name = models.CharField(max_length=200)
    user_mobile = models.CharField(max_length=20)
    user_email = models.CharField(max_length=200)
    user_password = models.CharField(max_length=50)

class ContactDetailsModel(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/')
    linkedin_link = models.TextField()

class EducationDetailsModel(models.Model):
    course = models.CharField(max_length=300)
    university = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    year = models.DateField(null=True)

class ExperianceModel(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    job_details = models.CharField(max_length=200)
    

class SkillModel(models.Model):
    skill = models.CharField(max_length=200,null=True)

class objetiveModel(models.Model):
    title = models.CharField(max_length=200,null=True)
    about = models.TextField()

class languageModel(models.Model):
    language = models.CharField(max_length=200)

class ProjectModel(models.Model):
    project_name = models.CharField(max_length=200)
    project_start = models.DateField()
    project_end = models.DateField()
    project_decription = models.TextField()

class CertificationModel(models.Model):
    Certificate_name = models.CharField(max_length=300)
    cer_address = models.TextField(null=True)
    certicicate_date = models.DateField()



from django.shortcuts import redirect, render
from django.http import HttpResponse



from .models import UserModel,ContactDetailsModel,EducationDetailsModel,objetiveModel,ProjectModel,CertificationModel,SkillModel,languageModel,ExperianceModel
# Create your views here.
def login(req):
    return render(req,"login.html")

def register(req):
    return render(req,"register.html")


def save_user(req):
    print(req.POST)
    newuser = UserModel(
        user_name=req.POST['uname'],
        user_mobile=req.POST['umobile'],
        user_email=req.POST['uemail'],
        user_password=req.POST['upassword'],

    )
    newuser.save()
    return redirect("/")


def dologin(req):
    
    userdet = UserModel.objects.filter(
                                        user_email=req.POST['uemail'],
                                        user_password=req.POST['upassword']
                                     )
    if(len(userdet)>0):
        req.session['user_id']=userdet[0].id
        return redirect("/home")
    else:
        return HttpResponse("<script>alert('login faild');history.back();</script>")


def home(req):
    if(req.session.has_key('user_id')):
        return render(req,"home.html")
    else:
         return redirect("/")

def profile(req):
    return render(req,"profile.html")

def resumetemplate(req):
    return render(req,"resumetemplate.html")



def save_contactDetails(req):
    contact_details = ContactDetailsModel()
    contact_details.name = req.POST['name']
    contact_details.mobile = req.POST['mobile']
    contact_details.email = req.POST['email']
    contact_details.address = req.POST['address']
    contact_details.image = req.FILES['image']
    contact_details.linkedin_link = req.POST['linkedin_link']
    contact_details.save()
    print(req.POST)
    return render(req,"profile.html")
    
def save_education(req):
    education_details = EducationDetailsModel()
    education_details.course = req.POST['course']
    education_details.university = req.POST['university']
    education_details.grade = req.POST['grade']
    education_details.year = req.POST['year']
    education_details.save()
    print(req.POST)
    return render(req,"profile.html")






def save_objective(req):
    objective_details =  objetiveModel()
    objective_details.title = req.POST['title']
    objective_details.about = req.POST['about']
    objective_details.save()
    print(req.POST)
    return render(req,"profile.html")


def save_project(req):
    project_details =  ProjectModel()
    project_details.project_name =  req.POST['project_name']
    project_details.project_start =  req.POST['project_start']
    project_details.project_end =  req.POST['project_end']
    project_details.project_decription =  req.POST['project_decription']
    project_details.save()
    print(req.POST)
    return render(req,"profile.html")


def save_course(req):
    course_details = CertificationModel()
    course_details.Certificate_name = req.POST['Certificate_name']
    course_details.cer_address = req.POST['cer_address']
    course_details.certicicate_date = req.POST['certicicate_date']
    course_details.save()
    print(req.POST)
    return render(req,"profile.html")

def save_skill(req):
    techonolgy = SkillModel()
    techonolgy.skill = req.POST['skill']
    techonolgy.save()
    print(req.POST)
    return render(req,"profile.html")

def save_langauge(req):
    language_know = languageModel()
    language_know.language = req.POST['language']
    language_know.save()
    print(req.POST)
    return render(req, "profile.html")

def save_experience(req):
    experinece_details = ExperianceModel()
    experinece_details.job_title = req.POST['job_title']
    experinece_details.company_name = req.POST['company_name']
    experinece_details.start_date = req.POST['start_date']
    experinece_details.end_date = req.POST['end_date']
    experinece_details.job_details = req.POST['job_details']
    experinece_details.save()
    print(req.POST)
    return render(req, "profile.html")

def resume1(req):
    data=ContactDetailsModel.objects.all()
    educationData = EducationDetailsModel.objects.all()
    aboutdata = objetiveModel.objects.all()
    projectdata = ProjectModel.objects.all()
    coursedata = CertificationModel.objects.all()
    skilldata = SkillModel.objects.all()
    languagedata = languageModel.objects.all()
    experiancedata = ExperianceModel.objects.all()
    obj={'data':data, 'educationData':educationData, 'aboutdata':aboutdata, 'projectdata':projectdata, 'coursedata':coursedata, 'skilldata':skilldata, 'languagedata':languagedata, 'experiancedata':experiancedata }
    
    return render(req,"resume1.html",obj)



def resume2(req):
    data=ContactDetailsModel.objects.all()
    educationData = EducationDetailsModel.objects.all()
    aboutdata = objetiveModel.objects.all()
    projectdata = ProjectModel.objects.all()
    coursedata = CertificationModel.objects.all()
    skilldata = SkillModel.objects.all()
    languagedata = languageModel.objects.all()
    experiancedata = ExperianceModel.objects.all()
    obj={'data':data, 'educationData':educationData, 'aboutdata':aboutdata, 'projectdata':projectdata, 'coursedata':coursedata, 'skilldata':skilldata,'languagedata':languagedata, 'experiancedata':experiancedata}
    
    return render(req,"resume2.html",obj)

def delete_skill(req):
    SkillModel.objects.get(id=req.GET['id']).delete()
    return render(req,"profile.html")

def delete_langauge(req):
    languageModel.objects.get(id=req.GET['id']).delete()
    return render(req,"profile.html")


def delete_education(req):
    EducationDetailsModel.objects.get(id=req.GET['id']).delete()
    return render(req,"profile.html")

def delete_course(req):
    CertificationModel.objects.get(id=req.GET['id']).delete()
    return render(req,"profile.html")
    
def delete_project(req):
    ProjectModel.objects.get(id=req.GET['id']).delete()
    return render(req,"profile.html")

def delete_contact(req):
    ContactDetailsModel.objects.get(id=req.GET['id']).delete()
    return render(req,"profile.html")

def delete_experiance(req):
    ExperianceModel.objects.get(id=req.GET['id']).delete()
    return render(req,"profile.html")

def delete_about(req):
    objetiveModel.objects.get(id=req.GET['id']).delete()
    return render(req,"profile.html")


def allresume(req):
    data=ContactDetailsModel.objects.all()
    educationData = EducationDetailsModel.objects.all()
    aboutdata = objetiveModel.objects.all()
    projectdata = ProjectModel.objects.all()
    coursedata = CertificationModel.objects.all()
    skilldata = SkillModel.objects.all()
    languagedata = languageModel.objects.all()
    experiancedata = ExperianceModel.objects.all()
    obj={'data':data, 'educationData':educationData, 'aboutdata':aboutdata, 'projectdata':projectdata, 'coursedata':coursedata, 'skilldata':skilldata, 'languagedata':languagedata, 'experiancedata':experiancedata}
    
    return render(req,"allresume.html", obj)











    


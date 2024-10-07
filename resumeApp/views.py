from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import UserModel,ContactDetailsModel,EducationDetailsModel,SkillModel,objetiveModel,ProjectModel,CertificationModel
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
    course_details.certicicate_date = req.POST['certicicate_date']
    course_details.cer_address = req.POST['cer_address']
    course_details.save()
    print(req.POST)
    return render(req,"profile.html")

def dropdown_view(request):
    statuses = SkillModel.objects.all()
    if request.method == 'POST':
        selected_status = request.POST.get('status')

        # Process the selected option (e.g., save it or use it in logic)
        return HttpResponse(f"Selected Status: {selected_status}")

    return render(request, 'profile.html', {'statuses': statuses})



def resume1(req):
    data=ContactDetailsModel.objects.all()
    educationData = EducationDetailsModel.objects.all()
    aboutdata = objetiveModel.objects.all()
    projectdata = ProjectModel.objects.all()
    coursedata = CertificationModel.objects.all()
    obj={'data':data, 'educationData':educationData, 'aboutdata':aboutdata, 'projectdata':projectdata, 'coursedata':coursedata}
    
    return render(req,"resume1.html",obj)


    


    

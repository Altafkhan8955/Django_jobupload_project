from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import*
from random import randint


# Create your views here.

def button(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        en = contactform.objects.create(username=username, password=password)
        en.save

    
    return render(request,"button.html")



def index(request):
    return render (request,"index.html")

def signup(request):
    if request.POST.get('role') == "Candidate":
        role = request.POST.get('role')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render(request,"signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                canduser = Candidate.objects.create(User_id=newuser,firstname=firstname,lastname=lastname)
                return render(request,"Otpverify.html",{'email':email})
           
    else:
         if request.POST.get('role') == "Company":
            role = request.POST.get('role')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')

            user = UserMaster.objects.filter(email=email)
            if user:
                message == "User already Exist"
                return render(request,"signup.html",{'msg':message})
            else:
                if password == cpassword:
                    otp = randint(100000,999999)
                    newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    compuser = Company.objects.create(Com_id=newuser,firstname=firstname,lastname=lastname)
                    return render(request,"Otpverify.html",{'email':email})
    return render(request,"signup.html")

def Otpverify(request):
    email = request.POST.get('email')
    otp = request.POST.get('otp')

    user = UserMaster.objects.filter(email=email)

    if user:
        if otp == otp:
            message = "Otp verify successfull"
            return render(request,"login.html",{'msg':message})
        else:
            message = "Otp is incorrect"
            return render(request,"Otpverify.html",{'msg':message})
    else:
        return render(request,"signup.html")

def login(request):
    if request.POST.get('role') == "Candidate":
        email = request.POST['email']
        password = request.POST['password']

        user= UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="Candidate":
                can = Candidate.objects.get(User_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return render(request,"index.html")
            else:
                message = "Password does not match"
                return render(request,"login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"login.html")
    else:
        if request.POST.get('role') == "Company":
            email = request.POST['email']
            password = request.POST['password']
            
            user= UserMaster.objects.get(email=email)
            if user:
                if user.password==password and user.role=="Company":
                    com = Company.objects.get(Com_id=user)
                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['firstname'] = com.firstname
                    request.session['lastname'] = com.lastname
                    request.session['email'] = user.email
                    request.session['password'] = user.password
                    return render(request,"company/index2.html")
                else:
                    message = "Password does not match"
                    return render(request,"login.html",{'msg':message})
            else:
                message = "User does not exist"
                return render(request,"login.html")
        
    return render(request,"login.html")

#def profile(request,pk):
    #user = UserMaster.objects.get(pk=pk)
    #can = Candidate.objects.get(User_id=user)
    #return render(request,"profile.html",{'user':user,'can':can})

def profile(reguest,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(User_id=user)
        can.birthday = reguest.POST.get('birthday')
        can.gender = reguest.POST.get('gender')
        can.phone = reguest.POST.get('phone')
        can.state = reguest.POST.get('state')
        can.city = reguest.POST.get('city')
        can.address = reguest.POST.get('address')
        can.highestdu = reguest.POST.get('highestdu')
        can.job_type = reguest.POST.get('job_type')
        can.jobcategory = reguest.POST.get('jobcategory')
        can.save()
        return render(reguest,"profile.html",{'user':user,'can':can, })
        #url = f'/profile/{pk}' # URL formatting
        #return redirect(url)

def candidatelogout(request):
    del request.session['email']
    del request.session['password']
    return render(request,"login.html")

def condidatejob(request):
    all_job = jobDetails.objects.all()
    return render(request,"joblistpage.html",{'all_job':all_job})

def jobApplypage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user:
        cand = Candidate.objects.get(User_id=user)
    return render(request,"jobApplypage.html",{'user':user,'cand':cand})

def jobApply(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user:
        cand = Candidate.objects.get(User_id=user)
        contact = request.POST['contact']
        jobtype = request.POST['jobtype']
        education = request.POST['education']
        website = request.POST['website']
        min_salary = request.POST['min_salary']
        mix_salary = request.POST['mix_salary']
        resume = request.FILES['resume']
        
        newapply= ApplyList.objects.create(candidate=cand,contact=contact,jobtype=jobtype,education=education,
        website=website,min_salary=min_salary,mix_salary=mix_salary,resume=resume)
        message = "Job Apply successfully"
        return render(request,"jobApplypage.html",{'msg':message})
      

    return render(request,"jobApplypage.html")


#################################company Views########################

def index2(request):
    return render(request,"company/index2.html",)

def update(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        com = Company.objects.get(Com_id=user)
        com.company_name = request.POST.get('company_name')
        com.state = request.POST.get('state')
        com.city  = request.POST.get('city ')
        com.phone = request.POST.get('phone')
        com.address = request.POST.get('address')
        com.logo_pic = request.FILES.get('logo_pic')
        com.save()
        #return render(request,"company/index2.html")
    return render(request,"company/update.html",{'user':user, 'com':com})

def jobdetail(request):
    if request.method == 'POST':
        jonname = request.POST.get('jonname')
        companyname = request.POST.get('companyname')
        companyaddress = request.POST.get('companyaddress')
        jobdescription = request.POST.get('jobdescription')
        qualification = request.POST.get('qualification')
        resposibilities = request.POST.get('resposibilities')
        location = request.POST.get('location')
        companywebsite = request.POST.get('companywebsite')
        email = request.POST.get('companyemail')
        companycontact = request.POST.get('companycontact')
        salarypackage = request.POST.get('salarypackage')
        experience = request.POST.get('experience')
        logo_pic = request.FILES.get('logo_pic')
        newjob = jobDetails.objects.create(jonname=jonname,companyname=companyname,companyaddress=companyaddress,
        jobdescription=jobdescription,qualification=qualification,resposibilities=resposibilities,location=location,
        companywebsite=companywebsite,companyemail=email,companycontact=companycontact,salarypackage =salarypackage ,
        experience=experience,logo_pic=logo_pic)
        message = "job Post Successfully"
        return render(request,"company/jobdetail.html")
    return render(request,"company/jobdetail.html")

def companylogout(request):
    del request.session['email']
    del request.session['password']
    return render(request,"login.html")

def joblistpage(request):
    all_job = jobDetails.objects.all()
    return render(request,"company/joblist.html",{'alljob':all_job})

def Applylist(request):
    jobapply = ApplyList.objects.all()
    return render(request,"company/Applylist.html",{'jobapply':jobapply})

##########################Admin side###########################
def adminindex(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"admin/adminindex2.html")
    else:
        return redirect('adminlogin')

def adminlogin(request):
    return render(request,"admin/adminlogin.html")

def adminpage(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == 'admin' and password == 'admin':
        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminindex')
    else:
        message = "Username and Password wrong"
        return render(request,"admin/adminlogin.html",{'msg':message})

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('adminlogin')

def userList(request):
    conuser = UserMaster.objects.filter(role='Candidate')
    return render(request,"admin/userList.html",{'conuser':conuser})

def companylist(request):
    comuser = UserMaster.objects.filter(role='Company')
    return render(request,"admin/companylist.html",{'comuser':comuser})

def userDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect(userList)

def Verifycompany(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render(request,"admin/verify.html",{'company':company})

def Verifypage(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified = request.POST.get('verify')
        company.save()
        return redirect(companylist)

def companyDelete(request,pk):
    company = UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect(userList)
    
    

   
   
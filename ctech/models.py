from django.db import models

# Create your models here.

class contactform(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class Company(models.Model):
    Com_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    logo_pic = models.ImageField(upload_to="ctech/img/company")

class Candidate(models.Model):
    User_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    birthday = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    job_type = models.CharField(max_length=150)
    jobcategory = models.CharField(max_length=150)
    highestdu = models.CharField(max_length=150)

class jobDetails(models.Model):
    jonname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250)
    jobdescription = models.CharField(max_length=250)
    qualification = models.CharField(max_length=250)
    resposibilities = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    companywebsite = models.CharField(max_length=250)
    companyemail = models.EmailField(max_length=50)
    companycontact = models.CharField(max_length=50)
    salarypackage = models.CharField(max_length=20)
    experience = models.IntegerField()
    logo_pic = models.ImageField(upload_to="ctech/img/company")

class ApplyList(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    jobtype = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    min_salary = models.CharField(max_length=50)
    mix_salary = models.CharField(max_length=50)
    resume = models.FileField(upload_to="templates/resume")

   
   



    
        
    
      
        


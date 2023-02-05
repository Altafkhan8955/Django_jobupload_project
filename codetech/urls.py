"""codetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ctech import views

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('button',views.button),
    path("index",views.index),
    path('signup',views.signup,name="signup"),
    path('Otpverify',views.Otpverify,name="Otpverify"),
    path('login',views.login,name="login"),
    path("profile/<int:pk>",views.profile,name="profile"),
    path("candidatelogout",views.candidatelogout,name="candidatelogout"),
    path("condidatejob",views.condidatejob,name="condidatejob"),
    path("jobApplypage/<int:pk>",views.jobApplypage,name="jobApplypage"),
    path("jobApply/<int:pk>",views.jobApply,name="jobApply"),

    ###################URL company######################
    path("index2",views.index2,name='index2'),
    path("update/<int:pk>",views.update,name='update'),
    path("jobdetail/",views.jobdetail,name="jobdetail"),
    path("companylogout",views.companylogout,name="companylogout"),
    path("joblistpage",views.joblistpage,name="joblistpage"),
    path("Applylist",views.Applylist,name="Applylist"),

    #######################Admin side#################
    path("adminindex",views.adminindex,name="adminindex"), 
    path("adminlogin",views.adminlogin,name="adminlogin"),
    path("adminpage",views.adminpage,name="adminpage"),
    path("adminlogout",views.adminlogout,name="adminlogout"),
    path("userList",views.userList,name="userList"),
    path("companylist",views.companylist,name="companylist"),
    path("userDelete/<int:pk>",views.userDelete,name="userDelete"),
    path("Verifycompany/<int:pk>",views.Verifycompany,name="Verifycompany"),
    path("Verifypage/<int:pk>",views.Verifypage,name="Verifypage"),
    path("companyDelete/<int:pk>",views.companyDelete,name="companyDelete")
  
]

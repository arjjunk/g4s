"""g4s URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from g4security import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index1),
    path('login/',views.login),
    path('log/',views.log),
    path('contact/',views.contact),
    path('about/',views.about),
    path('insert/',views.insert),
    path('details/',views.details),
    path('admission/',views.admission),
    path('adminheader/',views.adminheader),
    path('applicant/',views.applicant),
    path('client/',views.client),
    path('public/',views.public),
    path('manager/',views.manager),
    path('employee/',views.employee),
    path('adminheader1/',views.adminheader1),
    path('applicant1/',views.applicant1),
    path('client1/',views.client1),
    path('manager1/',views.manager1),
    path('employee1/',views.employee1),
    path('addjobmaster/',views.addjobmaster),
    path('vaccancy/',views.vaccancy),
    path('jobapplication/<str:id>',views.jobapplication),
    path('complaint/',views.complaint),
    path('login/',views.login),
    path('clientregistration/',views.clientregistration),
    path('feedback/<str:id>',views.feedback),
    path('leaveapplication/',views.leaveapplication),
    path('loanapplication/',views.loanapplication),
    path('jobmaster/',views.jobmaster),
    path('addvacancy/',views.addvacancy),
    path('givecomplaint/',views.givecomplaint),
    path('givefeedback/',views.givefeedback),
    path('addclient/',views.addclient),
    path('application/',views.application),
    path('applyleave/',views.applyleave),
    path('removejobmaster/',views.removejobmaster),
    path('changejobmaster/',views.changejobmaster),
    path('removejobmaster1/<int:id>',views.removejobmaster1),
    path('verifyclient/',views.verifyclient),
    path('applyloan/',views.applyloan),
    path('changejob/<int:id>',views.changejob),
    path('updatejob/<int:id>',views.updatejob),
    path('viewapplication/<str:id>',views.viewapplication),
    path('viewjob/',views.viewjob),
    path('generaterequest/<int:id>',views.generaterequest),
    path('addrequest/',views.addrequest),
    path('acceptclient/<int:id>',views.acceptclient),
    path('rejectclient/<int:id>',views.rejectclient),
    path('viewfeedback/',views.viewfeedback),
    path('feedbackview/<str:id>',views.feedbackview),
    path('viewservices/',views.viewservices),
    path('viewvacancy/<str:id>',views.viewvacancy),
    path('viewjobmaster/',views.viewjobmaster),
    path('viewvacancy1/<str:id>',views.viewvacancy1),
    path('jobmaster1/',views.jobmaster1),
    path('vacancy1/',views.vacancy1),
    path('interviewlist/<int:id>',views.interviewlist),
    path('addinterview/',views.addinterview),
    path('viewinterview/',views.viewinterview),
    path('selectionlist/<str:id>',views.selectionlist),
    path('addselection/',views.addselection),
    path('viewselectionlist/',views.viewselectionlist),
    path('appoint/<str:id>',views.appoint),
    path('addemployee/<int:id>',views.addemployee),
    path('viewrequest/<str:id>',views.viewrequest),
    path('viewclient/',views.viewclient),
    path('adminlogout/',views.adminlogout),
     path('applicantlogout/',views.applicantlogout),
    path('vacancydetails/<str:id>',views.vacancydetails),
    path('applicantdetails/<str:id>',views.applicantdetails),
    path('applicantdetails1/<str:id>',views.applicantdetails1),
    path('searchemployee/',views.searchemployee),
    path('searchemployee1/<str:id>',views.searchemployee1),
    path('searchemployee2/<str:id>',views.searchemployee2),
    path('applicationstatus/',views.applicationstatus),
    path('interviewstatus/',views.interviewstatus),
    path('selectionstatus/',views.selectionstatus),
    path('clientlogout/',views.clientlogout),
    path('feedback1/',views.feedback1),
    path('employeelogout/',views.employeelogout),
    path('allotmanager/',views.allotmanager),
    path('allotmanager1/<str:id>',views.allotmanager1),
    path('allotmanager2/<str:id>',views.allotmanager2),
    path('managerlogout/',views.managerlogout),
    path('leaveprocess/',views.leaveprocess),
    path('loanprocess/',views.loanprocess),
    path('salarystatement/',views.salarystatement),
    path('leaveprocess1/<int:id>',views.leaveprocess1),
    path('loanprocess1/<int:id>',views.loanprocess1),
    path('loanprocess2/<int:id>',views.loanprocess2),
    path('salarystatement1/<str:id>',views.salarystatement1),
    path('salarystatement2/',views.salarystatement2),
    path('acceptrequest/<int:id>',views.acceptrequest),
    path('allotemployee/',views.allotemployee),
    path('updaterequest/<str:id>',views.updaterequest),
    path('updaterequest1/<int:id>',views.updaterequest1),
    path('viewallotment/',views.viewallotment),
    path('viewallotment1/<str:id>',views.viewallotment1),
    path('viewallotment2/<str:id>',views.viewallotment2),
    path('leaveapplicationstatus/',views.leaveapplicationstatus),
    path('loanapplicationstatus/',views.loanapplicationstatus),
    path('salary/',views.salary),
    path('viewresume/<int:id>',views.viewresume),




    
]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

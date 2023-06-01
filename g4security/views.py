from django.shortcuts import render,redirect,HttpResponse
import datetime
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail

from g4security.models import tbl_application,tbl_client_employee,tbl_client,tbl_salary_statement, tbl_client_request, tbl_complaint, tbl_employee, tbl_feedback, tbl_interview_list, tbl_job_master, tbl_leave, tbl_loan, tbl_login, tbl_selection_list, tbl_vacancy
def index1(request):
    return render(request,"work.html")

def login(request):
    return render(request,"login.html")
def adminlogout(request):
    del request.session['admin']
    return render(request,"login.html") 
def applicantlogout(request):
    del request.session['applicant']
    return render(request,"login.html")    
def clientlogout(request):
    del request.session['client']
    return render(request,"login.html")   
def employeelogout(request):
    del request.session['employee']
    return render(request,"login.html")   
def managerlogout(request):
    del request.session['manager']
    return render(request,"login.html")             


def log(request):
    if request.method == "POST":
        data = tbl_login.objects.all()
        user = request.POST.get("user")
        pwd = request.POST.get("pswd")
        flag=0
        for da in data:
            if user == da.userid and pwd == da.password:
                type=da.category
                flag = 1
                if type=="admin":
                    request.session['admin']=user
                    return redirect('/adminheader1')   
                elif type=="manager":
                    request.session['manager']=user
                    return redirect('/manager1')  
                elif type=="employee":
                    request.session['employee']=user
                    return redirect('/employee1')
                elif type=="public":
                    request.session['public']=user
                    return redirect('/public') 
                elif type=="applicant":
                    request.session['applicant']=user
                    return redirect('/applicant1') 
                elif type=="client":
                    request.session['client']=user
                    return redirect('/client1') 
                else:
                    return render(request,"error.html")
    if flag==0:
        return render(request,"error.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")  

def insert(request):
    if request.method=='POST':
        email=request.POST.get('s1')
        p=request.POST.get('s2')
    return render(request,"view.html",{'e1':email,'e2':p})

def details(request):
    if request.method=='POST':
        sid=request.POST.get('id')
        sname=request.POST.get('name')
        sage=request.POST.get('age')
    return render(request,"view.html",{'i':sid,'n':sname,'a':sage})   
 
def admission(request):
    if request.method=='POST':
        admissionnumber=request.POST.get('id')
        studentname=request.POST.get('s_name')

    return render(request,"view.html",{'ad':admissionnumber,'sn':studentname})
def adminheader(request):
    return render(request,"adminheader.html")      
def applicant(request):
    return render(request,"applicant.html")  
def client(request):
    return render(request,"client.html")   

def public(request):
    return render(request,"index.html")

def manager(request):
    return render(request,"manager.html") 

def employee(request):
    return render(request,"employee.html")
def adminheader1(request):
    return render(request,"adminheader1.html")      
def applicant1(request):
    return render(request,"applicant1.html")  
def client1(request):
    return render(request,"client1.html")   
def manager1(request):
    return render(request,"manager1.html") 

def employee1(request):
    return render(request,"employee1.html")
def addjobmaster(request):
    return render(request,"addjobmaster.html")      
    
def vaccancy(request):
    data=tbl_job_master.objects.all()
    return render(request,"vaccancy.html",{'data1':data})      
    
def jobapplication(request,id):
    return render(request,"jobapplication.html",{'data':id})

def complaint(request):
    uid=request.session['employee']
    return render(request,"complaint.html",{'id':uid})

def login(request):
    return render(request,"login.html")

def clientregistration(request):
    return render(request,"clientregistration.html")

def feedback(request,id):
    return render(request,"feedback.html",{'id':id})       
              
def leaveapplication(request):
    uid=request.session['employee']
    data=tbl_employee.objects.get(employee_id=uid)
    data1=tbl_vacancy.objects.get(name=data.vacancyname)
    data3=tbl_job_master.objects.get(job_id=data1.job_id)
    print(data3.job_name)
    return render(request,"leaveapplication.html",{'id':uid,'data3':data3})  

def loanapplication(request):
    uid=request.session['employee']
    return render(request,"loanapplication.html",{'id':uid})      
def jobmaster(request):
    if request.method == 'POST':
        data = tbl_job_master()
        data.job_id="na"
        data.job_name=request.POST.get('jobname')
        data.qualification=request.POST.get('qualification')
        data.experience=request.POST.get('experience')
        data.basic_sal=request.POST.get('basicsalary')
        b=int(request.POST.get('basicsalary'))
        ta=b*15/100
        da=b*80/100
        hra=b*20/100
        lic=b*8/100
        pf=b*10/100
        data.ta=ta
        data.da=da
        data.hra=hra
        data.lic=lic
        data.pf=pf
        data.loan_limit=request.POST.get('loanlimit')
        data.status="active"
        data.save()


        data.job_id = "JM" + str(data.id)
        data.save()   
    return render(request,"addjobmaster.html")

def addvacancy(request):
    if request.method =='POST':
        c=tbl_vacancy.objects.filter(job_id=request.POST.get('jobid')).count()
        if c==0:
            data = tbl_vacancy()
            data.vac_no="na"
            data.job_id=request.POST.get('jobid')
            data3=tbl_job_master.objects.get(job_id=request.POST.get('jobid'))
            data.name=data3.job_name
            data.no_of_vac=request.POST.get('noofvacancy')
            data.age_limit=request.POST.get('agelimit')
            data.appli_last_date=request.POST.get('applicationlastdate')
            data.status="active"
            data.save()
            data.vac_no = "VN" + str(data.id)
            data.save()
        else:
            data5=tbl_vacancy.objects.get(job_id=request.POST.get('jobid'))
            data5.no_of_vac=request.POST.get('noofvacancy')
            data5.age_limit=request.POST.get('agelimit')
            data5.appli_last_date=request.POST.get('applicationlastdate')
            data5.save()
    return redirect('/vaccancy')


def givecomplaint(request):
    if request.method =='POST':
        data = tbl_complaint()
        data.complaint_id="na"
        data.employee_id=request.POST.get('employee_id')
        data.complaint=request.POST.get('complaint')
        data.complaint_date=datetime.datetime.now().strftime ("%Y-%m-%d")
        data.status="active"
        data.save()
        data.complaint_id= "complaint" + str(data.id)
        data.save()
    return redirect('/complaint')


def givefeedback(request):
    if request.method =='POST':
        data = tbl_feedback()
        data.feedback_id="na"
        data.feedback=request.POST.get('feedback')
        data.client_id=request.POST.get('client_id')
        data.date=datetime.datetime.now().strftime ("%Y-%m-%d")
        data.save()
        data.feedback_id= "feedback" + str(data.id)
        data.save()
    return redirect('/feedback1')


def addclient(request):
    if request.method == 'POST':
        data = tbl_client()
        data.client_id = "na"
        data.category = request.POST.get('category')
        data.name = request.POST.get('name')
        data.address = request.POST.get('address')
        data.phone  = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.status = "not_verified"
        Photo = request.FILES['resume']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.id_proof=uploaded_file_url
        data.save()
        data.client_id = "CL" + str(data.id)
        data.save()
    return render(request,"clientregistration.html")

def application(request):
    if request.method == 'POST':
        data=tbl_application()
        data.appli_no= "na"
        data.vac_no= request.POST.get('vacancynumber')
        data.applicant_name= request.POST.get('applicantname')
        data.address=request.POST.get('address')
        data.date_of_birth=request.POST.get('dob')
        data.age=request.POST.get('age')
        data.gender=request.POST.get('gender')
        data.mail=request.POST.get('email')
        data.phone=request.POST.get('phonenumber')
        data.qualification=request.POST.get('qualification')
        data.experience=request.POST.get('experience')
        Photo = request.FILES['resume']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.resume=uploaded_file_url


        data.status="pending"
        data.save()
        data.appli_no="AN"+str(data.id)
        data.save()
        data1 = tbl_login()
        data1.userid=data.appli_no
        data1.password=request.POST.get('phonenumber')
        data1.category="applicant"
        data1.save()
        
    return redirect('/viewservices')


def applyleave(request):
    if request.method == 'POST':
        data=tbl_leave()
        data.leave_id= "na"
        data.employee_id = request.POST.get('employeid')
        data.job_id=request.POST.get('jobname')
        data.leave_date=request.POST.get('leavedate')
        data.no_of_days=request.POST.get('days')
        data.application_date=datetime.datetime.now().strftime ("%Y-%m-%d")
        data.status="pending"
        data.save()
        data.leave_id="L"+str(data.id)
        data.save()
    return redirect('/leaveapplication')

def applyloan(request):
    if request.method == 'POST':
        data = tbl_loan()
        data.loan_id = "na"
        data.employee_id = request.POST.get('employeid')
        data.loan_amount = request.POST.get('loanamount')
        data.recovery_amount = request.POST.get('recoveryamount')
        data.loan_application_date =datetime.datetime.now().strftime ("%Y-%m-%d")
        data.loan_sanction_date = ""
        data.status = "pending"
        data.save()
        data.loan_id = "LD"+str(data.id)
        data.save()
    return redirect('/loanapplication')

def removejobmaster(request):
    data=tbl_job_master.objects.all()
    return render(request,"removejobmaster.html",{'data1':data})

def changejobmaster(request):
    data=tbl_job_master.objects.all()
    return render(request,"changejobmaster.html",{'data1':data})

def removejobmaster1(request,id):
    data=tbl_job_master.objects.get(id=id)
    data.delete()
    return redirect('/removejobmaster')

def verifyclient(request):
    data=tbl_client.objects.filter(status="not_verified")
    return render(request,"verifyclient.html",{'data1':data})
def changejob(request,id):    
    data=tbl_job_master.objects.get(id=id)
    return render(request,"changejob.html",{'data1':data})
def updatejob(request,id):    
    data=tbl_job_master.objects.get(id=id)
    data.experience=request.POST.get('experience')
    data.basic_sal=request.POST.get('basicsalary')

    data.save()
    return redirect('/changejobmaster')  

def viewapplication(request,id):
    data=tbl_application.objects.filter(vac_no=id).filter(status="pending")
    return render(request,"viewapplication.html",{'data1':data})

def viewjob(request):
    data=tbl_job_master.objects.all()
    return render(request,"viewjob.html",{'data1':data})

def generaterequest(request,id):
    data=tbl_job_master.objects.get(id=id)
    uid=request.session['client']
    return render(request,"generaterequest.html",{'data1':data,'uid':uid})

def addrequest(request):
    if request.method == 'POST':
        data = tbl_client_request()
        data.request_id = "na"
        data.jobmaster_id = request.POST.get('jobmaster_id')
        data.service_name = request.POST.get('service_name')
        data.client_id = request.POST.get('client_id')
        data.no_of_employees = request.POST.get('no_of_employees')
        data.request_date = datetime.datetime.now().strftime ("%Y-%m-%d")
        data.status = "pending"
        data.save()
        data.request_id = "R"+str(data.id)
        data.save()
    return redirect('/viewjob')
def acceptclient(request,id):
    data=tbl_client.objects.get(id=id)
    data.status="verified"
    data.save()
    data1 = tbl_login()
    data1.userid=data.client_id
    data1.password=data.phone
    data1.category="client"
    data1.save()
    return redirect('/verifyclient')
def rejectclient(request,id):
    data=tbl_client.objects.get(id=id)
    data.status="rejected"
    data.save()
    return redirect('/verifyclient')
def feedback1(request):
    data=tbl_client.objects.filter(status="verified")
    return render(request,"feedback1.html",{'data1':data})
def viewfeedback(request):
    data=tbl_client.objects.filter(status="verified")
    return render(request,"viewfeedback.html",{'data1':data})
def feedbackview(request,id):
    data=tbl_feedback.objects.filter(client_id=id)
    return render(request,"feedbackview.html",{'data1':data})

def viewservices(request):
    data=tbl_job_master.objects.all()
    return render(request,"viewservices.html",{'data1':data})  

def viewvacancy(request,id):
    data = tbl_vacancy.objects.filter(job_id=id)
    return render(request,"viewvacancy.html",{'data1':data})  

def viewjobmaster(request):

    
    data=tbl_job_master.objects.all()
    return render(request,"viewjobmaster.html",{'data1':data})

def viewvacancy1(request,id):
    data=tbl_vacancy.objects.filter(job_id=id)
    return render(request,"viewvacancy1.html",{'data1':data})

def jobmaster1(request):
    data=tbl_job_master.objects.all()
    return render(request,"jobmaster1.html",{'data1':data})

def vacancy1(request):
    data=tbl_vacancy.objects.all()
    return render(request,"vacancy1.html",{'data1':data})

def interviewlist(request,id):
    data=tbl_application.objects.get(id=id)
    return render(request,"interviewlist.html",{'data':data})

def addinterview(request):
    if request.method == 'POST':
        data = tbl_interview_list()
        data.interview_id = "na"
        data.vacancy_no = request.POST.get('vacancy_no')
        data.application_no = request.POST.get('application_no')
        data.interview_date = request.POST.get('interview_date')
        data.time = request.POST.get('time')
        data.venue = request.POST.get('venue')
        data.status = "pending"
        data.save()
        data.interview_id = "IL"+str(data.id)
        data.save()
        data1=tbl_application.objects.get(appli_no=request.POST.get('application_no'))
        data1.status="accepted"
        data1.save()
        dd=tbl_application.objects.get(appli_no=request.POST.get('application_no'))
        send_mail('interview details','interviewdate is'+request.POST.get('interview_date'),'from@example.co',[dd.mail,])
    return redirect('/viewjobmaster')

def viewinterview(request):
    data=tbl_interview_list.objects.filter(status="pending")
    return render(request,"viewinterview.html",{'data1':data})

def selectionlist(request,id):
    data=tbl_interview_list.objects.get(interview_id=id)
    return render(request,"selectionlist.html",{'data':data})


def addselection(request):
    if request.method == 'POST':
        data = tbl_selection_list()
        data.selection_id = "na"
        data.interview_id = request.POST.get('interview_id')
        data.applicant_name = request.POST.get('applicant_name')
        data.remark = request.POST.get('remark')
        data.reporting_date = request.POST.get('reporting_date')
        data.time = request.POST.get('time')
        data.reporting_office = request.POST.get('reporting_office')
        data.status = "pending"
        data.save()
        data.selection_id = "SL"+str(data.id)
        data.save()
        data1=tbl_interview_list.objects.get(interview_id=request.POST.get('interview_id'))
        data1.status="Added to selection list"
        data1.save()
    return redirect("/viewinterview")
def viewselectionlist(request):
    data=tbl_selection_list.objects.filter(status="pending")
    return render(request,"viewselectionlist.html",{'data1':data})

def appoint(request,id):
    data=tbl_selection_list.objects.get(selection_id=id)
    data1=tbl_application.objects.get(appli_no=data.applicant_name)
    return render(request,"appoint.html",{'data1':data1,'data':data})

def addemployee(request,id):
    if request.method == 'POST':
        data3=tbl_selection_list.objects.get(id=id)
        data = tbl_employee()
        data.employee_id = "na"
        data.vacancyname = request.POST.get('job_id')
        data.name = request.POST.get('name')
        data.address = request.POST.get('address')
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.date_of_birth = request.POST.get('date_of_birth')
        data.age = request.POST.get('age')
        data.gender = request.POST.get('gender')
        data.qualification = request.POST.get('qualification')
        data.experience = request.POST.get('experience')
        data.remark = request.POST.get('remark')
        data.date_of_join = request.POST.get('date_of_join')
        data.status="active"
        data.save()
        data.employee_id = "EL"+str(data.id)
        data.save()
        data3.status="selected as employee"
        data3.save()
        data1 = tbl_login()
        data1.userid=data.employee_id
        data1.password=request.POST.get('phone')
        data1.category="employee"
        data1.save()
    return redirect('/viewselectionlist')

def viewrequest(request,id):
    data=tbl_client_request.objects.filter(client_id=id)
    return render(request,"viewrequest.html",{'data1':data})

def viewclient(request):
    data=tbl_client.objects.all()
    return render(request,"viewclient.html",{'data1':data})
def vacancydetails(request,id):
    data = tbl_vacancy.objects.filter(name=id)
    return render(request,"vacancydetails.html",{'data1':data})  
def applicantdetails(request,id):
    data = tbl_application.objects.filter(appli_no=id)
    return render(request,"applicantdetails.html",{'data1':data})      
def applicantdetails1(request,id):
    data = tbl_application.objects.filter(appli_no=id)
    return render(request,"applicantdetails1.html",{'data1':data})    
def searchemployee(request):
    data=tbl_job_master.objects.all()
    return render(request,"searchemployee.html",{'data1':data})      
def searchemployee1(request,id):
    data = tbl_vacancy.objects.filter(job_id=id)
    return render(request,"searchemployee1.html",{'data1':data})    
def searchemployee2(request,id):
    data=tbl_employee.objects.filter(vacancyname=id)
    return render(request,"searchemployee2.html",{'data1':data})     
def applicationstatus(request):
    c=tbl_application.objects.filter(appli_no=request.session['applicant']).count()
    if c==0:
        return HttpResponse("appliactions not found......")
    else:

        data=tbl_application.objects.filter(appli_no=request.session['applicant'])
        return render(request,"applicationstatus.html",{'data1':data})
def interviewstatus(request):
    c=tbl_interview_list.objects.filter(application_no=request.session['applicant']).count()
    if c==0:
        return HttpResponse("you are not selected......try again")
    else:

        data=tbl_interview_list.objects.filter(application_no=request.session['applicant'])
        return render(request,"interviewstatus.html",{'data1':data})     
def selectionstatus(request):
    c=tbl_selection_list.objects.filter(applicant_name=request.session['applicant']).count()
    if c==0:
        return HttpResponse("you are not selected......try again")
    else:

        data=tbl_selection_list.objects.filter(applicant_name=request.session['applicant'])
        return render(request,"selectionstatus.html",{'data1':data})    
def allotmanager(request):
    data=tbl_employee.objects.all()
    return render(request,"allotmanager.html",{'data1':data})  
def allotmanager1(request,id):
    data=tbl_employee.objects.get(employee_id=id)
    return render(request,"allotmanager1.html",{'data1':data})      
def allotmanager2(request,id):
    data1 = tbl_login()
    data1.userid=id
    data1.password=request.POST.get('password')
    data1.category="manager"
    data1.save()
    return render(request,"adminheader.html") 
def leaveprocess(request):
    data=tbl_leave.objects.filter(status="pending")
    return render(request,"leaveprocess.html",{'data1':data})      
def leaveprocess1(request,id):
    data=tbl_leave.objects.get(id=id)
    data.status="approved"
    data.save()
    return redirect('/leaveprocess')    
def loanprocess(request):
    data=tbl_loan.objects.filter(status="pending")
    return render(request,"loanprocess.html",{'data1':data})      
def leaveprocess1(request,id):
    data=tbl_leave.objects.get(id=id)
    data.status="approved"
    data.save()
    return redirect('/leaveprocess')  
def loanprocess1(request,id):
    data=tbl_loan.objects.get(id=id)   
    return render(request,'loanprocess1.html',{'data':data})     
def loanprocess2(request,id):
    data=tbl_loan.objects.get(id=id)
    data.status="approved"
    data.loan_sanction_date=request.POST.get('sanctiondate')
    data.save()
    return redirect('/loanprocess')      
def salarystatement(request):
    data=tbl_employee.objects.all()
    return render(request,"salarystatement.html",{'data1':data})      
def salarystatement1(request,id):
    data=tbl_employee.objects.get(employee_id=id)
    data1=tbl_vacancy.objects.get(name=data.vacancyname)
    data3=tbl_job_master.objects.get(job_id=data1.job_id)
    b=data3.basic_sal
    g=int(data3.ta)+int(data3.da)+int(data3.hra)
    d=int(data3.pf)+int(data3.lic)
    n=int(b+g)-int(d)
    e=data.employee_id
    print(e)
    return render(request,"salarystatement1.html",{'b':b,'g':g,'n':n,'d':d,'id':e})
def salarystatement2(request):
    data=tbl_salary_statement.objects.filter(employee_id=request.POST.get('employeeid')).filter(month=request.POST.get('month')).count()
    if data==0:
        data1=tbl_salary_statement()
        data1.statement_id="na"
        data1.employee_id=request.POST.get('employeeid')
        data1.month=request.POST.get('month')
        data1.year=request.POST.get('year')
        data1.basic_salary=request.POST.get('basicsalary')
        data1.grows_pay=request.POST.get('g1')
        data1.deduction=request.POST.get('d')
        data1.netamount=request.POST.get('n')
        data1.save()
        data1.statement_id="statement"+str(data1.id)
        data1.save()
    else:
        return HttpResponse("salary statement already uploaded......")    
    return render(request,"manager.html")   
def acceptrequest(request,id):     
    data=tbl_client_request.objects.get(id=id)
    data1=tbl_vacancy.objects.get(job_id=data.jobmaster_id)
    data2=tbl_employee.objects.filter(vacancyname=data1.name).filter(status="active")
    return render(request,"allotemployee.html",{'data':data,'data2':data2})
def allotemployee(request):
    data1=tbl_client_employee()
    data1.client_employee_id="na"
    data1.emp_id=request.POST.get('employee')
    data1.client_id=request.POST.get('clientid')
    data1.request_id=request.POST.get('requestid')
    data1.allotment_date=datetime.datetime.now().strftime ("%Y-%m-%d")
    data1.status="active"
    data1.save()
    data1.client_employee_id="clientemployee"+str(data1.id)
    data1.save()  
    data=tbl_client_request.objects.get(request_id=request.POST.get('requestid'))
    data.status="accepted"
    data.save()
    data2=tbl_employee.objects.get(employee_id=request.POST.get('employee'))
    data2.status="inactive"
    data2.save()
    return redirect('/viewclient')
def updaterequest(request,id):
    data=tbl_client_employee.objects.filter(client_id=id)
    return render(request,"updaterequest.html",{'data':data})
def updaterequest1(request,id):
    data=tbl_client_employee.objects.get(id=id)
    data.status="completed"
    data.save()
    data2=tbl_employee.objects.get(employee_id=data.emp_id)
    data2.status="active"
    data2.save()
    data3=tbl_client_request.objects.get(request_id=data.request_id)
    data3.status="completed"
    data3.save()
    return redirect('/viewclient')
def updaterequest(request,id):
    data=tbl_client_employee.objects.filter(client_id=id)
    return render(request,"updaterequest.html",{'data':data})    
def viewallotment(request):
    data=tbl_client_request.objects.filter(client_id=request.session['client'])
    return render(request,"viewrequest1.html",{'data1':data})    
def viewallotment1(request,id):
    data=tbl_client_employee.objects.filter(request_id=id)
    return render(request,"viewallotment.html",{'data':data})      
def viewallotment2(request,id):     
    data=tbl_employee.objects.get(employee_id=id)
    return render(request,"viewallotment2.html",{'va':data})    
def leaveapplicationstatus(request):
    data=tbl_leave.objects.filter(employee_id=request.session['employee'])
    return render(request,"leaveapplicationstatus.html",{'data1':data})       
def loanapplicationstatus(request):
    data=tbl_loan.objects.filter(employee_id=request.session['employee'])
    return render(request,"loanapplicationstatus.html",{'data1':data})     
def salary(request):
    data=tbl_salary_statement.objects.filter(employee_id=request.session['employee'])
    return render(request,"salary.html",{'data1':data})    
def viewresume(request,id):
    data=tbl_application.objects.get(id=id)
    return render(request,"viewresume.html",{'data1':data})













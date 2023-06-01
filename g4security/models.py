from django.db import models
from django.db.models.base import Model

    
  

class tbl_job_master(models.Model):
   job_id = models.CharField(max_length=90)
   job_name = models.CharField(max_length=90)
   qualification = models.CharField(max_length=90)
   experience = models.CharField(max_length=90)
   basic_sal = models.IntegerField()
   ta = models.IntegerField()
   da = models.IntegerField()
   hra = models.IntegerField()
   lic = models.IntegerField()
   pf = models.IntegerField()
   loan_limit = models.CharField(max_length=90)
   status = models.CharField(max_length=90)
   
   class Meta:
       db_table = "tbl_job_master"

class tbl_vacancy(models.Model):
    vac_no = models.CharField(max_length=90)
    job_id  = models.CharField(max_length=90)
    name = models.CharField(max_length=90)
    no_of_vac = models.CharField(max_length=90)
    age_limit = models.CharField(max_length=90)
    appli_last_date = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_vacancy"

class tbl_complaint(models.Model):
    complaint_id = models.CharField(max_length=90)
    employee_id = models.CharField(max_length=90)
    complaint = models.CharField(max_length=90)
    complaint_date = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_complaint"

class tbl_feedback(models.Model):
   feedback_id = models.CharField(max_length=90)
   feedback = models.CharField(max_length=90)
   client_id = models.CharField(max_length=90)
   date = models.CharField(max_length=90)

   class Meta:
       db_table = "tbl_feedback"

class tbl_client(models.Model):
    client_id = models.CharField(max_length=90)
    category = models.CharField(max_length=90)
    name = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    id_proof = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_client"

class tbl_application(models.Model):
    appli_no = models.CharField(max_length=90)
    vac_no = models.CharField(max_length=90)
    applicant_name = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    date_of_birth = models.CharField(max_length=90)
    age = models.CharField(max_length=90)
    gender = models.CharField(max_length=90)
    mail = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    qualification = models.CharField(max_length=90)
    experience = models.CharField(max_length=90)
    resume = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_application"

class tbl_leave(models.Model):
    leave_id = models.CharField(max_length=90)
    employee_id = models.CharField(max_length=90)
    job_id = models.CharField(max_length=90)
    leave_date = models.CharField(max_length=90)
    no_of_days = models.CharField(max_length=90)
    application_date = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_leave"

class tbl_loan(models.Model):
    loan_id = models.CharField(max_length=90)
    employee_id = models.CharField(max_length=90)
    loan_amount = models.CharField(max_length=90)
    recovery_amount = models.CharField(max_length=90)
    loan_application_date = models.CharField(max_length=90)
    loan_sanction_date = models.CharField(max_length=90)
    status = models.CharField(max_length=90)


    class Meta:
        db_table = "tbl_loan"

class tbl_client_request(models.Model):
    request_id = models.CharField(max_length=90)
    jobmaster_id = models.CharField(max_length=90)
    service_name = models.CharField(max_length=90)
    client_id = models.CharField(max_length=90)
    no_of_employees = models.CharField(max_length=90)
    request_date = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_client_request"

class tbl_login(models.Model):
    userid = models.CharField(max_length=90)
    password = models.CharField(max_length=90)
    category = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_login"

class tbl_interview_list(models.Model):
    interview_id = models.CharField(max_length=90)
    vacancy_no = models.CharField(max_length=90)
    application_no = models.CharField(max_length=90)
    interview_date = models.CharField(max_length=90)
    time = models.CharField(max_length=90)
    venue = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_interview_list"



class tbl_selection_list(models.Model):
    selection_id = models.CharField(max_length=90)
    interview_id = models.CharField(max_length=90)
    applicant_name = models.CharField(max_length=90)
    remark = models.CharField(max_length=90)
    reporting_date = models.CharField(max_length=90)
    time = models.CharField(max_length=90)
    reporting_office = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_selection_list"

class tbl_employee(models.Model):
    employee_id = models.CharField(max_length=90)
    vacancyname = models.CharField(max_length=90)
    name = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    date_of_birth = models.CharField(max_length=90)
    age= models.CharField(max_length=90)
    gender = models.CharField(max_length=90)
    qualification = models.CharField(max_length=90)
    experience= models.CharField(max_length=90)
    remark= models.CharField(max_length=90)
    date_of_join = models.CharField(max_length=90)
    status=models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_employee"

class tbl_client_employee(models.Model):
    client_employee_id = models.CharField(max_length=90)
    client_id = models.CharField(max_length=90)
    emp_id = models.CharField(max_length=90)
    request_id = models.CharField(max_length=90)
    allotment_date = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_client_employee"
class tbl_salary_statement(models.Model):
    statement_id = models.CharField(max_length=90)
    month = models.CharField(max_length=90)
    year= models.CharField(max_length=90)
    employee_id = models.CharField(max_length=90)
    basic_salary= models.IntegerField()
    grows_pay = models.IntegerField()
    deduction = models.IntegerField()
    netamount = models.IntegerField()

    class Meta:
        db_table = "tbl_salary_statement"        

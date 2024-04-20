from django.db import models

# Create your models here.
# Model for Users
class wf_users(models.Model):
   
    userID = models.AutoField(primary_key=True)
    usertoken = models.CharField(max_length=100, null=True, blank=True)
    user_profile = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    useremail = models.EmailField(max_length=350, null=True, blank=True)
    password = models.CharField(max_length=300, null=True, blank=True)
    role_id = models.ForeignKey('wf_Rolemenu', on_delete=models.CASCADE)
    userlogtime = models.CharField(max_length=50, null=True, blank=True)
    userlogkey = models.CharField(max_length=50, null=True, blank=True)
    last_loggedon = models.DateTimeField(null=True, blank=True)
    createdby = models.IntegerField(default=0)
    createdon = models.DateTimeField(null=True, blank=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'wf_users'


# Model for Company.
class wf_Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey('wf_Rolemenu', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    company_location = models.TextField()
    company_address = models.TextField()
    company_contact_person_name = models.CharField(max_length=255)
    company_contact_email = models.CharField(max_length=255)
    company_contact_phone_number = models.CharField(max_length=15)
    company_image = models.ImageField(upload_to='company_images/', blank=True, null=True) # Change from CharField to ImageField
    company_resources_needed = models.IntegerField(default=0)  # Number of resources needed by the company
    company_service_provided = models.TextField()
    company_size = models.CharField(max_length=50)
    company_whatsapp_no = models.TextField()
    company_Linkedin = models.TextField()
    company_instagram = models.TextField()
    company_facebook = models.TextField()
    company_website = models.TextField()
    createby = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    deleted = models.IntegerField(default=0)
  
    class Meta:
        db_table = 'wf_Company'
        
       
class wf_Recruiter(models.Model):
    recruiter_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey('wf_Rolemenu', on_delete=models.CASCADE)
    recruiter_name = models.CharField(max_length=100)
    recruiter_email = models.CharField(max_length=255)
    recruiter_password = models.CharField(max_length=255)
    recruiter_qualification = models.CharField(max_length=100)
    recruiter_experience = models.CharField(max_length=100)
    recruiter_employee_since = models.DateField(null=True, blank=True)
    recruiter_image = models.ImageField(upload_to='recruiter_images/', blank=True, null=True)
    recruiter_role = models.CharField(max_length=255, null=True, blank=True)
    recruiter_mobile_number = models.CharField(max_length=20)
    recruiter_location = models.CharField(max_length=225)  # Added max_length
    recruiter_whatsapp_no = models.TextField()
    recruiter_Linkedin = models.TextField()
    recruiter_instagram = models.TextField()
    recruiter_facebook = models.TextField()
    recruiter_website = models.TextField()
    createby = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'wf_Recruiter'
 
#Model for Candidate        
class wf_Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey('wf_Rolemenu', on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=100)
    candidate_email = models.CharField(max_length=255)
    candidate_phone_number = models.CharField(max_length=15)
    candidate_experience = models.IntegerField(default=0)  # Experience in years
    candidate_skillset = models.TextField()  # Skillset as text
    candidate_working_hours = models.IntegerField(default=0)  # Working hours
    candidate_resume = models.FileField(upload_to='resumes/')  # Resume as varchar
    candidate_image = models.CharField(max_length=255, null=True, blank=True)  # Candidate image
    content = models.TextField()
    createby = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'wf_Candidate'
        
#Model for Rolemenu
class wf_Rolemenu(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, unique=True)
    createby = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'wf_Rolemenu'

class wf_jobpost(models.Model):
    job_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(wf_Company, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(wf_Recruiter, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_description_id = models.CharField(max_length=20, null=True)  # Change field to CharField with null=True
    job_salary_range = models.CharField(max_length=100)
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    ]
    job_priority = models.IntegerField(choices=PRIORITY_CHOICES)
    job_vacancies = models.IntegerField()
    job_skills = models.TextField()
    job_deadline = models.DateField()
    job_languages_known = models.CharField(max_length=255)
    job_qualification = models.CharField(max_length=255)
    job_description = models.TextField()
    job_employment_type = models.TextField()
    job_experience = models.IntegerField()
    job_preffered_shift = models.TextField() 
    job_location = models.TextField()
    job_working_days = models.CharField(max_length=225)
    job_monthly_incentives = models.CharField(max_length=225)
    job_key_responsibilites = models.TextField()
    job_requirements = models.TextField()
    createby = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    deleted = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'wf_jobpost'

# Model for JobAssign Details
class wf_jobassign_details(models.Model):
    assign_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(wf_Company, on_delete=models.CASCADE)
    recruiter_id = models.ForeignKey(wf_Recruiter, on_delete=models.CASCADE, default=1)
    job_id = models.ForeignKey(wf_jobpost, on_delete=models.CASCADE, default=1)
    job_status = models.CharField(max_length=30)
    createby = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'wf_jobassign_details'

class wf_talent(models.Model):
    talent_id = models.AutoField(primary_key=True)
    talent_name = models.CharField(max_length=100)
    talent_email = models.EmailField()
    talent_phone_number = models.CharField(max_length=20)
    talent_date_of_birth = models.DateField()
    talent_gender = models.CharField(max_length=20)        
    talent_martial_status = models.CharField(max_length=20)    
    talent_employment_type = models.CharField(max_length=20)    
    talent_prefered_shift = models.CharField(max_length=20)    
    talent_address = models.TextField()
    talent_location = models.TextField()
    talent_education = models.TextField()
    talent_experience = models.TextField()
    talent_career_objective = models.TextField()
    talent_certifications = models.TextField()
    talent_work_availability = models.TextField()
    talent_profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    talent_resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    talent_skills = models.TextField()  # Consider how you want to store skills, maybe as a comma-separated string or in another table
    talent_linkedin_profile_url = models.URLField(blank=True)
    talent_instagram_profile_url = models.URLField(blank=True)
    talent_facebook_profile_url = models.URLField(blank=True)
    role_id = models.ForeignKey('wf_Rolemenu', on_delete=models.CASCADE)
    createby = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    deleted = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'wf_talent'

class wf_Education(models.Model):
    talent = models.ForeignKey(wf_talent, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    college_batch = models.CharField(max_length=100)
    college_location = models.CharField(max_length=100)
    createby = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)
    deleted = models.IntegerField(default=0)
    class Meta:
        db_table = 'wf_Education'
        
class wf_Experience(models.Model):
    talent = models.ForeignKey(wf_talent, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    createby = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    deleted = models.IntegerField(default=0)
    class Meta:
        db_table = 'wf_Experience'
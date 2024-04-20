from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import wf_users,wf_Company,wf_Recruiter,wf_Candidate,wf_talent,wf_Education,wf_Experience
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import check_password
from django.utils import timezone
from django.http import JsonResponse,HttpResponse
from .models import wf_jobpost, wf_jobassign_details 
from datetime import datetime
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.db import IntegrityError
from django.db.models import Count

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username and password are provided
        if not username or not password:
            messages.error(request, 'Please enter your login credentials.')
            return redirect('login_view')

        try:
            # Attempt to retrieve the user from the custom user table
            user = wf_users.objects.get(username=username)
        except wf_users.DoesNotExist:
            # Handle the case where the user does not exist
            messages.error(request, 'Username does not exist.')
            return redirect('login_view')

        # Check if passwords match
        if not check_password(password, user.password):
            # If the passwords do not match, render the login page with an error message
            messages.error(request, 'Incorrect password.')
            return redirect('login_view')

        # If everything is correct, log in the user and redirect to the desired page
        request.session['user_id'] = user.userID
        return redirect('dashboard')

    # Render the login page for GET requests
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')




# Create a new user with a hashed password for USER TABLE - LOGIN 
# hashed_password = make_password('Workforce@123')
# Assuming 'admin_role' is the admin role object retrieved from wf_Rolemenu
# admin_role = wf_Rolemenu.objects.get(role_name='admin')  # Adjust this according to your actual implementation
# user = wf_users.objects.create(username='Admin', password=hashed_password)


######################################################################################################
#COMPANIES

def list_company(request):
    # Fetch all companies initially
    companies = wf_Company.objects.filter(deleted=0) 

    # Fetch distinct locations from the Company table
    locations = wf_Company.objects.values_list('company_location', flat=True).distinct()
   
    # Calculate counts for each location
    location_counts = {}
    for location in locations:
        location_counts[location] = companies.filter(company_location=location).count()

    # Fetch distinct company sizes from the Company table
    company_sizes = wf_Company.objects.values_list('company_size', flat=True).distinct()

    company_size_counts = {}
    for company_size in company_sizes:
        company_size_counts[company_size] = companies.filter(company_size=company_size).count()

    # Fetch distinct employment types from the JobPost table
    employment_types = wf_jobpost.objects.values_list('job_employment_type', flat=True).distinct()

    # Calculate counts for each employment type
    employment_type_counts = {}
    for employment_type in employment_types:
        employment_type_counts[employment_type] = wf_jobpost.objects.filter(job_employment_type=employment_type).count()
    
    # Query the JobPost table to get the count of jobs posted by each company
    job_counts_by_company = wf_jobpost.objects.values('company_id').annotate(job_count=Count('company_id'))
   
    # Handling filter parameters from the request
    location = request.GET.get('location')
    company_size = request.GET.get('company_size')
    employment_type = request.GET.get('employment_type')

    # Applying filters if they are provided in the request
    if location:
        companies = companies.filter(company_location=location)
    if company_size:
        companies = companies.filter(company_size=company_size)
    if employment_type:
        companies = companies.filter(company_id__in=wf_jobpost.objects.filter(job_employment_type=employment_type).values_list('company_id', flat=True))

    return render(request, 'list_company.html', {
        'companies': companies,
        'locations': locations,
        'company_sizes': company_sizes,
        'employment_types': employment_types,
        'location_counts': location_counts,
        'company_size_counts': company_size_counts,
        'employment_type_counts': employment_type_counts,
        'job_counts_by_company': job_counts_by_company,
    })

def preview_company(request, company_id):
    company = get_object_or_404(wf_Company, pk=company_id)
    # Add necessary logic here
    return render(request, 'preview_company.html', {'company': company})

def delete_company(request, company_id):
    # Ensure request method is POST
    if request.method == 'POST':
        # Retrieve the company object
        company = get_object_or_404(wf_Company, pk=company_id)
        
        # Mark the record as deleted (soft delete)
        company.deleted = 1
        
        try:
            # Save the changes to the database
            company.save()
        except Exception as e:
            # Handle any exceptions that occur during database operation
            return HttpResponseBadRequest("Error deleting company: {}".format(str(e)))
        
        # Redirect to the list of companies
        return redirect('list_company')
    else:
        # Handle other HTTP methods if needed
        return HttpResponseBadRequest("Only POST requests are allowed for deletion.")

def add_company(request):
    if request.method == 'POST':
        # Retrieve data from the form
        company_name = request.POST.get('company_name')
        company_description = request.POST.get('company_description')
        company_location = request.POST.get('company_location')
        company_contact_person_name = request.POST.get('company_contact_person_name')
        company_contact_email = request.POST.get('company_contact_email')
        company_contact_phone_number = request.POST.get('company_contact_phone_number')
        # company_resources_needed = request.POST.get('company_resources_needed')
        company_image = request.FILES.get('company_image')
        company_service_provided = request.POST.get('company_service_provided')
        company_size = request.POST.get('company_size')
        company_address = request.POST.get('company_address')
        company_website = request.POST.get('company_website')
        company_Linkedin = request.POST.get('company_Linkedin')
        company_instagram = request.POST.get('company_instagram')
        company_facebook = request.POST.get('company_facebook')
        # Create a new Company object with the retrieved data
        new_company = wf_Company(
            company_name=company_name,
            company_description=company_description,
            company_location=company_location,
            company_contact_person_name=company_contact_person_name,
            company_contact_email=company_contact_email,
            company_contact_phone_number=company_contact_phone_number,
            # company_resources_needed=company_resources_needed,
            company_service_provided=company_service_provided,
            company_image=company_image,
            company_size=company_size,
            company_address=company_address,
            company_website=company_website,
            company_Linkedin=company_Linkedin,
            company_instagram=company_instagram,
            company_facebook=company_facebook,
             role_id_id=1,  # Set default role_id_id to 1
            createdon=timezone.now()  # Set the creation timestamp
        )
        
        # Save the new company object to the database
        new_company.save()
        
         # Add a success message
        messages.success(request, 'Company created successfully!')
        
        
        # Redirect to the list_company view after successfully adding the company
        return redirect('list_company')
    
    # Render the form template for GET requests
    return render(request, 'add_company.html')


def edit_company(request, company_id):
    company = get_object_or_404(wf_Company, pk=company_id)
    if request.method == 'POST':
        # Handle form submission for editing company details
        company.company_name = request.POST['company_name']
        company.company_description = request.POST['company_description']
        company.company_location = request.POST['company_location']
        company.company_size = request.POST['company_size']
        company.company_contact_person_name = request.POST['company_contact_person_name']
        company.company_image = request.FILES.get('company_image')  # Use FILES for file upload
        company.company_contact_email = request.POST['company_contact_email']
        company.company_contact_phone_number = request.POST['company_contact_phone_number']
        company.company_service_provided = request.POST['company_service_provided']
        company.company_address = request.POST['company_address']
        company.company_website = request.POST['company_website']
        company.company_Linkedin = request.POST['company_Linkedin']
        company.company_instagram = request.POST['company_instagram']
        company.company_facebook = request.POST['company_facebook']
       
        # Save the updated company object
        company.save()
        return redirect('list_company')  # Redirect to company list page after editing
    return render(request, 'edit_company.html', {'company': company})



######################################################################################################

#RECRUITERS
def list_recruiters(request):
    recruiters = wf_Recruiter.objects.filter(deleted=0)  # Assuming Recruiter is your model for storing recruiter information
    return render(request, 'list_recruiter.html', {'recruiters': recruiters})

def add_recruiters(request):
    if request.method == 'POST':
        # Retrieve data from the form
        recruiter_name = request.POST.get('recruiter_name')
        recruiter_email = request.POST.get('recruiter_email')
        recruiter_experience = request.POST.get('recruiter_experience')
        recruiter_qualification = request.POST.get('recruiter_qualification')
        recruiter_mobile_number = request.POST.get('recruiter_mobile_number')
        recruiter_location = request.POST.get('recruiter_location')
        recruiter_image = request.FILES.get('recruiter_image')
        recruiter_role = request.POST.get('recruiter_role')
        recruiter_Linkedin = request.POST.get('recruiter_Linkedin')
        recruiter_instagram = request.POST.get('recruiter_instagram')
        recruiter_facebook = request.POST.get('recruiter_facebook')
        

        # Create a new Company object with the retrieved data
        new_recruiter = wf_Recruiter(
            recruiter_name=recruiter_name,
            recruiter_email=recruiter_email,
            recruiter_experience=recruiter_experience,
            recruiter_qualification=recruiter_qualification,
            recruiter_mobile_number=recruiter_mobile_number,
            recruiter_location=recruiter_location,
            recruiter_image=recruiter_image,
            recruiter_role=recruiter_role,
            recruiter_Linkedin=recruiter_Linkedin,
            recruiter_instagram=recruiter_instagram,
            recruiter_facebook=recruiter_facebook,
             role_id_id=1,  # Set default role_id_id to 1
            createdon=timezone.now()  # Set the creation timestamp
        )
        
        # Save the new company object to the database
        new_recruiter.save()
        
         # Add a success message
        messages.success(request, 'Recruiter created successfully!')
        
        
        # Redirect to the list_company view after successfully adding the company
        return redirect('list_recruiters')
    
    # Render the form template for GET requests
    return render(request, 'add_recruiters.html')        
       

def edit_recruiters(request, recruiter_id):
    recruiter = get_object_or_404(wf_Recruiter, pk=recruiter_id)
    if request.method == 'POST':
        # Handle form submission for editing company details
        recruiter.recruiter_name = request.POST['recruiter_name']
        recruiter.recruiter_email = request.POST['recruiter_email']
        recruiter.recruiter_image = request.FILES.get('recruiter_image')  # Use FILES for file upload
        recruiter.recruiter_qualification = request.POST['recruiter_qualification']
        recruiter.recruiter_experience = request.POST['recruiter_experience']
        recruiter.recruiter_mobile_number = request.POST['recruiter_mobile_number']
        recruiter.recruiter_location = request.POST['recruiter_location']
        recruiter.recruiter_role = request.POST['recruiter_role']
        recruiter.recruiter_Linkedin = request.POST['recruiter_Linkedin']
        recruiter.recruiter_instagram = request.POST['recruiter_instagram']
        recruiter.recruiter_facebook = request.POST['recruiter_facebook']
       
        # Save the updated company object
        recruiter.save()
        return redirect('list_recruiters')  # Redirect to company list page after editing
    return render(request, 'edit_recruiters.html', {'recruiter': recruiter})       
        

def preview_recruiters(request,recruiter_id):
    recruiter = get_object_or_404(wf_Recruiter, pk=recruiter_id)
    return render(request, 'preview_recruiters.html', {'recruiter': recruiter})



def delete_recruiter(request, recruiter_id):
    # Ensure request method is POST
    if request.method == 'POST':
        # Retrieve the recruiter object
        recruiter = get_object_or_404(wf_Recruiter, pk=recruiter_id)
        
        # Mark the record as deleted
        recruiter.deleted = True
        
        try:
            # Save the changes to the database
            recruiter.save()
        except Exception as e:
            # Handle any exceptions that occur during database operation
            return HttpResponseBadRequest("Error deleting recruiter: {}".format(str(e)))
        
        # Redirect to a desired page after deletion (e.g., back to the list of recruiters)
        return redirect('list_recruiters')
    else:
        # Handle other HTTP methods if needed
        return HttpResponseBadRequest("Only POST requests are allowed for deletion.")

######################################################################################################
  
#JOBS

def list_jobs(request):
    # Fetch all job posts along with their associated companies
    jobs_with_companies = wf_jobpost.objects.select_related('company')

    # Fetch distinct values for job location, work status, salary range, and skills
    job_locations = jobs_with_companies.values_list('job_location', flat=True).distinct()
    job_employment_type = jobs_with_companies.values_list('job_employment_type', flat=True).distinct()
    job_salary_ranges = jobs_with_companies.values_list('job_salary_range', flat=True).distinct()
    job_skills = jobs_with_companies.values_list('job_skills', flat=True).distinct()

  # Split the skills string into a list of individual skills
    job_skills_list = set()  # Use a set to ensure unique skills
    for skills_string in job_skills:
        skills_list = skills_string.split(',')
        for skill in skills_list:
            job_skills_list.add(skill.strip())

    # Calculate the total count of jobs
    total_jobs_count = jobs_with_companies.count()

    # Handling filter parameters from the request
    job_location = request.GET.get('job_location')
    selected_skills = request.GET.getlist('job_skills')  # Handle multiple skills
    job_salary_range = request.GET.get('job_salary_range')

    # Applying filters if they are provided in the request
    if job_location:
        jobs_with_companies = jobs_with_companies.filter(job_location=job_location)
    if job_salary_range:
        jobs_with_companies = jobs_with_companies.filter(job_salary_range=job_salary_range)
    if selected_skills:
        filtered_jobs = []
        for job in jobs_with_companies:
            job_skills = job.job_skills.split(',')
            if any(skill.strip() in selected_skills for skill in job_skills):
                filtered_jobs.append(job)
        jobs_with_companies = filtered_jobs

    return render(request, 'list_jobs.html', {
        'jobs_with_companies': jobs_with_companies,
        'job_locations': job_locations,
        'job_employment_type': job_employment_type,
        'job_salary_ranges': job_salary_ranges,
        'job_skills_list': job_skills_list,
        'total_jobs_count': total_jobs_count,
    })

# def add_jobs(request):
#     if request.method == 'POST':
#         try:
#             # Retrieve form data
#             job_title = request.POST.get('job_title')
#             company_id = request.POST.get('company')
#             recruiter_id = request.POST.get('recruiter')
#             job_description_id = request.POST.get('job_description_id')
#             job_priority_str = request.POST.get('priority', 'Low')  # Default value is 'Low' if 'priority' is None or empty
#             job_vacancies = request.POST.get('vacancies')
#             job_skills = request.POST.get('skills')
#             job_preffered_work_status = request.POST.get('job_preffered_work_status')
#             job_location = request.POST.get('job_location')
#             job_deadline = request.POST.get('job-deadline')
#             #job_languages_known = request.POST.get('languages_known')
#             job_qualification = request.POST.get('qualifications')
#             job_description = request.POST.get('job-description')
#             job_experience = request.POST.get('job_experience')
#             # Map priority string value to integer value
#             job_priority_map = {'High': 1, 'Medium': 2, 'Low': 3}
#             job_priority = job_priority_map.get(job_priority_str)
#             # job_employment_type = request.POST.get('job_employment_type')
            
#             # Create job post instance
#             job_post = wf_jobpost.objects.create(
#                 job_title=job_title,
#                 company_id=company_id,
#                 recruiter_id=recruiter_id,
#                 job_description_id=job_description_id,
#                 job_priority=job_priority,
#                 job_vacancies=job_vacancies,
#                 job_skills=job_skills,
#                 job_deadline=job_deadline,
#                 #job_languages_known=job_languages_known,
#                 job_qualification=job_qualification,
#                 job_description=job_description,
#                 job_experience=job_experience,
#                 job_preffered_work_status=job_preffered_work_status,
#                 job_location=job_location,
#                 # job_employment_type=job_employment_type,
#             )

#             # Save the new job post object to the database
#             job_post.save()

#             # Redirect to the list_company view after successfully adding the company
#             return redirect('list_jobs')
        
#         except IntegrityError:
#             error_message = "Integrity Error: Unable to add job post. Please ensure that the company and recruiter IDs are valid."
#             return render(request, 'error.html', {'error_message': error_message})

#     else:
#         # Retrieve companies and recruiters from the database
#         companies = wf_Company.objects.all()
#         recruiters = wf_Recruiter.objects.all()

#         # Render the form with companies and recruiters data
#         return render(request, 'add_jobs.html', {'companies': companies, 'recruiters': recruiters})

def add_jobs(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        company_id = request.POST.get('company')
        recruiter_id = request.POST.get('recruiter')
        job_description_id = request.POST.get('job_description_id')
        job_salary_range = request.POST.get('job_salary_range')
        job_priority = request.POST.get('job_priority')
        job_vacancies = request.POST.get('vacancies')
        job_skills = request.POST.get('skills')
        job_deadline = request.POST.get('job-deadline')
        # job_languages_known = request.POST.get('languages_known')
        job_qualification = request.POST.get('qualifications')
        job_description = request.POST.get('job_description')
        job_employment_type = request.POST.get('job_employment_type')
        job_experience = request.POST.get('job_experience')
        job_preffered_shift = request.POST.get('job_preffered_shift')
        job_location = request.POST.get('job_location')
        job_working_days = request.POST.get('job_working_days')
        job_monthly_incentives = request.POST.get('job_monthly_incentives')
        job_key_responsibilites = request.POST.get('job_key_responsibilites')
        job_requirements = request.POST.get('job_requirements')
        
        # Perform basic validation
        if not job_title:
            messages.error(request, 'Please provide a job title.')
            return redirect('add_jobs')
        
        # Create job post instance
        job_post = wf_jobpost(
            company_id=company_id,
            recruiter_id=recruiter_id,
            job_title=job_title,
            job_description_id=job_description_id,
            job_salary_range=job_salary_range,
            job_priority=job_priority,
            job_vacancies=job_vacancies,
            job_skills=job_skills,
            job_deadline=job_deadline,
            # job_languages_known=job_languages_known,
            job_qualification=job_qualification,
            job_description=job_description,
            job_employment_type=job_employment_type,
            job_experience=job_experience,
            job_preffered_shift=job_preffered_shift,
            job_location=job_location,
            job_working_days=job_working_days,
            job_monthly_incentives=job_monthly_incentives,
            job_key_responsibilites=job_key_responsibilites,
            job_requirements=job_requirements,
        )
        job_post.save()
        
        messages.success(request, 'Job posted successfully!')
        return redirect('list_jobs')
        
    companies = wf_Company.objects.all()
    recruiters = wf_Recruiter.objects.all()
    priority_choices = wf_jobpost.PRIORITY_CHOICES
    shift_choices = ['Day Shift', 'Night Shift', 'Flexible Shift']  # Define your shift choices
    incentive_choices = ['Fixed', 'Based on Performance']  # Define your incentive choices
    work_status_choices = ['Fresher', 'Experience']  # Define your work status choices
    return render(request, 'add_jobs.html', {'companies': companies, 'recruiters': recruiters, 'priority_choices': priority_choices, 'shift_choices': shift_choices, 'incentive_choices': incentive_choices,'work_status_choices': work_status_choices})




# def edit_jobs(request, job_id):
#     jobs = get_object_or_404(wf_jobpost, pk=job_id)
#     if request.method == 'POST':
#         # Handle form submission for editing company details
#         jobs.job_title = request.POST['job_title']
#         jobs.job_priority = request.POST('job_priority')  
#         jobs.job_qualification = request.POST['job_qualification']
#         jobs.job_description = request.POST['job_description']
#         jobs.job_vacancies = request.POST['job_vacancies']
#         jobs.job_skills = request.POST['job_skills']
#         jobs.job_deadline = request.POST['job_deadline']
#         jobs.job_experience = request.POST['job_experience']
#         jobs.job_preffered_work_status = request.POST['job_preffered_work_status']
#         jobs.job_location = request.POST['job_location']
#         jobs.job_employment_type = request.POST['job_employment_type']
#         jobs.recruiter = request.POST['recruiter']
#         jobs.company_id = request.POST['company']
       
#         # Save the updated company object
#         jobs.save()
#         return redirect('list_jobs')  # Redirect to company list page after editing
#     return render(request, 'edit_jobs.html', {'jobs': jobs})  


def edit_jobs(request, job_id):
    job = get_object_or_404(wf_jobpost,pk=job_id)

    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        company_id = request.POST.get('company')
        recruiter_id = request.POST.get('recruiter')
        job_description_id = request.POST.get('job_description_id')
        job_salary_range = request.POST.get('job_salary_range')
        job_priority = request.POST.get('job_priority')
        job_vacancies = request.POST.get('job_vacancies')
        job_skills = request.POST.get('skills')
        # job_deadline = request.POST.get('job-deadline')
        # job_deadline = datetime.strptime(request.POST.get('job-deadline'), '%Y-%m-%d')
        job_deadline_str = request.POST.get('job_deadline')
        if job_deadline_str:  # Check if job_deadline_str is not None
            job_deadline = datetime.strptime(job_deadline_str, '%Y-%m-%d').strftime('%Y-%m-%d')
        else:
            job_deadline = None
        # job_languages_known = request.POST.get('languages_known')
        job_qualification = request.POST.get('qualifications')
        job_description = request.POST.get('job_description')
        job_employment_type = request.POST.get('job_employment_type')
        job_experience = request.POST.get('job_experience')
        job_preffered_shift = request.POST.get('job_preffered_shift')
        job_location = request.POST.get('job_location')
        job_working_days = request.POST.get('job_working_days')
        job_monthly_incentives = request.POST.get('job_monthly_incentives')
        job_key_responsibilites = request.POST.get('job_key_responsibilites')
        job_requirements = request.POST.get('job_requirements')
        
        # Perform basic validation
        if not job_title:
            messages.error(request, 'Please provide a job title.')
            return redirect('edit_jobs', job_id=job_id)
        
        # Update job post instance
        job.company_id = company_id
        job.recruiter_id = recruiter_id
        job.job_title = job_title
        job.job_description_id = job_description_id
        job.job_salary_range = job_salary_range
        job.job_priority = job_priority
        job.job_vacancies = job_vacancies
        job.job_skills = job_skills
        job.job_deadline = job_deadline
        # job.job_languages_known = job_languages_known
        job.job_qualification = job_qualification
        job.job_description = job_description
        job.job_employment_type = job_employment_type
        job.job_experience = job_experience
        job.job_preffered_shift = job_preffered_shift
        job.job_location = job_location
        job.job_working_days = job_working_days
        job.job_monthly_incentives = job_monthly_incentives
        job.job_key_responsibilites = job_key_responsibilites
        job.job_requirements = job_requirements
        
        job.save()
        
        messages.success(request, 'Job updated successfully!')
        return redirect('list_jobs')
        
    companies = wf_Company.objects.all()
    recruiters = wf_Recruiter.objects.all()
    priority_choices = wf_jobpost.PRIORITY_CHOICES
    shift_choices = ['Day Shift', 'Night Shift', 'Flexible Shift']  # Define your shift choices
    incentive_choices = ['Fixed', 'Based on Performance']  # Define your incentive choices
    work_status_choices = ['Fresher', 'Experience']  # Define your work status choices
    
    return render(request, 'edit_jobs.html', {'job': job, 'companies': companies, 'recruiters': recruiters, 'priority_choices': priority_choices, 'shift_choices': shift_choices, 'incentive_choices': incentive_choices,'work_status_choices': work_status_choices})




def track_jobs(request):
     # Fetch job details from wf_jobpost
    job_details = wf_jobpost.objects.all()
    
    context = {
        'job_details': job_details
    }
    return render(request, 'track_jobs.html', context)

def preview_jobs(request):
    return render(request, 'preview_jobs.html')

def company_dashboard(request):
    return render(request, 'company_dashboard.html')

def preview_jobs(request,job_id):
    jobs = get_object_or_404(wf_jobpost, pk=job_id)
    return render(request, 'preview_jobs.html', {'jobs': jobs})
######################################################################################################

#MEETINGS
def list_meetings(request):
    return render(request, 'list_meetings.html')

######################################################################################################

#Talent
# def list_talent(request):
#     talents = wf_talent.objects.all()  # Assuming Recruiter is your model for storing recruiter information
#     return render(request,'list_talent.html' ,  {'talents': talents})

def list_talent(request):
    # Fetch all talent data
    talents = wf_talent.objects.filter(deleted=0)

    # Fetch education data
    educations = wf_Education.objects.all()

    # Fetch experience data
    experiences = wf_Experience.objects.all()

    # Preprocess skills data
    for talent in talents:
        talent.skills = talent.talent_skills.split(',')

    # Pass all data to the template
    return render(request, 'list_talent.html', {'talents': talents, 'educations': educations, 'experiences': experiences})



def add_talent(request):
    if request.method == 'POST':
        talent_name = request.POST.get('talent_name')
        talent_email = request.POST.get('talent_email')
        talent_phone_number = request.POST.get('talent_phone_number')
        talent_date_of_birth_str = request.POST.get('talent_date_of_birth')
        talent_date_of_birth = datetime.strptime(talent_date_of_birth_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        talent_gender = request.POST.get('talent_gender')
        if not talent_gender:
            return HttpResponseBadRequest("Gender is required.")
        talent_martial_status = request.POST.get('talent_martial_status')
        talent_work_availability = request.POST.get('talent_work_availability')
        talent_employment = request.POST.get('talent_employment')
        talent_skills = request.POST.get('talent_skills')
        talent_career_objective = request.POST.get('talent_career_objective')
        talent_certifications = request.POST.get('talent_certifications')
        talent_linkedin_profile_url = request.POST.get('talent_linkedin_profile_url')
        talent_instagram_profile_url = request.POST.get('talent_instagram_profile_url')
        talent_facebook_profile_url = request.POST.get('talent_facebook_profile_url')
        talent_address = request.POST.get('talent_address')
        talent_resume_file = request.FILES.get('talent_resume')
        talent_profile_image_file = request.FILES.get('talent_profile_image')
        talent_prefered_shift = request.POST.get('talent_prefered_shift')
        talent_location = request.POST.get('talent_location')

        talent = wf_talent.objects.create(
            talent_name=talent_name,
            talent_email=talent_email,
            talent_phone_number=talent_phone_number,
            talent_date_of_birth=talent_date_of_birth,
            talent_gender=talent_gender,
            talent_martial_status=talent_martial_status,
            talent_employment_type=talent_employment,
            talent_work_availability=talent_work_availability,
            talent_skills=talent_skills,
            talent_career_objective=talent_career_objective,
            talent_certifications=talent_certifications,
            talent_linkedin_profile_url=talent_linkedin_profile_url,
            talent_instagram_profile_url=talent_instagram_profile_url,
            talent_facebook_profile_url=talent_facebook_profile_url,
            talent_address=talent_address,
            talent_resume=talent_resume_file,
            talent_profile_image=talent_profile_image_file,
            talent_prefered_shift=talent_prefered_shift,
            talent_location=talent_location,
            role_id_id=1
        )

        education_data = zip(request.POST.getlist('college_name[]'),
                             request.POST.getlist('degree[]'),
                             request.POST.getlist('college_batch[]'),
                             request.POST.getlist('college_location[]'))

        for college_name, degree, college_batch, college_location in education_data:
            wf_Education.objects.create(
                talent=talent,
                college_name=college_name,
                degree=degree,
                college_batch=college_batch,
                college_location=college_location
            )

        experience_data = zip(request.POST.getlist('company_name[]'),
                              request.POST.getlist('company_location[]'),
                              request.POST.getlist('start_date[]'),
                              request.POST.getlist('end_date[]'))

        for company_name, company_location, start_date, end_date in experience_data:
            start_date = datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d') if start_date else None
            end_date = datetime.strptime(end_date, '%d/%m/%Y').strftime('%Y-%m-%d') if end_date else None
            wf_Experience.objects.create(
                talent=talent,
                company_name=company_name,
                company_location=company_location,
                start_date=start_date,
                end_date=end_date
            )

        return redirect('list_talent')

    return render(request, 'add_talents.html')

def edit_talent(request, talent_id):
    # Fetch the talent object to be edited
    talent = get_object_or_404(wf_talent, pk=talent_id)
    educations = wf_Education.objects.filter(talent=talent)
    experiences = wf_Experience.objects.filter(talent=talent)
    if request.method == 'POST':
        # Update talent data from the POST request
        talent.name = request.POST.get('name')
        talent.email = request.POST.get('email')
        talent.phone_number = request.POST.get('phone_number')
        date_of_birth_str = request.POST.get('date_of_birth')
        talent.date_of_birth = datetime.strptime(date_of_birth_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        talent.gender = request.POST.get('select_gender')
        talent.martial_status = request.POST.get('select_martial_status')
        talent.work_status = request.POST.get('work_status')
        talent.career_objective = request.POST.get('career_objective')
        talent.certifications = request.POST.get('certifications')
        talent.talent_profile_image = request.POST.get('talent_profile_image')
        talent.linkedin_profile_url = request.POST.get('linkedin_profile_url')
        talent.instagram_profile_url = request.POST.get('instagram_profile_url')
        talent.facebook_profile_url = request.POST.get('facebook_profile_url')
        talent.role_id_id = 1  # Set default role_id_id to 1

        # Save the updated talent object
        talent.save()

        # Process education data
        wf_Education.objects.filter(talent=talent).delete()  # Delete existing education data
        education_data = zip(request.POST.getlist('college_name[]'),
                             request.POST.getlist('degree[]'),
                             request.POST.getlist('college_batch[]'),
                             request.POST.getlist('college_location[]'))

        for college_name, degree, college_batch, college_location in education_data:
            wf_Education.objects.create(
                talent=talent,
                college_name=college_name,
                degree=degree,
                college_batch=college_batch,
                college_location=college_location
            )

        # Process experience data
        wf_Experience.objects.filter(talent=talent).delete()  # Delete existing experience data
        experience_data = zip(request.POST.getlist('company_name[]'),
                              request.POST.getlist('company_location[]'),
                              [datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d') if date else None for date in request.POST.getlist('start_date[]')],
                              [datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d') if date else None for date in request.POST.getlist('end_date[]')])

        for company_name, company_location, start_date, end_date in experience_data:
            if start_date is not None:
                wf_Experience.objects.create(
                    talent=talent,
                    company_name=company_name,
                    company_location=company_location,
                    start_date=start_date,
                    end_date=end_date
                )

        # Redirect to a success page or any other desired page after talent update
        return redirect('list_talent')

    # Render the edit talent form template if request method is GET
    return render(request, 'edit_talents.html', {'talent': talent ,'educations': educations ,'experiences': experiences})


def preview_talent(request, id):
    talent = get_object_or_404(wf_talent, pk=id)
    talent_skills_list = talent.talent_skills.split(",")  # Split skills string into a list
    education = wf_Education.objects.filter(talent=talent)
    experience = wf_Experience.objects.filter(talent=talent)
    return render(request, 'preview_talent.html', {'talent': talent, 'talent_skills_list': talent_skills_list, 'education': education, 'experience': experience})

def delete_talent(request, talent_id):
    # Ensure request method is POST
    if request.method == 'POST':
        # Retrieve the talent object
        talent = get_object_or_404(wf_talent, pk=talent_id)
        
        # Mark the record as deleted (soft delete)
        talent.deleted = 1
        
        try:
            # Save the changes to the database
            talent.save()
        except Exception as e:
            # Handle any exceptions that occur during database operation
            return HttpResponseBadRequest("Error deleting talent: {}".format(str(e)))
        
        # Redirect to the list of companies
        return redirect('list_talent')
    else:
        # Handle other HTTP methods if needed
        return HttpResponseBadRequest("Only POST requests are allowed for deletion.")

######################################################################################################
def recruiters_dashboard(request):
    return render(request, 'recruiters_dashboard.html')
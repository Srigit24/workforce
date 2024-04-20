# Generated by Django 5.0.4 on 2024-04-17 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wf_Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('company_description', models.TextField()),
                ('company_location', models.TextField()),
                ('company_address', models.TextField()),
                ('company_contact_person_name', models.CharField(max_length=255)),
                ('company_contact_email', models.CharField(max_length=255)),
                ('company_contact_phone_number', models.CharField(max_length=15)),
                ('company_image', models.ImageField(blank=True, null=True, upload_to='company_images/')),
                ('company_resources_needed', models.IntegerField(default=0)),
                ('company_service_provided', models.TextField()),
                ('company_size', models.CharField(max_length=50)),
                ('company_whatsapp_no', models.TextField()),
                ('company_Linkedin', models.TextField()),
                ('company_instagram', models.TextField()),
                ('company_facebook', models.TextField()),
                ('company_website', models.TextField()),
                ('createby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'wf_Company',
            },
        ),
        migrations.CreateModel(
            name='wf_Recruiter',
            fields=[
                ('recruiter_id', models.AutoField(primary_key=True, serialize=False)),
                ('recruiter_name', models.CharField(max_length=100)),
                ('recruiter_email', models.CharField(max_length=255)),
                ('recruiter_password', models.CharField(max_length=255)),
                ('recruiter_qualification', models.CharField(max_length=100)),
                ('recruiter_experience', models.CharField(max_length=100)),
                ('recruiter_employee_since', models.DateField(blank=True, null=True)),
                ('recruiter_image', models.ImageField(blank=True, null=True, upload_to='recruiter_images/')),
                ('recruiter_role', models.CharField(blank=True, max_length=255, null=True)),
                ('recruiter_mobile_number', models.CharField(max_length=20)),
                ('recruiter_location', models.CharField(max_length=225)),
                ('recruiter_whatsapp_no', models.TextField()),
                ('recruiter_Linkedin', models.TextField()),
                ('recruiter_instagram', models.TextField()),
                ('recruiter_facebook', models.TextField()),
                ('recruiter_website', models.TextField()),
                ('createby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'wf_Recruiter',
            },
        ),
        migrations.CreateModel(
            name='wf_Rolemenu',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50, unique=True)),
                ('createby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'wf_Rolemenu',
            },
        ),
        migrations.CreateModel(
            name='wf_jobpost',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=255)),
                ('job_description_id', models.CharField(max_length=20, null=True)),
                ('job_salary_range', models.CharField(max_length=100)),
                ('job_priority', models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')])),
                ('job_vacancies', models.IntegerField()),
                ('job_skills', models.TextField()),
                ('job_deadline', models.DateField()),
                ('job_languages_known', models.CharField(max_length=255)),
                ('job_qualification', models.CharField(max_length=255)),
                ('job_description', models.TextField()),
                ('job_employment_type', models.TextField()),
                ('job_experience', models.IntegerField()),
                ('job_preffered_shift', models.TextField()),
                ('job_location', models.TextField()),
                ('job_working_days', models.CharField(max_length=225)),
                ('job_monthly_incentives', models.CharField(max_length=225)),
                ('job_key_responsibilites', models.TextField()),
                ('job_requirements', models.TextField()),
                ('createby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_company')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_recruiter')),
            ],
            options={
                'db_table': 'wf_jobpost',
            },
        ),
        migrations.CreateModel(
            name='wf_jobassign_details',
            fields=[
                ('assign_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_status', models.CharField(max_length=30)),
                ('createby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_company')),
                ('job_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_jobpost')),
                ('recruiter_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_recruiter')),
            ],
            options={
                'db_table': 'wf_jobassign_details',
            },
        ),
        migrations.AddField(
            model_name='wf_recruiter',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_rolemenu'),
        ),
        migrations.AddField(
            model_name='wf_company',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_rolemenu'),
        ),
        migrations.CreateModel(
            name='wf_Candidate',
            fields=[
                ('candidate_id', models.AutoField(primary_key=True, serialize=False)),
                ('candidate_name', models.CharField(max_length=100)),
                ('candidate_email', models.CharField(max_length=255)),
                ('candidate_phone_number', models.CharField(max_length=15)),
                ('candidate_experience', models.IntegerField(default=0)),
                ('candidate_skillset', models.TextField()),
                ('candidate_working_hours', models.IntegerField(default=0)),
                ('candidate_resume', models.FileField(upload_to='resumes/')),
                ('candidate_image', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField()),
                ('createby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_rolemenu')),
            ],
            options={
                'db_table': 'wf_Candidate',
            },
        ),
        migrations.CreateModel(
            name='wf_talent',
            fields=[
                ('talent_id', models.AutoField(primary_key=True, serialize=False)),
                ('talent_name', models.CharField(max_length=100)),
                ('talent_email', models.EmailField(max_length=254)),
                ('talent_phone_number', models.CharField(max_length=20)),
                ('talent_date_of_birth', models.DateField()),
                ('talent_gender', models.CharField(max_length=20)),
                ('talent_martial_status', models.CharField(max_length=20)),
                ('talent_employment_type', models.CharField(max_length=20)),
                ('talent_prefered_shift', models.CharField(max_length=20)),
                ('talent_address', models.TextField()),
                ('talent_location', models.TextField()),
                ('talent_education', models.TextField()),
                ('talent_experience', models.TextField()),
                ('talent_career_objective', models.TextField()),
                ('talent_certifications', models.TextField()),
                ('talent_work_availability', models.TextField()),
                ('talent_profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('talent_resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('talent_skills', models.TextField()),
                ('talent_linkedin_profile_url', models.URLField(blank=True)),
                ('talent_instagram_profile_url', models.URLField(blank=True)),
                ('talent_facebook_profile_url', models.URLField(blank=True)),
                ('createby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_rolemenu')),
            ],
            options={
                'db_table': 'wf_talent',
            },
        ),
        migrations.CreateModel(
            name='wf_Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_location', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('createby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_talent')),
            ],
            options={
                'db_table': 'wf_Experience',
            },
        ),
        migrations.CreateModel(
            name='wf_Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('college_batch', models.CharField(max_length=100)),
                ('college_location', models.CharField(max_length=100)),
                ('createby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_talent')),
            ],
            options={
                'db_table': 'wf_Education',
            },
        ),
        migrations.CreateModel(
            name='wf_users',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('usertoken', models.CharField(blank=True, max_length=100, null=True)),
                ('user_profile', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('useremail', models.EmailField(blank=True, max_length=350, null=True)),
                ('password', models.CharField(blank=True, max_length=300, null=True)),
                ('userlogtime', models.CharField(blank=True, max_length=50, null=True)),
                ('userlogkey', models.CharField(blank=True, max_length=50, null=True)),
                ('last_loggedon', models.DateTimeField(blank=True, null=True)),
                ('createdby', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(blank=True, null=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('deleted', models.IntegerField(default=0)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDS_wfapp.wf_rolemenu')),
            ],
            options={
                'db_table': 'wf_users',
            },
        ),
    ]

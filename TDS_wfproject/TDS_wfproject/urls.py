"""
URL configuration for TDS_wfproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from TDS_wfapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    #LOGIN
    path('', views.login_view, name='login_view'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('recruiters_dashboard', views.recruiters_dashboard, name='recruiters_dashboard'),

    #COMPANY
    path('add_company',views.add_company,name='add_company'),
    path('companies/', views.list_company, name='list_company'),
    path('preview_companies/<int:company_id>/', views.preview_company, name='preview_company'),
    # path('companies/<int:company_id>/delete', views.delete_company, name='delete_company'),
    path('delete_company/<int:company_id>', views.delete_company, name='delete_company'),
    path('companies/<int:company_id>/edit', views.edit_company, name='edit_company'),
    #RECRUITERS
    path('list_recruiter',views.list_recruiters,name='list_recruiters'),
    path('add_recruiters',views.add_recruiters,name='add_recruiters'),
    path('edit_recruiters/<int:recruiter_id>',views.edit_recruiters,name='edit_recruiters'),
    path('preview_recruiters/<int:recruiter_id>', views.preview_recruiters, name='preview_recruiters'),
    path('delete_recruiter/<int:recruiter_id>/', views.delete_recruiter, name='delete_recruiter'),

    #JOBS
    path('list_jobs',views.list_jobs,name='list_jobs'),  
    path('add_jobs',views.add_jobs,name='add_jobs'),  
    path('edit_jobs/<int:job_id>',views.edit_jobs,name='edit_jobs'),  
    path('track_jobs',views.track_jobs,name='track_jobs'),  
    path('preview_jobs/<int:job_id>',views.preview_jobs,name='preview_jobs'),  

    #RESUMES
    path('list_meetings',views.list_meetings,name='list_meetings'),  

    #Talent
    path('list_talent',views.list_talent,name='list_talent'),
    path('add_talent',views.add_talent,name='add_talent'),
    path('preview_talent/<int:id>',views.preview_talent,name='preview_talent'),
    path('edit_talent/<int:talent_id>',views.edit_talent,name='edit_talent'),
    path('delete_talent/<int:talent_id>',views.delete_talent,name='delete_talent'),

    #COMPANY PANEL
     path('company_dashboard',views.company_dashboard,name='company_dashboard'), 
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
urlpatterns = [
    path("",views.userlogin,name="login"),
    path("login/",views.userlogin,name="login"),
    path("admin_dashboard/",views.admin,name="admin_dashboard"),
    path("teacher_dashboard/",views.teacher,name="teacher_dashboard"),
    path("student_dashboard/",views.student,name="student_dashboard"),
    path("user_authentication/",views.authentication,name="user_authentication"),
    path("admission_EXPLORE_SCHOOLS/",views.admission,name="admission_EXPLORE_SCHOOLS"),
    path("school_of_computings/",views.school_of_computings,name="school_of_computings"),
    path("AIML_ADMISSION_EXPLORE_SCHOOLS/",views.admission_aiml,name="AIML_ADMISSION_EXPLORE_SCHOOLS"),
    path("Software_Engineering_explore/",views.admission_Software_Engineering,name="Software_Engineering_explore"),
    path("Data_Sciences_explore/",views.admiss_Data_Sciences,name="Data_Sciences_explore"),
    path("admission_cybersecurity/",views.admission_cybersecurity,name="admission_cybersecurity"),
    path("admision_block_techonogly/",views.admision_block_techonogly,name="admision_block_techonogly"),
    path("admission_internet_of_things/",views.admission_internet_of_things,name="admission_internet_of_things"),
    path("admission_cloud_computing/",views.admission_cloud_computing,name="admission_cloud_computing"),
    path("admission_computer_networks/",views.admission_computer_networks,name="admission_computer_networks"),
]

    

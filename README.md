# infludom

Infludom is an Influencer API platform.

A Django API for a casting platform
-Users will be able to create accounts as talents
-add data about themselves
-Casting companies will create accounts as companies and create projects, which will have roles
-Talents will be able to apply for roles
-Companies will be able to see applicants for each role


To install, download the files from Github with the link below:
https://github.com/mcwilton/infludom.git

Create a Python environment

Run with python manage.py runserver

To view the API online, visit the below website address:
http://infludom.pythonanywhere.com/

![image](https://user-images.githubusercontent.com/20909827/188434936-67e43ef4-7e31-4e0a-9d84-91cf8da3c713.png)

Some of the API direct links:

http://infludom.pythonanywhere.com/talent/talent/

http://infludom.pythonanywhere.comtalent/talent<drf_format_suffix:format>

http://infludom.pythonanywhere.com/talent/talent/1/

http://infludom.pythonanywhere.com/talent/talent/<int:pk><drf_format_suffix:format>

http://infludom.pythonanywhere.com/talent/registration/

http://infludom.pythonanywhere.com/talent/registration/<drf_format_suffix:format>

http://infludom.pythonanywhere.com/company/projects/ 

http://infludom.pythonanywhere.com/company/projects/<int:project_id>

http://infludom.pythonanywhere.com/company/applications/

http://infludom.pythonanywhere.com/company/applications/<int:pk>

http://infludom.pythonanywhere.com/company/registration/

http://infludom.pythonanywhere.com/company/roles/

http://infludom.pythonanywhere.com/company/roles/<int:role_name_id>

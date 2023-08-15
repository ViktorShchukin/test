#### Task-Backend-1

In this document i will describe process of the set up and deploying  of my django project. In the end I will describe some usage cases. 

I create django project witch I called test_project for this task. As database I use postgres on https://railway.app. As host service I use https://vercel.com. 

##### set up 

At first we need to set up our project. 

1. To connect  posgres database to our project we need to copy variables of database from  https://railway.app to variable DATABASES inside *test_project/test_project/settings.py* file. 

   ![](/images/DATABASES_variable.jpg)

   Then we need to make migrations by command: **python manage.py makemigrations app1**

   Then migrate by command: **python manage.py migrate**

   

    

2. To deploy project on https://vercel.com we need to make file vercel.json into *test/test_project*  witch contain following settings for vercel: 

   ![](/images/json_for_vercel.jpg)

   

3. make the requirements.txt file if not exist into *test/test_project* by command: **python -m pip freeze > requirements.txt**

4. set the host name into ALLOWED_HOSTS variable into settings.py file 

   ![](/images/ALLOWED_HOSTS_variable.jpg)

   

   
##### deployment 

1.  sign in on vercel.com

2. select Add New and Project

   ![](/images/vercel_1.jpg)

   

3. select git-hub repository with project you want to deploy 

4. click import project 

   ![](/images/vercel_import.jpg)

   

5. set name of the project 

   ![](/images/vercel_name.jpg)

   

6. set as root directory  root of django project. For me it's *test/test_project*

   ![](/images/vercel_root.jpg)

   

7. click on deploy button

##### Usage 

In this app I made custom user model and REST API for it.

My app link is https://viktor-1234.vercel.app

Usage cases:

https://viktor-1234.vercel.app/api-auth/login - for user login

https://viktor-1234.vercel.app/api-auth/loguot - for user logout 

https://viktor-1234.vercel.app/app1/users/ - http-GET for get list of users and http-POST for create new user

https://viktor-1234.vercel.app/app1/users/<int:pk> - http-GET for retrieve user, http-PUT for update user, http-DELETE for delete user
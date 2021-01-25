# Blog-Hosting-Application
Blog Hosting Application using Django , DRF(Django Rest Framework) , HTML , CSS and Javacsript allowing users to register themselves , post blogs written by them and view different blogs by other bloggers in three different categories including Bussiness, Sports and Entertainment apart from that they have a dedicated profile page where they can view and update their various details ,Also has a api to query the database for different blogs written by various users in each category ,update them and delete their respective blogs. 

# Requirements 
`Python 3`
`Django 2.2 `  
`crispy forms`   
`Django rest framework 3.9.3 `  
`messages 2.24 ` 

# Install and Run
## *(Optional)* Create a virtual Environment and activate it with :  
  
`$ python3 -m venv .venv && source .venv/bin/activate`  

## Install the required dependencies  

## Create the database with :  
`$ python3 manage.py makemigrations`  
`$ python3 manage.py makemigrations blog`  
`$ python3 manage.py makemigrations users`  

## Create a Super User with :  
`python3 manage.py createsuperuser`  
  
then run in the developement mode on port 8080 with :  
`python manage.py runserver`  
  
# Available settings to override are :  



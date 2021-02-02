# **Hey Bloggers !! Your one-stop Destination for the Purpose**  
# Blog-Hosting-Application
Blog Hosting Application using Django , DRF(Django Rest Framework) , HTML , CSS  allowing users to register themselves , post blogs written by them and view different blogs by other bloggers in three different categories including Bussiness, Sports and Entertainment apart from that they have a dedicated profile page where they can view and update their various details , Also has a api to query the database for different blogs written by various users in each category ,update them and delete their respective blogs. 

# Requirements 
`Python 3`  
`Django 2.2 `  
`Django crispy forms 1.9.2`   
`Django rest framework 3.9.3 `  
`messages 2.24 `   
`requests 2.24.0`  
`Pillow 8.0.1`  


# Install and Run
## *(Optional)* Create a virtual Environment and activate it with :  
  
`$ python3 -m venv .venv && source .venv/bin/activate`  

## Install the required dependencies in the requirements mentioned  using the command Below   
  
 `pip3 install -r requirements.txt`

## Create the database with :  
`$ python3 manage.py makemigrations`  
`$ python3 manage.py makemigrations blog`  
`$ python3 manage.py makemigrations users`  
`$ python3 manage.py migrate`  

## Create a Super User with :  
`$ python3 manage.py createsuperuser`  
  
  
then run in the developement mode on port 8080 with :  
`$ python manage.py runserver`  
  
# Available settings to override are :  
* `DEBUG` : set the django `DEBUG` option. Defualt `True`.  
* `TIMEZONE` : Default `UTC`. Other examples are : `America/Buenos_Aires` .  
* `LANGUAGE_CODE` : Default `en-us`. Other exmaples are : `es-ar` .   

## Few Screenshots of the running server - 
![alt text](https://github.com/stunn-areeb09/Blog-Hosting-Application/blob/main/screenshots/Screenshot%20(180).png "Index page")
![alt text](https://github.com/stunn-areeb09/Blog-Hosting-Application/blob/main/screenshots/Screenshot%20(181).png "Login Page")
![alt text](https://github.com/stunn-areeb09/Blog-Hosting-Application/blob/main/screenshots/Screenshot%20(182).png "Signed in page with user as areebnew")
![alt text](https://github.com/stunn-areeb09/Blog-Hosting-Application/blob/main/screenshots/Screenshot%20(183).png "Business Blogs listing ")
![alt text](https://github.com/stunn-areeb09/Blog-Hosting-Application/blob/main/screenshots/Screenshot%20(184).png "Profile page of the signedin user")
![alt text](https://github.com/stunn-areeb09/Blog-Hosting-Application/blob/main/screenshots/Screenshot%20(185).png "New blog with title created in Bussiness category")
![alt text](https://github.com/stunn-areeb09/Blog-Hosting-Application/blob/main/screenshots/Screenshot%20(186).png "Register button")
![alt text](https://github.com/stunn-areeb09/Blog-Hosting-Application/blob/main/screenshots/Screenshot%20(187).png "After Registration Redirection")

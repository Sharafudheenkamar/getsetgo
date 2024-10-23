from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.views import View
from .models import UserProfile,Token
from django.contrib.auth import authenticate
from django.contrib import messages
import json
from .form import Clubregistrationform,Eoregistrationform,Schoolregistrationform,Collegeregistrationform
from django.http import HttpResponse

# Create your views here.
class Login(View):
    templates_name = 'administrator/login.html'

    def get(self, request):
        return render(request, "administrator/login.html")

    def post(self, request):
        print("$$$$$$$$$$$$$$$$$$$$$")
        response_dict = {"success": False}
        landing_page_url = {
            "ADMIN": "administrator/viewadministratordashboard",
            "EVENTORGANIZER":"eventorganizer/vieweventorganiserdashboard/",
            "CLUB":"club/viewclubdashboard",     
            # main url l kodutha name specify cheyyanam 
        }

        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, 'username')
        print(password, 'password********')

        user = UserProfile.objects.filter(username=username).first()
        print(user)
        if not user:
            response_dict["reason"] = "No account found for this username, please sign up."
            messages.error(request, response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict["reason"]})

        # Check if the user is inactive
        if not user.is_active:
            response_dict["reason"] = "User is inactive, please contact admin."
            messages.error(request, response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict["reason"]})

        # Check if the user type is pending
        print(user.user_type)
        if user.user_type == "pending":
            response_dict["reason"] = "User is pending, please contact admin."
            messages.error(request, response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict["reason"]})

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user:
            session_dict = {"real_user": user.id}
            token, created = Token.objects.get_or_create(
                user=user, defaults={"session_dict": json.dumps(session_dict)}
            )

            request.session["data"] = {
                "user_id": user.id,
                "user_type": user.user_type,
                "token": token.key,
                "username": user.username,
                "status": user.is_active,
            }
            print(user)
            print(user.user_type)
            print(f"4444444444444444User Type: {user.user_type}")
            print("session",request.session["data"]["user_id"])
            print(f"77777777777777777Landing Page URLs: {landing_page_url}")
            return redirect(landing_page_url[user.user_type])
        else:
            response_dict["reason"] = "Invalid credentials."
            messages.error(request, response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict["reason"]})
        
class Clubregistration(View):
    def get (self,request):
        return render(request,'administrator/clubregistration.html')
    def post(self,request):
        form=Clubregistrationform(request.POST)
        if form.is_valid():

            try:
                # Check if username already exists
                if UserProfile.objects.filter(username=request.POST['username']).exists():
                    return HttpResponse('''<script>alert("Username already exists! Please choose a different one.");window.location="{% url 'CameraManreg' %}"</script>''')
                
                # Create a new user
                login_instance = UserProfile.objects.create_user(
                    user_type='CLUB',
                    username=request.POST['username'],
                    password=request.POST['password'],
                    is_active=False
                )
                
                # Save the shop details with reference to the created user
                reg_form = form.save(commit=False)
                reg_form.login_id = login_instance
                reg_form.save()

                return HttpResponse('''<script>alert("Registered successfully!");window.location="{% url 'CameraManreg' %}"</script>''')
            
            except IntegrityError as e:
                # Print the exact error for debugging
                print(f"IntegrityError: {e}")
                return HttpResponse('''<script>alert("An error occurred while processing your request. Please try again.");window.location="{% url 'CameraManreg' %}"</script>''')
        else:
            # Print form errors for debugging
            print("Form is not valid. Errors:", form.errors)
            return HttpResponse('''<script>alert("Form submission failed. Please check the form and try again.");window.location="{% url 'CameraManreg' %} "</script>''')
class Eoregistration(View):
    def get (self,request):
        return render(request,'administrator/eoregistration.html')
    def post(self,request):
        form=Eoregistrationform(request.POST)
        if form.is_valid():

            try:
                # Check if username already exists
                if UserProfile.objects.filter(username=request.POST['username']).exists():
                    return HttpResponse('''<script>alert("Username already exists! Please choose a different one.");window.location="{% url 'CameraManreg' %}"</script>''')
                
                # Create a new user
                login_instance = UserProfile.objects.create_user(
                    user_type='EVENTORGANIZER',
                    username=request.POST['username'],
                    password=request.POST['password'],
                    is_active=False
                )
                
                # Save the shop details with reference to the created user
                reg_form = form.save(commit=False)
                reg_form.login_id = login_instance
                reg_form.save()

                return HttpResponse('''<script>alert("Registered successfully!");window.location="{% url 'CameraManreg' %}"</script>''')
            
            except IntegrityError as e:
                # Print the exact error for debugging
                print(f"IntegrityError: {e}")
                return HttpResponse('''<script>alert("An error occurred while processing your request. Please try again.");window.location="{% url 'CameraManreg' %}"</script>''')
        else:
            # Print form errors for debugging
            print("Form is not valid. Errors:", form.errors)
            return HttpResponse('''<script>alert("Form submission failed. Please check the form and try again.");window.location="{% url 'CameraManreg' %} "</script>''')        

class Schoolregistration(View):
    def get (self,request):
        return render(request,'administrator/eoregistration.html')
    def post(self,request):
        form=Schoolregistrationform(request.POST)
        if form.is_valid():

            try:
                # Check if username already exists
                if UserProfile.objects.filter(username=request.POST['username']).exists():
                    return HttpResponse('''<script>alert("Username already exists! Please choose a different one.");window.location="{% url 'CameraManreg' %}"</script>''')
                
                # Create a new user
                login_instance = UserProfile.objects.create_user(
                    user_type='SCHOOL',
                    username=request.POST['username'],
                    password=request.POST['password'],
                    is_active=False
                )
                
                # Save the shop details with reference to the created user
                reg_form = form.save(commit=False)
                reg_form.login_id = login_instance
                reg_form.save()

                return HttpResponse('''<script>alert("Registered successfully!");window.location="{% url 'CameraManreg' %}"</script>''')
            
            except IntegrityError as e:
                # Print the exact error for debugging
                print(f"IntegrityError: {e}")
                return HttpResponse('''<script>alert("An error occurred while processing your request. Please try again.");window.location="{% url 'CameraManreg' %}"</script>''')
        else:
            # Print form errors for debugging
            print("Form is not valid. Errors:", form.errors)
            return HttpResponse('''<script>alert("Form submission failed. Please check the form and try again.");window.location="{% url 'CameraManreg' %} "</script>''')                
        
class Collegeregistration(View):
    def get (self,request):
        return render(request,'administrator/eoregistration.html')
    def post(self,request):
        form=Collegeregistrationform(request.POST)
        if form.is_valid():

            try:
                # Check if username already exists
                if UserProfile.objects.filter(username=request.POST['username']).exists():
                    return HttpResponse('''<script>alert("Username already exists! Please choose a different one.");window.location="{% url 'CameraManreg' %}"</script>''')
                
                # Create a new user
                login_instance = UserProfile.objects.create_user(
                    user_type='COLEEGE',
                    username=request.POST['username'],
                    password=request.POST['password'],
                    is_active=False
                )
                
                # Save the shop details with reference to the created user
                reg_form = form.save(commit=False)
                reg_form.login_id = login_instance
                reg_form.save()

                return HttpResponse('''<script>alert("Registered successfully!");window.location="{% url 'CameraManreg' %}"</script>''')
            
            except IntegrityError as e:
                # Print the exact error for debugging
                print(f"IntegrityError: {e}")
                return HttpResponse('''<script>alert("An error occurred while processing your request. Please try again.");window.location="{% url 'CameraManreg' %}"</script>''')
        else:
            # Print form errors for debugging
            print("Form is not valid. Errors:", form.errors)
            return HttpResponse('''<script>alert("Form submission failed. Please check the form and try again.");window.location="{% url 'CameraManreg' %} "</script>''')                
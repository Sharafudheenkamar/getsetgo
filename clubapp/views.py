from django.shortcuts import render,redirect
from django.views import View
from .form import Addalerform

# Create your views here.
class Addalert(View):
    def get(self,request):
        return render(request,'addalert.html')
    def post(self,request):
        form=Addalerform(request.POST)
        if form.is_valid():
            c=form.save(commit=False)
            c.login_id=request.sessiion["data"]["user_id"]
            c.save()
            return redirect('viewalert')
class Viewalert(View):
    def get(self,request):
        al=Emergencyalerts.object.all()
        return render(request,'viewemergencyalerts',{'al':al})
class Editalert(View):
    def get(self,request):
        al=Emergencyalerts.objects.get(id=id)
        

from django.shortcuts import render,redirect
from django.views import View
from clubapp.models import Clubprofile
from schoolapp.models import Schoolprofile
from collegeapp.models import Collegeprofile
from login.form import *

# Create your views here.
class Viewadminsistratordashoard(View):
    def get(self,request):
        return render (request,'administrator/administratordashboard.html')
class Viewusers(View):
    def get(self,request):
        return render(request,'administrator/adminviewusers.html')
    

class Viewclub(View):
    def get(self,request):
        c=Clubprofile.objects.all()
        return render (request,'viewclubs.html',{'c':c})
class Viewschool(View):
    def get(self,request):
        s=Schoolprofile.objects.all()
        return render (request,'viewschools.html',{'s':s})
class Viewcollege(View):
    def get(self,request):
        col=Collegeprofile.objects.all()
        return render (request,'viewcolleges.html',{'col':col})

class Editclub(View):
    def get(self,request,id):
        c=Clubprofile.objects.get(id=id)
        return render(request,"editclub.html",{'c':c})
    def post(self,request,id):
        c=Clubprofile.objects.get(id=id)
        form=Clubregistrationform(request.POST,instance=c)
        if form.is_valid():
            form.save()
            return redirect('viewclub')

class Editcollege(View):
    def get(self,request,id):
        col=Collegeprofile.objects.get(id=id)
        return render(request,"editcollege.html",{'col':col})
    def post(self,request,id):
        col=Collegeprofile.objects.get(id=id)
        form=Collegeregistrationform(request.POST,instance=col)
        if form.is_valid():
            form.save()
            return redirect('viewcollege')
class Editschool(View):
    def get(self,request,id):
        sch=Schoolprofile.objects.get(id=id)
        return render(request,"editschool.html",{'sch':sch})
    def post(self,request,id):
        col=Collegeprofile.objects.get(id=id)
        form=s=Schoolregistrationform(request.POST,instance=col)
        if form.is_valid():
            form.save()
            return redirect('viewschool')
class Deleteclub(View):
    def get(self,request,id):
        c=Clubprofile.objects.get(id=id)
        c.delete()
        return redirect('viewclub')
class Deleteschool(View):
    def get(self,request,id):
        c=Schoolprofile.objects.get(id=id)
        c.delete()
        return redirect('viewschool')
class Deletecollege(View):
    def get(self,request,id):
        c=Collegeprofile.objects.get(id=id)
        c.delete()
        return redirect('viewcollege')
class Verifyclub(View):
    def get (self,request,id):
        c=Collegeprofile.objects.get(id=id)
        c.login_id.status='ACTIVE'
        c.save()
        return redirect('viewclub')
class Verifycollege(View):
    def get (self,request,id):
        c=Collegeprofile.objects.get(id=id)
        c.login_id.status='ACTIVE'
        c.save()
        return redirect('viewcollege')
class Verifyschool(View):
    def get (self,request,id):
        c=Collegeprofile.objects.get(id=id)
        c.login_id.status='ACTIVE'
        c.save()
        return redirect('viewschool')

        

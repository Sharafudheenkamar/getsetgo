from django.shortcuts import render
from django.views import View

# Create your views here.
class Viewadminsistratordashoard(View):
    def get(self,request):
        return render (request,'administrator/administratordashboard.html')
class Viewusers(View):
    def get(self,request):
        return render(request,'administrator/adminviewusers.html')
    

class Viewclubs(View):
    def get(self,request):
        c=Clubprofile.objects.all()
        return render (request,'viewclubs.html',{'c':c})
class Viewschools(View):
    def get(self,request):
        s=Schoolprofile.objects.all()
        return render (request,'viewschools.html',{'s':s})
class Viewcolleges(View):
    def get(self,request):
        col=Collegesprofile.objects.all()
        return render (request,'viewcolleges.html',{'col':col})
    
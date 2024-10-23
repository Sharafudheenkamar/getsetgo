from django.forms import ModelForm
from clubapp.models import Clubprofile
from eventapp.models import Eventprofile
from schoolapp.models import Schoolprofile
from collegeapp.models import Collegeprofile


class Clubregistrationform(ModelForm):
    class Meta:
        model = Clubprofile
        fields=['club_id','clubname','address','phone_no','email','club_owner']


class Eoregistrationform(ModelForm):
    class Meta:
        model = Eventprofile
        fields = ['eo_id','eoname','address','phone_no','email']
class Schoolregistrationform(ModelForm):
    class Meta:
        model = Schoolprofile
        fields=['school_id','schoolname','address','phone_no','email']

class Collegeregistrationform(ModelForm):
    class Meta:
        model = Collegeprofile
        fields=['college_id','collegename','address','phone_no','email']
from django.forms import ModelForm
from .models import Emergencyalerts

class Addalerform(ModelForm):
    class Meta:
        model=Emergencyalerts
        fields=['alert','alertdate','alerttime']
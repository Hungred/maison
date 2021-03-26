from django.forms import ModelForm
from .models import Worksche

class WorkscheForm(ModelForm):
    class Meta:
        model = Worksche
        fields = '__all__'
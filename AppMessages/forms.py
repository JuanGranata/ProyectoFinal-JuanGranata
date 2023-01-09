from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone

class MsgForm(forms.ModelForm):
    date = forms.DateTimeField(initial=timezone.now)
	
    class Meta:
        model = Msg
        fields = ('userto', 'userfrom','subject', 'text')
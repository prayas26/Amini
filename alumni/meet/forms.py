from django import forms
from .models import *
import formencode

class AlumnusForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Alumnus
        fields = [
			"enrollment_no",
			"name",
            "gender",
            "dob",
            "contactno",
            "fblink",
            "linkedin",
            "email",
            "branch",
            "batch",
            "placed",
            "image",
		]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["answer",]

class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggest
        fields = [
            "sname",
            "semail",
            "smessage",
        ]

class ChangeForm(forms.ModelForm):
    class Meta:
        model = Change
        fields = [
            "cname",
            "cbatch",
            "cemail",
            "ccontact",
            "cdetail",
        ]
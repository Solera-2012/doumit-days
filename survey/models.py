from django import forms
from django.forms import ModelForm
from django.db import models

class Family(models.Model):
    rep_name = models.CharField("Name",max_length=120)
    num_members = models.PositiveSmallIntegerField("# of family members")
    email = models.CharField("Email", max_length=120)
    comments = models.TextField(default="")



    CHOICES=[('Y','Yes'),('N','No'),('M','Maybe')]
    rsvp = models.CharField(max_length=1,choices=CHOICES, default="")

    def __str__(self):
        return "%s (%s)"%(self.rep_name, self.num_members)

class FamilyForm(ModelForm):
	class Meta:
		model = Family
		fields = ['rep_name', 'num_members', 'email', 'rsvp', 'comments']


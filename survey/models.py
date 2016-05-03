from django import forms
from django.forms import ModelForm
from django.db import models

class Family(models.Model):
	rep_name = models.CharField("Representative's name",max_length=120)
	num_members = models.IntegerField("Number of family members")
	email = models.CharField("Email address", max_length=120)
	
	def __str__(self):
		return "%s (%s)"%(self.rep_name, self.num_members)

class FamilyForm(ModelForm):
	class Meta:
		model = Family
		fields = ['rep_name', 'num_members', 'email']

class Choice(models.Model):
	name = models.CharField(max_length=45, default="NA")
	details = models.CharField(max_length=140)
	date_start = models.DateField()
	date_end = models.DateField()

	def __str__(self):
		return "%s (%s to %s)"%(self.name, self.date_start, self.date_end)

class Score(models.Model):
	family = models.ForeignKey(Family, on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE)	
	score  = models.IntegerField(default=0)
	result = models.CharField(max_length=32,default="cant")

	def __str__(self):	
		return "%s -- %s -- %s"%(self.family, self.choice, self.result)


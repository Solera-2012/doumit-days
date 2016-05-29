from django import forms
from django.forms import ModelForm, Textarea, EmailInput, NumberInput
from django.db import models






from datetime import date

def get_date_choices():
    date_options = [(date(2018,7,28), date(2018,8,5)),
                   (date(2018,8,5), date(2018,8,12))]
    date_options_str = [ "%s - %s"%(option[0].strftime('%b %d'), 
                                  option[1].strftime('%b %d')) 
                                  for option in date_options]
    DATE_CHOICES = ((1,date_options_str[0]), 
                   (2,date_options_str[1]), 
                   (3, "No preference"))

    return DATE_CHOICES


class Family(models.Model):
    rep_name = models.CharField(
        "Name",
        max_length=120
    )
    
    num_members = models.PositiveSmallIntegerField(
        "# of family participants"
    )
    
    num_rooms = models.PositiveSmallIntegerField(
        "# of rooms requested"
    )
    
    email = models.CharField(
        "Email", 
        max_length=120
    )

    comments = models.TextField(
        default=""
    )

    RSVP_CHOICES=[('Y','Yes'),('N','No')]
    rsvp = models.CharField(
        max_length=1,
        choices=RSVP_CHOICES, 
        default=""
    )
   
    date_preference = models.CharField(
        max_length=1, 
        choices=get_date_choices(), 
        default="No preference"
    )



    def __str__(self):
        return "%s (%s)"%(self.rep_name, self.num_members)

class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = ['rep_name', 'rsvp', 'date_preference','num_rooms', 'num_members', 'email',  'comments']

        
        widgets = {
            'comments': Textarea(attrs={'rows':3}),
            'email': EmailInput(),
            'num_rooms': NumberInput(),
        }











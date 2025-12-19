from django import forms
from django.core.exceptions import ValidationError
from datetime import date

GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female'),
    ('O','Other'),
]

SKILL_CHOICES = [
    ('python', 'Python'),
    ('django', 'Django'),
    ('sql', 'SQL'),
]

class Contact(forms.Form):
    full_name = forms.CharField(
        label="Name",
        max_length=100,
        min_length=5,
        strip=True,
        help_text="Enter Your Name",
    )
    bio = forms.CharField(
        label="Bio",
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder":'Tell us about yourself...',
            "rows":"3"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'password-field'})
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'confirm_password', 'class': 'password-field'})
    )
    age = forms.IntegerField(
        min_value=18,
        max_value=35,
    )
    salary = forms.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    rating = forms.FloatField(
        min_value=0.0,
        max_value=5.0
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={
            "type":'date',
        })
    ) 
    apoinment_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs= {
                "type":"time"
            }
        )
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect()
    )

    skills = forms.MultipleChoiceField(
        choices=SKILL_CHOICES,
        widget=forms.CheckboxSelectMultiple()
    )

    profile_pic = forms.ImageField()
    document = forms.FileField()


    def clean_full_name(self):
        name = self.cleaned_data['full_name']

        if len(name.split())<2:
            raise ValidationError("Full name must be contains at least 2 words")
        
        return name
    
    def clean_bio(self):
        bio = self.cleaned_data['bio']

        if len(bio.split())<5:
            raise ValidationError("Bio is too short it must be contain at least 5 words !!")
        
        return bio
    
    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']

        if birth_date > date.today():
            raise ValidationError("Birth date can't be in the future")

        return birth_date
    
    def clean_apoinment_time(self):
        apoinment_time = self.cleaned_data['apoinment_time']

        if(apoinment_time.hour<9 or apoinment_time.hour>18):
            raise ValidationError("Appointment time must be between 9:00 AM and 6:00 PM.")
        
        return apoinment_time

    def clean_profile_pic(self):
        image = self.cleaned_data['profile_pic']

        if image.size >100*1024:
            raise ValidationError("Image file too large . it must be under 100 KB")

        return image
    
    def clean_document(self):
        document = self.cleaned_data['document']
        ext = document.name.split('.')
        if(ext[-1] != 'pdf'):
            raise ValidationError("Document must be pdf")
        return document

    def clean(self):
        cleaed_data =  super().clean()

        password = cleaed_data.get('password')
        confirm_password = cleaed_data.get('confirm_password')

        if password!=confirm_password:
            self.add_error("confirm_password","Password does not match")
        
        return cleaed_data


# built in validator 

# from django import forms
# from django.core.exceptions import ValidationError
# from django.core.validators import (
#     MinValueValidator, 
#     MaxValueValidator, 
#     MinLengthValidator, 
#     FileExtensionValidator,
#     RegexValidator
# )
# from datetime import date
# import os

# GENDER_CHOICES = [
#     ('M', 'Male'),
#     ('F', 'Female'),
#     ('O', 'Other'),
# ]

# SKILL_CHOICES = [
#     ('python', 'Python'),
#     ('django', 'Django'),
#     ('sql', 'SQL'),
#     ('js', 'JavaScript'),
# ]

# class Contact(forms.Form):
#     full_name = forms.CharField(
#         label="Name", 
#         strip=True,
#         help_text="Enter Your Name",
#         
#         validators=[
#             MinLengthValidator(5, message="Name must be at least 5 characters long.")
#         ]
#     )
    
#     bio = forms.CharField(
#         label="Bio", 
#         required=False,
#         widget=forms.Textarea(attrs={"placeholder": 'Tell us about yourself...', "rows": "3"}),
#        
#         validators=[
#             MinLengthValidator(10, message="Bio is too short. Please write at least 10 characters.")
#         ]
#     )
    
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'password-field'}),
#         validators=[
#             MinLengthValidator(8, message="Password must be at least 8 characters long.")
#         ]
#     )
    
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'password-field'})
#     )
    
#     age = forms.IntegerField(
#         validators=[
#             MinValueValidator(18, message="You must be at least 18 years old."),
#             MaxValueValidator(60, message="Age cannot be more than 60.")
#         ]
#     )
    
#     salary = forms.DecimalField(
#         max_digits=12, 
#         decimal_places=2,
#         validators=[
#             MinValueValidator(0, message="Salary cannot be negative.")
#         ]
#     )
    
#     rating = forms.FloatField(
#         validators=[
#             MinValueValidator(0.0),
#             MaxValueValidator(5.0)
#         ]
#     )
    
#     birth_date = forms.DateField(
#         widget=forms.DateInput(attrs={"type": 'date'})
#     )
    
#     appointment_time = forms.TimeField(
#         widget=forms.TimeInput(attrs={"type": "time"})
#     )
    
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
#     skills = forms.MultipleChoiceField(choices=SKILL_CHOICES, widget=forms.CheckboxSelectMultiple())
    
#     profile_pic = forms.ImageField()
    
#    
#     document = forms.FileField(
#         validators=[
#             FileExtensionValidator(allowed_extensions=['pdf'], message="Only PDF files are allowed.")
#         ]
#     )



#     def clean_birth_date(self):
#         dob = self.cleaned_data['birth_date']
#         if dob > date.today():
#             raise ValidationError("Birth date cannot be in the future.")
#         return dob

#     def clean_appointment_time(self):
#         time = self.cleaned_data['appointment_time']
#         if time.hour < 9 or time.hour > 18:
#             raise ValidationError("Appointment time must be between 9:00 AM and 6:00 PM.")
#         return time

#     def clean_skills(self):
#         skills = self.cleaned_data['skills']
#         if len(skills) < 2:
#             raise ValidationError("Please select at least 2 skills.")
#         return skills
    
#     def clean_profile_pic(self):
#         image = self.cleaned_data.get('profile_pic')
#         if image:
#             if image.size > 2 * 1024 * 1024:
#                 raise ValidationError("Image file too large ( > 2mb ).")
#         return image

#     def clean(self):
#         cleaned_data = super().clean()
        
#         # Password Matching
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')

#         if password and confirm_password:
#             if password != confirm_password:
#                 self.add_error("confirm_password", "Password does not match")

#         return cleaned_data
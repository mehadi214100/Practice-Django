from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator,MinValueValidator


CATEGORY_CHOICES = [
    ('f','Frontend'),
    ('b','Backend'),
    ('a','AI'),
    ('s','Server'),
]
SKILLS_CHOICES = [
    ('html','HTML'),
    ('css','CSS'),
    ('tailwind','Tailwind'),
    ('python','Python'),
    ('.net','.NET'),
    ('mern','MERN'),
]

class HackathonRegistrationForm(forms.Form):
    full_name = forms.CharField(
        label="Full Name" ,
        widget=forms.TextInput(attrs={
            'placeholder':"Enter your legal name ",
        })
        )
    email = forms.EmailField()
    website = forms.URLField(help_text="Enter you Portfolio link",required=False)
    age = forms.IntegerField(
        validators=[MaxValueValidator(35,'max age can be 35'),MinValueValidator(18,'min age can 18')]
    )
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.RadioSelect()
       )
    skills = forms.MultipleChoiceField(
        required=False,
        choices=SKILLS_CHOICES,
        widget=forms.CheckboxSelectMultiple()
    )
    team = forms.BooleanField(label="Joining as Team",required=False)
    team_name = forms.CharField(required=False)
    arrival_time = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={
            'type':'datetime-local'
        }
    ))
    salary_expectation = forms.DecimalField(max_digits=10,decimal_places=2)
    resume = forms.FileField()
    profile_image =forms.ImageField()
    agree_terms = forms.BooleanField(label="Are you agree our terms & conditions")
    referral_code = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'password',
        }
    ))


    def clean_email(self):
        email = self.cleaned_data["email"]
        if email.split('@')[-1]!='gmail.com':
            raise ValidationError("Email must be @gmail.com domain !!!")
        return email
    
    def clean(self):
        data = super().clean()
        team = data.get('team')
        team_name = data.get('team_name')
        if team and len(team_name)==0:
            self.add_error('team_name','Please enter your team name')
            raise ValidationError("Please enter your team name")
        
        resume = data.get('resume')
        if resume:
            ext = resume.name.split('.')[-1].lower()
            if ext != 'pdf':
                self.add_error('resume', 'Please upload a PDF file')
                raise ValidationError("Please upload a PDF file")

        return data

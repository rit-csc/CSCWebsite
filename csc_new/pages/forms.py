
from django import forms

MAILING_LIST_CHOICES = [
    ('yes', 'Yes!'),
    ('no', 'No thanks')
]

class SignInForm(forms.Form):
    email = forms.EmailField(label='What is your RIT (or preferred) email address?')
    mailinglist = forms.ChoiceField(choices=MAILING_LIST_CHOICES, initial='yes', widget=forms.RadioSelect, label='Would you like to be added to our announcements mailing list?')




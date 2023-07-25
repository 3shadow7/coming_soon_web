from django import forms
from .models import Subscriber, contact

from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper



class SubscriberForm(forms.ModelForm):
    email = forms.CharField(
        label='',
        min_length=0,
        max_length=500,
        validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message="put a valid email address !")],
      required = True,
        widget=forms.TextInput(attrs={'placeholder':'Email',
        "style":"font-size:1em; border-radius: 0.5em;  ",}),
        )
    class Meta:
        model = Subscriber
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.label_class = "fs-3 w-auto"

class ContactForm(forms.ModelForm):
    
    name = forms.CharField(
        label="",
        min_length=2,
        max_length=500,
        validators= [RegexValidator(r'^[a-zA-Z-ء-ي ]*$',message="only letters is allowed !")],
        widget=forms.TextInput(attrs={'placeholder':'Name',
        "style":"font-size:1.3em; border-radius: 0.5em; box-sizing: border-box;resize: none;  "
        }),
        )
        
    email = forms.CharField(
        label='',
        min_length=0,
        max_length=500,
        validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message="put a valid email address !")],
      required = False,
        widget=forms.TextInput(attrs={'placeholder':'Email',
        "style":"font-size:1.3em; border-radius: 0.5em;  "}),
        )

    message = forms.CharField(
        label="",
        min_length=0,
        max_length=20000,
        widget=forms.Textarea(attrs={'placeholder':'Message',
        "style":"font-size:1.3em; border-radius: 0.5em;  ",
        "rows" : 5,
        }),
        )
    
    class Meta:
        model = contact
        fields = ["name","email","message",]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.label_class = "fs-3 w-auto"
    
        
            
            

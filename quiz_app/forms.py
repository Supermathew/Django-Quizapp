from quiz_app.models import Contact,Usersubmitted
from django.forms   import ModelForm 




class Contactform(ModelForm):
    class Meta:
        model= Contact
        fields =['username','email','message']


class userres(ModelForm):
    class Meta:
        model=Usersubmitted
        fields=['question','user','rightans']
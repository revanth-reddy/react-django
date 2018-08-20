from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','name','mobile_no','email','dp','cell','year','post')
        labels = {
            'mobile_no': _('Mobile'),
            'dp': _('Your Image'),
        }
        help_texts = {
            'password': None}
        error_messages = {
            'name': {
                'max_length': _("Name is too long."),
            },
            'mobile_no':{
            	'max_length':_("Invalid mobile number"),
            }
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username','name','mobile_no','email','dp','cell','year','post')


# class ProfilePictureForm(ModelForm):
#     class Meta:
#         model = Avatar
#         fields = ('avatar',)

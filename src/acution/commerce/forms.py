from django import forms
from src.acution.commerce.models import *


class MemberForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if not password2 == password1:
            raise forms.ValidationError('not match')
        return password1

    def save(self, commit=True):
        user = super(MemberForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class AddGoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['title', 'description', 'category', 'city', 'owner_price']


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['amount']

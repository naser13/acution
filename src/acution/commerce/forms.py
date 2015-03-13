from django import forms
from acution.commerce.models import *


class MemberForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 1:
            raise forms.ValidationError('نمیتواند خالی باشد.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 1:
            raise forms.ValidationError('نمیتواند خالی باشد.')
        return last_name

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


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Member
        fields = ['username', 'password']

    def clean_username(self):
        first_name = self.cleaned_data['username']
        if len(first_name) < 1:
            raise forms.ValidationError('نمیتواند خالی باشد.')
        return first_name

    def clean_password(self):
        last_name = self.cleaned_data['password']
        if len(last_name) < 1:
            raise forms.ValidationError('نمیتواند خالی باشد.')
        return last_name


class AddGoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['title', 'description', 'category']

    # def clean_title(self):
    #     title = self.clean_data['title']
    #     if len(title) < 1:
    #         raise forms.ValidationError("نمیتواند خالی باشد")
    #     return title
    #
    # def clean_comments(self):
    #     comment = self.clean_data['description']
    #     if len(comment) < 1:
    #         raise forms.ValidationError('نمیتواند خالی باشد')
    #     return comment



class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields =['amount']

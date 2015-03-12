from django import forms
from acution.commerce.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 1:
            raise forms.ValidationError('نمیتواند خالی باشد.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name)<1:
            raise forms.ValidationError('نمیتواند خالی باشد.')
        return last_name
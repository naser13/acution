from django.forms import ModelForm
from acution.commerce.models import Member


class MemberForm(ModelForm):
    class Meta:
        model = Member
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm


class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

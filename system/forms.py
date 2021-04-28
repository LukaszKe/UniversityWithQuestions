from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from system.models import Student
from django.db import transaction
from django.forms import ModelForm
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'name',)

class CandidateSignUpForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_candidate = True
        if commit:
            user.save()
        return user

class StudentSignUpForm(CustomUserCreationForm):

    class Meta(CustomUserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        # CHANGED: removed 'student-only' convenience forms below; keep base form
        fields = ['username', 'email', 'phone', 'user_type', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'emergency_contact', 'profile_picture']


# ADDED: StudentRegistrationForm - simplified registration form for students.
# This hides the user_type choice from the form so the view can force
# user_type='student' when creating the user.
class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    student_id = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'student_id', 'password1', 'password2']
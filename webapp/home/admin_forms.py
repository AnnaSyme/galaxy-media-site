"""Forms for managing generic content."""

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User, Notice


class UserCreationForm(forms.ModelForm):
    """Create new user.

    Includes all the required fields, plus a repeated password.
    """

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """Update user.

    Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()
    password1 = forms.CharField(
        label='Update Password',
        widget=forms.PasswordInput,
        required=False,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class NoticeAdminForm(forms.ModelForm):
    """Update and create Notices.

    Make the body widget bigger.
    """

    class Meta:
        """Form metadata."""

        model = Notice
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 30,
                'cols': 120,
            }),
            'short_description': forms.Textarea(attrs={
                'rows': 6,
                'cols': 80,
            }),
        }
        fields = '__all__'

    def clean(self):
        """Clean form data."""
        data = self.cleaned_data
        if data['notice_class'] == 'none':
            data['static_display'] = False
            data['title'] = ''
            data['display_title'] = False
            data['short_description'] = ''
            data['material_icon'] = ''
        else:
            for x in ('title', 'short_description', 'body'):
                self.require(x)

        return data

    def clean_short_description(self):
        """Clean short description."""
        description = self.cleaned_data['short_description']
        if not description:
            return description
        if '</a>' in description:
            self.add_error(
                'short_description',
                (
                    'Please remove <a> tags as this creates a confusing user'
                    ' experience (link within link).'
                ),
            )
        return description

    def require(self, field):
        """Require a field."""
        if not self.cleaned_data[field]:
            self.add_error(field, 'This field is required.')

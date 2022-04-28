from django import forms

from .models import aplly_job, job


class applyjob(forms.ModelForm):
    class Meta:
        model = aplly_job
        fields = ['name', 'email', 'website', 'cv', 'about']


class jobform(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('owner', 'slug')

from django import forms

from portal.fields import JobPostingModelChoiceField
from portal.models import JobPosting


class ReferralForm(forms.Form):
    referral_name = forms.CharField(label='Referral Name', max_length=100)
    referral_email = forms.CharField(label='Referral Email', max_length=100)
    job_postings = JobPostingModelChoiceField(queryset=JobPosting.objects.all().order_by('title'))

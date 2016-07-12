from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import JobPosting, Referral
from .forms import ReferralForm


@login_required(login_url='/portal/login/')
def index(request):
    jobs_list = JobPosting.objects.all().order_by('-pub_date')
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral = Referral(referral_name=form.cleaned_data['referral_name'],
                                referral_email=form.cleaned_data['referral_email'],
                                job_posting=form.cleaned_data['job_postings'])
            referral.save()
            return HttpResponseRedirect('/portal/')
    else:
        form = ReferralForm()
    return render(request, 'portal/index.html', {'referral_form': form, 'jobs_list': jobs_list})

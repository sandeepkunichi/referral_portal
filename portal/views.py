from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

from .models import JobPosting, Referral
from .forms import ReferralForm


@login_required(login_url='/portal/login/')
def index(request):
    latest_question_list = JobPosting.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral = Referral(referral_name=form.cleaned_data['referral_name'],
                                referral_email=form.cleaned_data['referral_email'],
                                job_posting=form.cleaned_data['job_postings'],
                                status='WAITING')

            referral.save()
            return HttpResponseRedirect('/portal/')
    else:
        form = ReferralForm()
    return render_to_response('portal/index.html', context=context, dictionary={'referral_form': form})


@login_required(login_url='portal/login/')
def list_jobs(request):
    jobs_list = JobPosting.objects.all().order_by('-pub_date')
    template = loader.get_template('portal/jobs.html')
    context = {
        'jobs_list': jobs_list,
    }
    return HttpResponse(template.render(context, request))

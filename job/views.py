from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse

from .form import applyjob, jobform
from .models import job
from .job_filter import JobFilter


# Create your views here.


def job_liste(request):
    job_liste = job.objects.all()

    myfilter=JobFilter(request.GET , queryset=job_liste )
    job_liste=myfilter.qs


    paginator = Paginator(job_liste, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj , 'myfilter':myfilter}
    return render(request, 'job/job_list.html', context)


def job_detalis(request, slug):
    job_detalis = job.objects.get(slug=slug)

    if request.method == 'POST':
        form = applyjob(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detalis
            myform.save()

    else:
        form = applyjob()

    context = {'job': job_detalis, 'form': form}
    return render(request, 'job/job_datels.html', context)

@login_required
def add_job(request):
    if request.method == 'POST':
        form = jobform(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect( reverse('jobs:job_list'))

    else:
        form = jobform()
    return render(request, 'job/add_job.html', {'form1': form})

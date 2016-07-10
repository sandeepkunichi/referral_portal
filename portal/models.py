from __future__ import unicode_literals

from django.db import models

# Create your models here.


class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    job_description = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published')


class Referral(models.Model):
    STATUS = (
        ('WAITING', 'WAITING'),
        ('ACCEPTED', 'ACCEPTED')
    )
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    referral_name = models.CharField(max_length=200)
    referral_email = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS, default='WAITING')

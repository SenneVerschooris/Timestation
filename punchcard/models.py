from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Department(models.Model):
    name= models.CharField(max_length=1024)

class JobRole(models.Model):
    title = models.CharField(max_length=1024)

class EmployeeProfile(models.Model):
    """ Employee model """
    GENDER_CHOICES = (('M', _('Male')), ('F', _('Female')), ('O', _('Other')))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(blank=True, null=True)
    email_address = models.EmailField(max_length=254, blank=True, unique=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)
    job_role = models.ForeignKey(JobRole, blank=True, null=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,blank=True, null=True, on_delete=models.CASCADE)
    line_manager = models.ForeignKey(User, blank=True, null=True,related_name="%(app_label)s_%(class)s_line_manager", on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s"%self.user

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile, new = EmployeeProfile.objects.get_or_create(user=inter)

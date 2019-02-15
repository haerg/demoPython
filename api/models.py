from django.db import models
from django.contrib.auth.models import User

# https://docs.djangoproject.com/en/2.1/topics/auth/default/#changing-passwords


class FsInstitution(models.Model):
    TYPE_CHOICES = (
        ('LP', 'LP'),
        ('GP', 'GP'),
    )
    parent = models.ForeignKey('self', blank=True, null=True, related_name='owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50, null=True)
    contact_email = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=50, default=None, null=True, choices=TYPE_CHOICES)
    signed_nda = models.BooleanField(default=False)
    needs_to_sign = models.BooleanField(default=True)
    is_investor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, through='FsInstitutionUser', related_name='institution_user')

    class Meta:
        verbose_name = 'Institution'
        db_table = 'fs_institution'


class FsInstitutionUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(FsInstitution, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Institution User'
        db_table = 'fs_institution_user'


class FsInstitutionNotification(models.Model):
    institution = models.ForeignKey(FsInstitution, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=16, default='notification')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Institution Notification'
        db_table = 'fs_institution_notification'
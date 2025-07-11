from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERADMIN = 'superadmin'
        ADMIN = 'admin'
        TEACHER = 'teacher'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.TEACHER)

class Article(models.Model):
    class Status(models.TextChoices):
        SUBMITTED = 'submitted', 'Submitted'
        IN_REVIEW = 'in_review', 'In Review'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        ARCHIVED = 'archived', 'Archived'

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': User.Role.TEACHER})
    pdf = models.FileField(upload_to='articles/')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SUBMITTED)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='reviewed_articles')

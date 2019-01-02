"""
Models for Blog application.
"""
from django.db import models


class Job(models.Model):
    """Job model attributes"""
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

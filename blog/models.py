"""
Models for Blog application.
"""
from django.db import models


class Blog(models.Model):
    """Blog model attributes"""
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        """Get short summary text"""
        return self.body[:100] + '...'

    def pub_date_pretty(self):
        """Get pre formatted blog publication date"""
        return self.pub_date.strftime('%b %e %Y')

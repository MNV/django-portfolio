from django.test import TestCase
from .models import Job


class JobTestCase(TestCase):
    def setUp(self):
        self.image = 'image/test.png'
        self.summary = 'summary text'

        Job.objects.create(image=self.image, summary=self.summary)

    def test_job(self):
        """Get job"""
        blog = Job.objects.get(image=self.image)
        self.assertEqual(blog.summary, self.summary)

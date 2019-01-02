from django.test import TestCase
from django.utils import timezone
from .models import Blog


class BlogTestCase(TestCase):
    def setUp(self):
        self.title = 'title'
        self.body = 'body text'
        self.pub_date = timezone.now()
        self.image = 'image/test.png'

        Blog.objects.create(title=self.title, body=self.body, pub_date=self.pub_date, image=self.image)

    def test_blog(self):
        """Get blog"""
        blog = Blog.objects.get(title=self.title)
        self.assertEqual(blog.body, self.body)
        self.assertEqual(blog.pub_date, self.pub_date)
        self.assertEqual(blog.image, self.image)

    def test_summary(self):
        """Get short summary text"""
        blog = Blog.objects.get(title=self.title)
        self.assertEqual(blog.summary(), blog.body[:100] + '...')

    def test_pub_date_pretty(self):
        """Get pre formatted blog publication date"""
        blog = Blog.objects.get(title=self.title)
        self.assertEqual(blog.pub_date_pretty(), blog.pub_date.strftime('%b %e %Y'))

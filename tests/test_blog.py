import time
from selenium import webdriver
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from app.models import Post, Category


class BlogTestCase(LiveServerTestCase):

    def setUp(self):
        """Setup Selenium with Chrome and Firefox"""
        self.chrome_driver = webdriver.Chrome()
        self.firefox_driver = webdriver.Firefox()
        self.user = User.objects.create_user(
            username="test",
            password="123456"
        )
        self.category = Category.objects.create(name="Therapy")
        self.post = Post.objects.create(
            title="Test the first post",
            content="This post is a test from Selenium",
            author=self.user,
            status="published",
            categories=self.category,
        )

    
    def tearDown(self):
        """Close browser after tests"""
        self.chrome_driver.quit()
        self.firefox_driver.quit()

    
    def test_positive_open_blog_page_firefox(self):
        """Test opening blog page in Chrome"""
        self.firefox_driver.get(self.live_server_url + '/blog/')
        time.sleep(30)
        self.assertIn("<h2>Test the first post</h2>\n", self.firefox_driver.page_source)

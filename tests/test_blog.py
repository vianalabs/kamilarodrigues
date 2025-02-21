import time
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from app.models import Post, Category

class BlogTestCase(StaticLiveServerTestCase):
    def setUp(self):
        """Setup the post and Selenium with Firefox"""
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--disable-dev-shm-usage')
        firefox_options.unhandled_prompt_behavior = 'accept'
        
        self.driver = webdriver.Firefox(options=firefox_options)

        #POST
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
        """Close the browser"""
        self.driver.quit()

    def test_positive_open_blog_page_firefox(self):
        """Test opening blog page in Firefox"""

        LOCALHOST_BLOG = f"{self.live_server_url}/blog/"

        self.driver.get(LOCALHOST_BLOG)
        time.sleep(2)
        assert "<h2>Test the first post</h2>" in self.driver.page_source

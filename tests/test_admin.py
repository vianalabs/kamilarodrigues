import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User


class AdminTestCase(StaticLiveServerTestCase):
    """Test case for the admin page"""
    def setUp(self):
        """Setup for Selenium and user"""
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--disable-dev-shm-usage')
        firefox_options.unhandled_prompt_behavior = 'accept'
        self.fx_driver = webdriver.Firefox(options=firefox_options)

        self.password = "123456"
        self.user = User.objects.create_superuser(
            username="admin", 
            password=self.password
        )


    def tearDown(self):
        """Close the browser"""
        self.fx_driver.quit()


    def test_positive_open_admin_page(self):
        """Test opening the admin page"""
        LOCALHOST_ADMIN = f"{self.live_server_url}/admin/"

        self.fx_driver.get(LOCALHOST_ADMIN)
        assert "Django" in self.fx_driver.page_source

    
    def test_positive_login_into_admin_page(self):
        """Test login into the admin page"""
        LOCALHOST_ADMIN = f"{self.live_server_url}/admin/"

        self.fx_driver.get(LOCALHOST_ADMIN)
        username = self.fx_driver.find_element(By.ID, "id_username")
        username.send_keys(self.user.username)
        password = self.fx_driver.find_element(By.ID, "id_password")
        password.send_keys(self.password)
        time.sleep(2)
        login = self.fx_driver.find_element(
            By.CSS_SELECTOR,
            ".submit-row input"
        )
        login.click()
        time.sleep(2)
        assert "Site administration" in self.fx_driver.page_source


    def test_negative_login_into_admin_page(self):
        """Test login into the admin page with wrong credentials"""
        LOCALHOST_ADMIN = f"{self.live_server_url}/admin/"

        self.fx_driver.get(LOCALHOST_ADMIN)
        username = self.fx_driver.find_element(By.ID, "id_username")
        username.send_keys(self.user.username)
        password = self.fx_driver.find_element(By.ID, "id_password")
        password.send_keys("wrong")
        login = self.fx_driver.find_element(
            By.CSS_SELECTOR,
            ".submit-row input"
        )
        login.click()
        time.sleep(3)
        assert "Please enter the correct username and password" in self.fx_driver.page_source


    def test_positive_create_category_and_post(self):
        """Test creating a post in the admin page"""

        LOCALHOST_ADMIN = f"{self.live_server_url}/admin/"
        LOCALHOST_ADD_POST = f"{self.live_server_url}/admin/app/post/add/"
        LOCALHOST_POST = f"{self.live_server_url}/admin/app/post/"
        LOCALHOST_ADD_CATEGORY = f"{self.live_server_url}/admin/app/category/add/"
        LOCALHOST_CATEGORY = f"{self.live_server_url}/admin/app/category"
    

        # Login
        self.fx_driver.get(LOCALHOST_ADMIN)
        username = self.fx_driver.find_element(By.ID, "id_username")
        username.send_keys(self.user.username)
        password = self.fx_driver.find_element(By.ID, "id_password")
        password.send_keys(self.password)
        login = self.fx_driver.find_element(
            By.CSS_SELECTOR,
            ".submit-row input"
        )
        login.click()
        time.sleep(3)
        assert "Site administration" in self.fx_driver.page_source


        # Create a category
        self.fx_driver.get(LOCALHOST_ADD_CATEGORY)
        name = self.fx_driver.find_element(By.ID, "id_name")
        name.send_keys("Test")
        save = self.fx_driver.find_element(
            By.CSS_SELECTOR,
            ".submit-row input"
        )
        save.click()
        time.sleep(2)
        self.fx_driver.get(LOCALHOST_CATEGORY)
        time.sleep(2)
        assert "Test" in self.fx_driver.page_source


        # Create a post
        self.fx_driver.get(LOCALHOST_ADD_POST)
        title = self.fx_driver.find_element(By.ID, "id_title")
        title.send_keys("Test the post")
        content = self.fx_driver.find_element(By.ID, "id_content")
        content.send_keys("This is a test post")

        author = Select(self.fx_driver.find_element(By.ID, "id_author"))
        author.select_by_visible_text("admin")
        status = Select(self.fx_driver.find_element(By.ID, "id_status"))
        status.select_by_visible_text("Published")
        categories = Select(self.fx_driver.find_element(By.ID, "id_categories"))
        categories.select_by_visible_text("Test")

        save = self.fx_driver.find_element(
            By.CSS_SELECTOR,
            ".submit-row input"
        )
        save.click()
        time.sleep(2)

        self.fx_driver.get(LOCALHOST_POST)
        time.sleep(2)
        assert "Test the post" in self.fx_driver.page_source



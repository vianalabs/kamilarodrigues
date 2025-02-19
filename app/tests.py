from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Post, Category


class PostModelTest(TestCase):
    def setUp(self):
        "Creates an user, category and a post befor the tests"
        self.user = User.objects.create_user(username="test", password="123456")
        self.category = Category.objects.create(name="Therapy")
        self.post = Post.objects.create(
            title="Test the first post",
            content="This post is a test from TestCase in Django",
            author=self.user,
            status="published",
            categories=self.category,
        )


    def test_positive_user_is_created(self):
        "Test if the user exists"
        user = User.objects.get(username=self.user.username)
        self.assertEqual(user.username, "test")


    def test_positive_password(self):
        "Test if the password is correct"
        password = User.objects.get(password=self.user.password)
        self.assertTrue(password.check_password("123456"))


    def test_positive_post_is_created(self):
        "Test if te post exists in the database"
        post = Post.objects.filter(title=self.post.title).exists()
        self.assertTrue(post, "This post doesn't exist in te db!")


    def test_positive_contet_from_post(self):
        "Test if the post content is correct"
        post = Post.objects.get(title=self.post.title)
        self.assertEqual(post.content[0], "T")


    def test_negative_contet_from_post(self):
        "Test if the post content is incorrect"
        post = Post.objects.get(title=self.post.title)
        self.assertNotEqual(post.content[0], "1")


    def test_negative_author_from_post(self):
        "Test if the author is incorrect"
        post = Post.objects.get(title=self.post.title)
        self.assertNotEqual(post.author.username, "victor")


    def test_positive_author_from_post(self):
        "Test if the author is correct"
        post = Post.objects.get(title=self.post.title)
        self.assertEqual(post.author.username, "test")

    
    def test_postive_category_from_post(self):
        "Test if the category is correct"
        post = Post.objects.get(title=self.post.title)
        self.assertTrue(post.categories.name == "Therapy")

    
    def test_negative_category_from_post(self):
        "Test if the category is incorrect"
        post = Post.objects.get(title=self.post.title)
        self.assertNotEqual(post.categories.name, "Tecnology")

    
    def test_negative_status_from_post(self):
        "Test if the status is incorrect"
        post = Post.objects.get(title=self.post.title)
        self.assertNotEqual(post.status, "draft")


    def test_positive_status_from_post(self):
        "Test if the status is correct"
        post = Post.objects.get(title=self.post.title)
        self.assertTrue(post.status == "published")

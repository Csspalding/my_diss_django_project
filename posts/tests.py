from django.test import TestCase
from posts.models import Posts
from django.contrib.auth.models import User, AnonymousUser 
from datetime import datetime
from django import models

#VSC files configured files begining with test_*.py will be run as test. 
# Create your tests here, run the tests by manage.py test, for multi tests replace test.py for a folder called tests, insert _init__.py and create test_*.py files - Django will discover and execute these. [Real Python, how to use Django Test Runner]
#Docs manage.py test posts.tests - all tests in posts module, or posts.test.postTestCase one class /case, or posts.tests.postTestCase.test_iser_is_anaonymous is one function or test method, or manage.py test my_diss_django_project - all tests found in package

#from django.config import AUTH_USER_
class MyTestCase(TestCase):
  def setUp(self):
    Posts.object.create(title = "This is my title",body = "This is my post body", user = " ", created_at = datetime.datetime(2019,5,5,12,20), last_modified = models.DatTimeField(2019,5,5,12,21), status = True, post_image = True)

  def test_user_is_anonymous(self):
    post = Posts.object.get(title ="This is my title")
    #self.assertEqual(post.view.function(), 'what I expect')


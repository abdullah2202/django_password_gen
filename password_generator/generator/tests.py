from django.test import TestCase

# Create your tests here.
class HomePageTests(TestCase):

   # Test to see if homepage loads successfully
   def test_homepage(self):
      response = self.client.get('/')
      self.assertEqual(response.status_code, 200)

   # Test to see if Title on homepage is Password Generator
   def test_homepage_title(self):
      response = self.client.get('/')
      self.assertContains(response, 'Password Generator')

class PassswordTests(TestCase):
   
   pass
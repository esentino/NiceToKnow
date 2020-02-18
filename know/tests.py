from django.test import TestCase

# Create your tests here.
class NowTest(TestCase):
    def setUp(self):
        self.data = []

    def test_data_is_empty(self):
        self.assertCountEqual(self.data, [])


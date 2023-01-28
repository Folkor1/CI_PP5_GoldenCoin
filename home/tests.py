from django.test import TestCase


class TestViewHome(TestCase):
    """
    Class to test home view
    """

    def test_render_home_page(self):
        """
        Check if index.html is rendered correctly
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

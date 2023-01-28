from django.test import TestCase


class TestViewCoins(TestCase):
    """
    Class to test coins page views
    """

    def test_render_coins_page(self):
        """
        Check if coins.html is rendered correctly
        """

        response = self.client.get('/coins/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coins/coins.html')

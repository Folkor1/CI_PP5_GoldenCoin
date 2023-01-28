from django.test import TestCase


class TestViewSell(TestCase):
    """
    Class to test sell view
    """

    def test_render_sell_page(self):
        """
        Check if sell.html is rendered correctly
        """

        response = self.client.get('/sell/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sell/sell.html')

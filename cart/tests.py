from django.test import TestCase


class TestViewBag(TestCase):
    """
    Class to test cart view
    """

    def test_render_bag_page(self):
        """
        Check if cart.html is rendered correctly
        """

        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

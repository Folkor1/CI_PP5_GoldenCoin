from django.test import TestCase


class TestViewContact(TestCase):
    """
    Class to test contact view
    """

    def test_render_contact_page(self):
        """
        Check if contact.html is rendered correctly
        """

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

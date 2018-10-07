from django.test import TestCase

from bands.forms import CustomUserCreationForm


class CustomUserCreationFormTest(TestCase):

    def test_form_has_css_classes(self):
        form = CustomUserCreationForm()
        self.assertIn('class="form-control"', form.as_p())

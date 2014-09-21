from django.test import SimpleTestCase

import thumborize


class ThumborizeTests(SimpleTestCase):

    def test_should_accept_filters_as_string(self):
        thumborized = thumborize.url("image.png",
                                     width=300,
                                     height=500,
                                     filters="quality(80):grayscale()")
        self.assertIn("filters:quality(80):grayscale()", thumborized)

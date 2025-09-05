from django.test import TestCase
import unittest

from suppliers.laskin import add, plus_complicated

# Create your tests here.
class LaskinTestCase(TestCase):
    def test_add(self):
        # testaa että add-funktio toimii oikein
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_plus_complicated(self):
        # testaa että plus_complicated-funktio toimii oikein
        self.assertEqual(plus_complicated(2, 3), 3)
        self.assertEqual(plus_complicated(-1, 1), 1)
        self.assertEqual(plus_complicated(0, 0), 0)
        self.assertEqual(plus_complicated(4, 2), 6)

    @unittest.expectedFailure
    def test_plus_complicated_failure(self):
        # tämä testi on tarkoitettu epäonnistumaan
        self.assertEqual(add("2", 3), 5)

    # TDD - Test Driven Development
import unittest
from scripts import testscript as ts
from bs4 import BeautifulSoup as bs


class DividerTest(unittest.TestCase):
    def test_divider(self):
        self.assertEqual(ts.divider(2, 2), 2/1)
        self.assertEqual(type(ts.divider(2, 2)), float)
        with self.assertRaises(ZeroDivisionError):
            ts.divider(2, 0)


class BsobjcreatorTest(unittest.TestCase):
    def test_bsobjcreator(self):
        self.assertEqual(type(ts.bsobj_creator()), bs)

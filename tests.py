import unittest

from pypelines import pypeline


@pypeline
def magic_comps(x: list) -> int:
    return x | sum | (lambda x: x * 2)


class TestPypelines(unittest.TestCase):
    def test_pypeline(self):
        self.assertEqual(magic_comps(range(10)), 90)

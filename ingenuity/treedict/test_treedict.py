import unittest
from .treedict import TreeDict

def data():
    return { 'a': 'string',
        'b': 1,
        'c': [2,3,4],
        'd': { 'e': 5,
              'f': 6,
              'g': {
                  'h': 7,
                  'i': 8}
              }
        }

class test_treedict(unittest.TestCase):

    def test_get_string(self):

        n = TreeDict(data())
        self.assertEqual(n.getdefault('a'), 'string')

    def test_get_list(self):

        n = TreeDict(data())
        self.assertIsInstance(n.getdefault('c'), list)

    def test_get_child_number(self):

        n = TreeDict(data())
        self.assertEqual(n.getdefault('d','e'), 5)

    def test_get_fail(self):

        n = TreeDict(data())
        self.assertIsNone(n.getdefault('d', 'a'))

    def test_get_default(self):

        n = TreeDict(data())
        self.assertEqual(n.getdefault('d', 'a', default=0), 0)

    def test_get_square_brackets(self):

        n = TreeDict(data())
        self.assertEqual(n['b'], 1)

    def test_get_brackets_with_array(self):

        n = TreeDict(data())
        self.assertEqual(n['d', 'e'], 5)

    def test_set_string(self):

        n = TreeDict(data())
        n['a'] = 'new'
        self.assertEqual(n['a'], 'new')

    def test_set_child_number(self):

        n = TreeDict(data())
        n['d','e'] = 6
        self.assertEqual(n.getdefault('d','e'), 6)

    def test_set_dont_set_dict(self):

        n = TreeDict(data())
        with self.assertRaises(Exception):
            n['d'] = 1

if __name__ == '__main__':
    unittest.main()

import unittest
from lab7.lab7A import match, search
from lab7.books import db

class Testlab7AFunctions(unittest.TestCase):

    def setUp(self):
        """
        Define a pattern variation of database used in some tests.
        """
        # Very similar to db but with some parts substituted
        # with "--" and "&"
        self.pattern = [[['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to',
                  'computer', 'science']],
       "--"],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       "&"],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']],
       ['År', 2011]],
      [['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using',
                  'python', 'and', 'c++']],
       ['År', 2009]],
      [['författare', ['anders', 'haraldsson']],
       ['&', ['programmering', 'i', 'lisp']],
       ['År', 1993]]]


    def test_match_basics(self):
        """
        Basic tests for our match function
        """

        # -- VALID TESTS -- #

        # Exact match
        pattern = ['författare', ['&', 'zelle']]
        seq = ['författare', ['&', 'zelle']]
        self.assertTrue(match(seq, pattern))

        # -- INVALID TESTS -- #

        # Test a mismatch
        pattern = ['år', 'Hello']
        seq = ['år', 'unknown']
        self.assertFalse(match(seq, pattern))


    def test_match_wildcard(self):
        """
        Specific tests for our wildcards
        """

        # -- VALID TESTS -- #

        # Test with '--' for both a string and empty
        pattern = ['titel', ['--', 'python', '--']]
        seq = ['titel', ['python', 'rocks']]
        self.assertTrue(match(seq, pattern))

        # Test "&" substitution for a string
        pattern = ['år', '&']
        seq = ['år', '2023']
        self.assertTrue(match(seq, pattern))

        # Test with '--' covering multiple elements in the sequence
        pattern = ['--', ['år', 2042], '--']
        seq = ['something', ['år', 2042], 'more']
        self.assertTrue(match(seq, pattern))

        # Test with '&' matching an element and '__' att the same time
        pattern = ['--', ['titel', ['&', '&']], '--']
        seq = ['before', ['titel', ['python', 'rocks']], 'after']
        self.assertTrue(match(seq, pattern))

        # Test with '__' matching multiple elements
        pattern = ['--']
        seq = ['before', ['titel', ['python', 'rocks']], 'after']
        self.assertTrue(match(seq, pattern))

        # Test a big sequence and pattern
        self.assertTrue(match(db, self.pattern))


        # -- INVALID TESTS -- #

        #Test so that '&' cant match with emptiness
        pattern = ['--', ['titel', ['&', '&']], '--']
        seq = ['before', ['titel', ['rocks']], 'after']
        self.assertFalse(match(seq, pattern))

        #Test so that '&' cant match with multiple elements
        pattern = ['--', ['titel', ['&']], '--']
        seq = ['before', ['titel', ['rocks', 'perfection']], 'after']
        self.assertFalse(match(seq, pattern))

    def test_search_basics(self):
        """
        Basic tests for our search function
        """

        # -- VALID TESTS -- #

        # Test exact match in simple list
        pattern = ['författare', ['john', 'zelle']]
        seq = [
            ['författare', ['john', 'zelle']],
            ['titel', ['python', 'programming']],
            ['författare', ['armen', 'asratian']]
        ]
        result = search(pattern, seq)
        expected = [['författare', ['john', 'zelle']]]
        self.assertEqual(result, expected)

        # Test multiple matches
        pattern = ['År', 2010]
        seq = [
            ['År', 2010],
            ['titel', ['python']],
            ['År', 2010],
            ['År', 2011]
        ]
        result = search(pattern, seq)
        expected = [['År', 2010], ['År', 2010]]
        self.assertEqual(result, expected)

        # Test search returns empty list for no matches
        pattern = ['författare', ['unknown', 'author']]
        seq = [
            ['författare', ['john', 'zelle']],
            ['titel', ['python']]
        ]
        result = search(pattern, seq)
        self.assertEqual(result, [])

        # Test search with empty sequence
        pattern = ['författare', ['john', 'zelle']]
        seq = []
        result = search(pattern, seq)
        self.assertEqual(result, [])

    def test_search_wildcards(self):
        """
        Tests for search function with wildcards
        """

        # -- VALID TESTS -- #

        # Test search with '&' wildcard
        pattern = ['År', '&']
        seq = [
            ['År', 2010],
            ['titel', ['python']],
            ['År', 2011],
            ['År', 'unknown']
        ]
        result = search(pattern, seq)
        expected = [['År', 2010], ['År', 2011], ['År', 'unknown']]
        self.assertEqual(result, expected)

        # Test search with '--' wildcard in list
        pattern = ['titel', ['--', 'python', '--']]
        seq = [
            ['titel', ['learning', 'python', 'the', 'hard', 'way']],
            ['titel', ['python', 'rocks']],
            ['titel', ['java', 'programming']],
            ['titel', ['advanced', 'python', 'techniques']]
        ]
        result = search(pattern, seq)
        expected = [
            ['titel', ['learning', 'python', 'the', 'hard', 'way']],
            ['titel', ['python', 'rocks']],
            ['titel', ['advanced', 'python', 'techniques']]
        ]
        self.assertEqual(result, expected)

        # Test search with nested wildcards
        pattern = ['titel', ['&', '&'], '--']
        seq = [
            ['författare', ['john', 'zelle']],
            ['titel', ['python', 'rocks']],
            ['År', 2010]
        ]
        expected = [['titel', ['python', 'rocks']]]
        result = search(pattern, seq)
        self.assertEqual(result, expected)  # Should match the entire sequence

        # -- INVALID TESTS -- #

        # Test that '&' doesn't match empty
        pattern = ['titel', ['&', '&']]
        seq = [
            ['titel', ['python']],  # Only one element
            ['titel', ['python', 'rocks']]  # Two elements
        ]
        result = search(pattern, seq)
        expected = [['titel', ['python', 'rocks']]]
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()
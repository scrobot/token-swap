import unittest

from token_swap import get_max_tokens


class TokenSwapCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_get_max_tokens(self):
        tokens = ["TokenA, TokenB, 1.2", "TokenB, TokenC, 0.003"]
        queries = ["TokenA, TokenC, 10000", "TokenB, TokenA, 10000"]
        expected = [36, 8333.333333]
        result = get_max_tokens(tokens, 2, queries, 2)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

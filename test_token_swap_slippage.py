import unittest
from token_swap_slippage import get_max_tokens_with_slippage


class TokenSwapWithSlippageCase(unittest.TestCase):
    def test_get_max_tokens(self):
        tokens = ["TokenA, TokenB, 1.2, -0.3", "TokenB, TokenC, 0.003, -1", "TokenA, TokenC, 0.0036, -1"]
        queries = ["TokenA, TokenC, 10000"]
        expected = [35.978402]
        result = get_max_tokens_with_slippage(tokens, queries)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

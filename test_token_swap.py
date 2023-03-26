import unittest
from io import StringIO
from unittest.mock import patch

from main import get_max_tokens_cli
from token_swap import get_max_tokens


class TokenSwapCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_get_max_tokens(self):
        tokens = ["TokenA, TokenB, 1.2", "TokenB, TokenC, 0.003"]
        queries = ["TokenA, TokenC, 10000", "TokenB, TokenA, 10000"]
        expected = [36, 8333.333333]
        result = get_max_tokens(tokens, queries)

        self.assertEqual(result, expected)

    # Test case with minimum input values
    def test_check_exchange_fiat_rate(self):
        self.assertEqual(get_max_tokens(['USD, EUR, 1.08'], ['USD, EUR, 1.08']), [1.080000])

    # Test case with multiple token pairs and queries
    def test_check_exchange_fiat_rate(self):
        tokens = ['USD, EUR, 1.2', 'EUR, GBP, 0.8', 'GBP, JPY, 150']
        queries = ['USD, EUR, 1', 'USD, GBP, 1', 'GBP, JPY, 1000']
        expected = [1.200000, 0.960000, 150000.000000]
        self.assertEqual(get_max_tokens(tokens, queries), expected)

    # Test case with large number of tokens and queries
    def test_check_exchange_fiat_rate(self):
        tokens = ['USD, EUR, 1.2'] * 1000
        queries = ['USD, EUR, 1'] * 1000
        expected = [1.200000] * 1000
        self.assertEqual(get_max_tokens(tokens, queries), expected)

    def test_valid_input(self):
        user_input = """
        2
        USD, EUR, 1.2
        EUR, GBP, 0.8
        2
        USD, EUR, 100
        EUR, GBP, 200
        """.strip()

        expected_output = "The maximum tokens that can be obtained are: [120.0, 160.0]"

        with patch("builtins.input", side_effect=user_input.split("\n")):
            with patch("sys.stdout", new=StringIO()) as output:
                get_max_tokens_cli()

        self.assertTrue(output.getvalue().__contains__(expected_output))

    def test_invalid_token_pairs_count(self):
        user_input = """
        3
        USD, EUR, 1.2
        EUR, GBP, 0.8
        2
        USD, EUR, 100
        EUR, GBP, 200"
        """.strip()

        expected_output = "Invalid input: token pairs count(3) or format(validation_failed=True)\n"

        with patch("builtins.input", side_effect=user_input.split("\n")):
            with patch("sys.stdout", new=StringIO()) as output:
                get_max_tokens_cli()

        self.assertTrue(output.getvalue().__contains__(expected_output))

    def test_invalid_token_pair_format(self):
        user_input = """
        2
        USD EUR 1.2
        EUR, GBP
        2
        USD, EUR, 100
        EUR, GBP, 200
        """.strip()

        expected_output = "Invalid input: token pairs count(2) or format(validation_failed=True)"

        with patch("builtins.input", side_effect=user_input.split("\n")):
            with patch("sys.stdout", new=StringIO()) as output:
                get_max_tokens_cli()

        self.assertTrue(output.getvalue().__contains__(expected_output))

    def test_invalid_query_format(self):
        user_input = """
        2
        USD, EUR, 1.2
        EUR, GBP, 0.8
        2
        USD, EUR, 100
        EUR, GBP
        """.strip()

        expected_output = "Invalid input\n"

        with patch("builtins.input", side_effect=user_input.split("\n")):
            with patch("sys.stdout", new=StringIO()) as output:
                get_max_tokens_cli()

        self.assertTrue(output.getvalue().__contains__(expected_output))

    def test_invalid_exchange_rate(self):
        user_input = """
        2
        USD, EUR, 1.2
        EUR, GBP, -0.8
        2
        USD, EUR, 100
        EUR, GBP, 200
        """.strip()

        expected_output = "Invalid input"

        with patch("builtins.input", side_effect=user_input.split("\n")):
            with patch("sys.stdout", new=StringIO()) as output:
                get_max_tokens_cli()

        print(output.getvalue())

        self.assertTrue(output.getvalue().__contains__(expected_output))


if __name__ == '__main__':
    unittest.main()

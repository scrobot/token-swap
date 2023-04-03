from token_swap import get_max_tokens


def get_max_tokens_cli():
    count = int(input("Enter token pairs count: "))
    tokens = []

    print("Enter the token pairs with exchange rate and maximum slippage in the format {}:".format("TokenA, TokenB, 1.2, -0.03"))
    for i in range(count):
        tokens.append(input())

    # filter out empty strings
    tokens = list(filter(None, tokens))

    if len(tokens) != count or _is_invalid(tokens):
        print("Invalid input: token pairs count({}) or format(validation_failed={})".format(len(tokens), _is_invalid(tokens)))
        return

    count = int(input("Enter queries count: "))
    queries = []

    print("Enter the queries in the format {}:".format("TokenA, TokenC, 10000"))
    for i in range(count):
        queries.append(input())

    # filter out empty strings
    queries = list(filter(None, queries))

    if len(queries) != count or _is_invalid(queries):
        print("Invalid input")
        return

    result = get_max_tokens(tokens, queries)
    print("The maximum tokens that can be obtained are: {}".format(result))


def _is_invalid(tokens: list[str]):
    for token in tokens:
        try:
            token_a, token_b, rate, max_slippage = token.split(', ')
            if token_a == token_b or float(rate) <= 0 or float(max_slippage) >= 0:
                print("token_a({}) == token_b({}): {}".format(token_a, token_b, token_a == token_b))
                print("rate <= 0: {}".format(float(rate) <= 0))
                print("max_slippage >= 0: {}".format(float(max_slippage) >= 0))
                return True
        except ValueError:
            print("Validation failed on parsing: {}".format(token))
            return True
    return False


if __name__ == '__main__':
    get_max_tokens_cli()

# This is a sample Python script.
from token_swap import get_max_tokens


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_max_tokens_cli():
    count = int(input("Enter token pairs count: "))
    tokens = []

    print("Enter the token pairs with exchange rate in the format {}:".format("TokenA, TokenB, 1.2"))
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
            token_a, token_b, rate = token.split(', ')
            if token_a == token_b or float(rate) <= 0:
                print("token_a({}) == token_b({}): {}".format(token_a, token_b, token_a == token_b))
                print("rate <= 0: {}".format(float(rate) <= 0))
                return True
        except ValueError:
            print("Validation failed on parsing: {}".format(token))
            return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_max_tokens_cli()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

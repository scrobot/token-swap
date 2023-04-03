from collections import defaultdict
import heapq

DECIMALS: int = 6


def get_max_tokens_with_slippage(tokens: list[str], queries: list[str]):
    # Build the graph with exchange rates and slippage
    graph = defaultdict(dict)
    token_pairs: int = len(tokens)
    for i in range(token_pairs):
        token_a, token_b, rate, max_slippage = tokens[i].split(', ')
        rate = float(rate)
        max_slippage = float(max_slippage)
        graph[token_a][token_b] = (rate, max_slippage)
        graph[token_b][token_a] = (1.0 / rate, -max_slippage * rate)

    max_tokens = []
    queries_count: int = len(queries)

    # Iterate over each query
    for i in range(queries_count):
        token_a, token_c, amount = queries[i].split(', ')
        amount = float(amount)

        results = []

        # Iterate over all the intermediate tokens
        for intermediate_token in graph[token_a].keys():
            rate_ab, max_slippage_ab = graph[token_a][intermediate_token]
            rate_bc, max_slippage_bc = graph[intermediate_token].get(token_c, (0, 0))
            if rate_bc == 0:
                continue

            # Iterate over all possible amounts to swap directly and indirectly
            for swap_amount in range(0, int(amount) + 1):
                amount_ab = swap_amount

                # Calculate the tokens obtained after the first swap (TokenA -> TokenB)
                tokens_b = _calc_amount_with_slippage(rate_ab, max_slippage_ab, amount_ab)
                # Calculate the tokens obtained from direct swap (TokenA -> TokenC) for the remaining amount
                tokens_c_from_direct = _calc_amount_with_slippage(rate_bc, max_slippage_bc, amount - amount_ab)
                # Calculate the total tokens obtained from both swaps (TokenA -> TokenB -> TokenC) and direct swap (TokenA -> TokenC)
                tokens_c = tokens_b * rate_bc + tokens_c_from_direct
                results.append(tokens_c)

        # Find the best result and append it to the max_tokens list
        best_result = max(results) if results else 0
        max_tokens.append(round(best_result, DECIMALS))

    return max_tokens


# Function to calculate the amount after considering slippage
def _calc_amount_with_slippage(rate, max_slippage, amount):
    slippage = max_slippage * amount / 100000
    rate_with_slippage = rate * (1 - slippage)
    return amount * rate_with_slippage

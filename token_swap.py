from collections import defaultdict
import heapq

DECIMALS: int = 6


def get_max_tokens(tokens: list[str], token_pairs: int, queries: list[str], queries_count: int):
    _validate(tokens)
    _validate(queries)

    # Create a graph with exchange rates as edges
    graph = defaultdict(dict)
    for i in range(token_pairs):
        token_a, token_b, rate = tokens[i].split(', ')
        rate = float(rate)
        graph[token_a][token_b] = rate
        graph[token_b][token_a] = 1.0 / rate

    # Run Dijkstra's algorithm for each query
    max_tokens = []
    for i in range(queries_count):
        token_a, token_c, amount = queries[i].split(', ')
        amount = float(amount)
        dist = {token_a: amount}
        heap = [(amount, token_a)]
        while heap:
            curr_amount, curr_token = heapq.heappop(heap)
            if curr_token == token_c:
                max_tokens.append(round(curr_amount, DECIMALS))
                break
            for neighbor, rate in graph[curr_token].items():
                next_amount = curr_amount * rate
                if next_amount > dist.get(neighbor, 0):
                    dist[neighbor] = next_amount
                    heapq.heappush(heap, (next_amount, neighbor))

    return max_tokens


def _validate(tokens: list[str]):
    for token in tokens:
        token_a, token_b, rate = token.split(', ')
        assert token_a != token_b
        assert float(rate) > 0

from collections import defaultdict
import heapq


def get_max_tokens(tokens, n, queries, q):
    # Create a graph with exchange rates as edges
    graph = defaultdict(dict)
    for i in range(n):
        tokenA, tokenB, rate = tokens[i].split(', ')
        rate = float(rate)
        graph[tokenA][tokenB] = rate
        graph[tokenB][tokenA] = 1.0 / rate

    # Run Dijkstra's algorithm for each query
    max_tokens = []
    for i in range(q):
        tokenA, tokenC, amount = queries[i].split(', ')
        amount = float(amount)
        dist = {tokenA: amount}
        heap = [(amount, tokenA)]
        while heap:
            curr_amount, curr_token = heapq.heappop(heap)
            if curr_token == tokenC:
                max_tokens.append(round(curr_amount, 6))
                break
            for neighbor, rate in graph[curr_token].items():
                next_amount = curr_amount * rate
                if next_amount > dist.get(neighbor, 0):
                    dist[neighbor] = next_amount
                    heapq.heappush(heap, (next_amount, neighbor))

    print(max_tokens)

    return max_tokens
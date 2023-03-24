# token swap test 

## token_swap.py

### Problem:

You are given a list of token pairs and their exchange rates in the following format:

TokenA, TokenB, 1.2
TokenB, TokenC, 0.003

This indicates that 1 unit of TokenA can be swapped for 1.2 units of TokenB, and 1 unit of TokenB can be swapped for 0.003 units of TokenC.

You will be given a number of queries, where each query will be in the format of:

TokenA, TokenC, 10000

This indicates that the user wants to swap 10000 units of TokenA to TokenC.

You need to write a program that will return the maximum number of tokens received at the end of the swap.

Input:

The first line of input will contain a single integer n (1 <= n <= 10^5) indicating the number of token pairs.
The next n lines will contain the token pairs in the format of TokenA, TokenB, rate, where rate is the exchange rate of TokenA to TokenB.
The next line will contain a single integer q (1 <= q <= 10^5) indicating the number of queries.
The next q lines will contain the queries in the format of TokenA, TokenC, amount, where amount is the number of units of TokenA that should be swapped to TokenC.
Output:

For each query, output a single line containing the maximum number of tokens that can be received.
Example:
Input:
2
TokenA, TokenB, 1.2
TokenB, TokenC, 0.003
2
TokenA, TokenC, 10000
TokenB, TokenA, 10000

Output:
36
8333.333333

Note:

The precision of the output should be 6 decimal places.
The tokens and rates are given for example, the actual token names and rates can be different.
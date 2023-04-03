# token swap test 

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/scrobot/token-swap/python-app.yml?style=plastic)

## token_swap.py

### Problem:

You are given a list of token pairs and their exchange rates in the following format:

```
TokenA, TokenB, 1.2
TokenB, TokenC, 0.003
```

This indicates that 1 unit of TokenA can be swapped for 1.2 units of TokenB, and 1 unit of TokenB can be swapped for 0.003 units of TokenC.

You will be given a number of queries, where each query will be in the format of:

```
TokenA, TokenC, 10000
```

This indicates that the user wants to swap 10000 units of TokenA to TokenC.

You need to write a program that will return the maximum number of tokens received at the end of the swap.

Input:

The first line of input will contain a single integer n (1 <= n <= 10^5) indicating the number of token pairs.
The next n lines will contain the token pairs in the format of TokenA, TokenB, rate, where rate is the exchange rate of TokenA to TokenB.
The next line will contain a single integer q (1 <= q <= 10^5) indicating the number of queries.
The next q lines will contain the queries in the format of TokenA, TokenC, amount, where amount is the number of units of TokenA that should be swapped to TokenC.
Output:

For each query, output a single line containing the maximum number of tokens that can be received.
Example input:
```
2
TokenA, TokenB, 1.2
TokenB, TokenC, 0.003
2
TokenA, TokenC, 10000
TokenB, TokenA, 10000
```

Output:
```
36
8333.333333
```

Note:

The precision of the output should be 6 decimal places.
The tokens and rates are given for example, the actual token names and rates can be different.


## token_swap.py[token_swap_slippage.py](token_swap_slippage.py)

### Problem:

In the real world token swaps result in slippage, which is the difference between the expected price of a trade and the price at which the trade is executed.

You are given a list of token pairs and their exchange rates, as well as the maximum slippage for each 100,000 units of the input token (in percentage)

For example, [TokenA, TokenB, 1.2, -0.03] indicates that 1 unit of TokenA can be swapped for 1.2 units of TokenB, and the maximum slippage for 100,000 units of TokenA is -0.03%. The slippage increases linearly from 0 to the maximum slippage depending on the amount of token swapped.

You will be given a number of queries, where each query will be in the format of:

```
TokenA, TokenC, 10000
```

This indicates that the user wants to swap 10000 units of TokenA to TokenC.

You need to write a program that will return the maximum number of tokens received at the end of the swap.

### Input:

The first line of input will contain a single integer n (1 <= n <= 10^5) indicating the number of token pairs.
The next n lines will contain the token pairs in the format of TokenA, TokenB, rate, maximum_slippage, where rate is the exchange rate of TokenA to TokenB and maximum_slippage is the maximum slippage for 100,000 units of TokenA.
The next line will contain a single integer q (1 <= q <= 10^5) indicating the number of queries.
The next q lines will contain the queries in the format of TokenA, TokenC, amount, where amount is the number of units of TokenA that should be swapped to TokenC.

### Output:

For each query, output a single line containing the maximum number of tokens that can be received, rounded to 6 decimal places.
Example:
Input:
```
3
TokenA, TokenB, 1.2, -0.3
TokenB, TokenC, 0.003, -1
TokenA, TokenC, 0.0036, -1
1
TokenA, TokenC, 10000
```

### Output:
```
35.978402
```

### Explanation:

If we swap 10,000 units of TokenA using [TokenA, TokenC, 0.0036, -1], the output will be 10000 * 0.0036 * (1 - 0.01 * 10000/100000) = 35.964 TokenC,

If we swap 10,000 units of TokenA using [TokenA, TokenB, 1.2, -0.3] & [TokenB, TokenC, 0.003, -1],
the first swap would result in 10000 * 1.2 * (1 - 0.003 * 10000/100000) = 11996.4 TokenB,
the second swap would result in 11996.4 * 0.003 * (1 - 0.01 * 11996.4/100000) = 35.946026 TokenC

Hence to maximize the token output, we should swap

```
5999 units of TokenA using [TokenA, TokenC, 0.0036, -1] for 21.583444
4001 units of TokenA using [TokenA, TokenB, 1.2, -0.3] & [TokenB, TokenC, 0.003, -1] for 14.394957
```


### Note:

The precision of the output should be at least 6 decimal places.
The tokens and rates are given for example, the actual token names and rates can be different.
The slippage is given as a percentage, should be converted to decimal for calculation.
The queries are independent and does not change exchange rate or slippage.
The slippage increases linearly from 0 to the maximum slippage depending on the amount of token swapped.
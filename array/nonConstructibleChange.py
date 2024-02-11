"""
PROBLEM STATEMENT:
Given an array of positive integers representing the values of coins in your possession, 
write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. 
The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4.
If you're given no coins, the minimum amount of change that you can't create is 1.

coins = [5, 7, 1, 1, 2, 3, 22]
output = 20
"""

def nonConstructibleChange(coins):
    coins = sorted(coins)
    current_change = 0
    for coin in coins:
        # if the current coin is greater than the current change + 1, 
        # then we can't make the current change + 1
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin
    return current_change + 1
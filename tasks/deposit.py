from ast import Raise
from typing import List

def getPercentage(money: float, period : int) -> float:
    """The given function will return final amount of money after some years"""
    if money < 30000:
        raise Exception('the given amount of money is too small bro!  The minimum is 30 000 soms')
    if period<3:
        raise Exception('the given number of years is too small bro! Tghe minimum is 3 years!')
    i = 0
    while i < period:
        money = money*1.1
        i+=1
    return money
    
print(getPercentage(300000,5))
def next_largest_coin(coin):
    """Возвращает следующую монету.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # остальные возвращают None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
    else:
        return 0

def count_coins(total):
    def monet(n, razmer):
        if n < 4:
            return 1
        elif (n < 0) or (razmer > n) or (razmer == None):
            return 0
        else:
            return monet(n - next_largest_coin(razmer), razmer) + monet(n, next_largest_coin(razmer))
    return monet(total, 1)

print(count_coins(15))
print(count_coins(10))
print(count_coins(20))
print(count_coins(100))

class Account:
    """An account has a.py balance and a.py holder.
    # >>> a.py = Account('John')
    # >>> a.py.deposit(10)
    # 10
    # >>> a.py.balance
    # 10
    # >>> a.py.interest
    # 0.02
    # >>> a.py.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    # 2
    # >>> a.py.balance               # balance should not change
    # 10
    # >>> a.py.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    # 5
    # >>> a.py.time_to_retire(100)
    # 117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
        years = 0
        assumed_balance = self.balance
        while assumed_balance < amount:
            assumed_balance += assumed_balance * self.interest
            years += 1
        return years


a = Account('John')


class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!
    # >>> ch = FreeChecking('Jack')
    # >>> ch.balance = 20
    # >>> ch.withdraw(100)  # First one's free. Still counts as a.py free withdrawal even though it was unsuccessful
    # 'Insufficient funds'
    # >>> ch.withdraw(3)    # Second withdrawal is also free
    # 17
    # >>> ch.balance
    # 17
    # >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    # 13
    # >>> ch.withdraw(3)
    # 9
    # >>> ch2 = FreeChecking('John')
    # >>> ch2.balance = 10
    # >>> ch2.withdraw(3) # No fee
    # 7
    # >>> ch.withdraw(3)  # ch still charges a.py fee
    # 5
    # >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    # 'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    "*** YOUR CODE HERE ***"

    def withdraw(self, amount):
        if self.free_withdrawals > 0:
            self.free_withdrawals -= 1
            return Account.withdraw(self, amount)
        else:
            return Account.withdraw(self, amount + self.withdraw_fee)

# Следующая задача - карточная игра Magic the Lambda-ing! (см. classes.py)
# Для класса Card нужно реализовать конструктор и метод power.
# Для класса Player - конструктор и методы draw и play.
# При реализации метода draw и конструктора используйте метод draw класса Deck.
# Запустить игру можно так: python3 cardgame.py

### Необязательно задание
# Реализовать методы effect для классов TutorCard, TACard, PrefessorCard -
# это сделает игру гораздо интереснее

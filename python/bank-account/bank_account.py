import threading


class BankAccount:
    def __init__(self):
        self.lock = threading.Lock()
        self.is_open = False
        self.balance = None

    def get_balance(self):
        if not self.is_open:
            raise ValueError("Bank account is not open")
        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError("Bank account is already open")
        self.is_open = True
        self.balance = 0

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError("Bank account is not open")
        if amount < 0:
            raise ValueError("Unable to deposit negative funds")

        self.lock.acquire()
        self.balance += amount
        self.lock.release()

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError("Bank account is not open")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        if amount < 0:
            raise ValueError("Unable to withdraw negative funds")

        self.lock.acquire()
        self.balance -= amount
        self.lock.release()

    def close(self):
        if not self.is_open:
            raise ValueError("Bank account is already closed")
        self.__init__()

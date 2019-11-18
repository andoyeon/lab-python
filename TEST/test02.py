class Account:

    def __init__(self, accountno, balance):
        self.accountno = accountno
        self.balance = balance

    def __repr__(self):
        return f'Account(account no.: {self.accountno}, balance: {self.balance})'

    def deposit(self, money):
        if money < 0:
            raise ValueError('입금 금액은 0보다 크거나 같아야 함')
        self.balance += money
        print(f'{money} 입금 후 잔액 {self.balance}')

    def withdraw(self, money):
        self.balance -= money
        print(f'{money} 출금 후 잔액 {self.balance}')

    def transfer(self, to, money):
        self.withdraw(money)
        to.deposit(money)


if __name__ == '__main__':
    count1 = Account(123456, 1000)
    print(count1)
    count1.deposit(500)
    count1.withdraw(200)

    count2 = Account(789456, 100)
    count1.transfer(count2, 500)



class BankAccount:
    history = []
    def __init__(self,balance,int_rate,trans):
        self.__balance = balance
        self.__int_rate = int_rate
        self.__trans = trans

    def deposit(self,amount):
        self.__balance = self.__balance +amount
        print(f'внесение наличных на счёт: {amount}')
        self.history.append('Внесение наличных')
    def withdraw(self,amount):
        self.__balance = self.__balance - amount
        print(f"Снятие наличных: {amount}")
        self.history.append('Снятие наличных')
    def add_interest(self):
        self.__balance = self.__balance * self.__int_rate / 100 + self.__balance
        print(f'Начислены проценты по вкладу: {self.__balance * self.__int_rate / 100}')
        self.history.append('Начисление процентов')

    def history_list(self):
        for i in self.history:
            print('-', i)

account = BankAccount(10000,0.05,1)
account.deposit(1500000)
account.withdraw(7500)
account.add_interest()
account.history_list()
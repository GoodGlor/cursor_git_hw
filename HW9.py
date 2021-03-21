from math import sqrt


class Calculator:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def count(self):
        while True:
            self.action = input('Your action: ')
            if self.action == '+':
                self.total = self._num1 + self._num2
                return print(f'Result: {self.total}')
            elif self.action == '-':
                self.total = self._num1 - self._num2
                return print(f'Result: {self.total}')
            elif self.action == '*':
                self.total = self._num1 * self._num2
                return print(f'Result: {self.total}')
            elif self.action == '/':
                self.total = self._num1 / self._num2
                return print(f'Result: {self.total}')
            elif self.action == '**':
                self.total = self._num1 ** self._num2
                return print(f'Result: {self.total}')
            elif self.action == '^':
                return print(f'Square root num_1:{sqrt(self._num1)} and num_2: {sqrt(self._num2)}')
            elif self.action == '%':
                self.precente = 100 * float(self._num2) / float(self._num1)
                return print(f'Percent of {self._num1} is {self.precente} ')
            else:
                print('Try enter another action')
                continue


n1 = int(input('Enter num 1: '))
n2 = int(input('Enter num 2: '))
c = Calculator(n1, n2)
c.count()








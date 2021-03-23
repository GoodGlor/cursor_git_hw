from math import sqrt
import logging


log_template = '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(level=logging.DEBUG, filename='calculator.log', filemode='a', format=log_template)




class Calculator:

    def count(self):
        while True:
            try:
                self._num1 = int(input('Enter num 1: '))
                logging.info(f'Enter num 1 <{self._num1}>')
                self._num2 = int(input('Enter num 2: '))
                logging.info(f'Enter num 2 <{self._num2}>')
            except ValueError:
                logging.error('ValueError', exc_info=True)
                print('Invalid literal try enter numbers')
                continue
            print('If u want exit press "z"')
            self.action = input('Your action "+", "-", "*", "/", "**", "^", "%" \nIf u want exit press "z"\nEnter your action:  ')
            logging.info(f'Enter action <{self.action}>')

            if self.action == '+':
                Calculator.add(self)

            elif self.action == '-':
                Calculator.difference(self)

            elif self.action == '*':
                Calculator.multiplication(self)

            elif self.action == '/':
                try:
                    Calculator.division(self)
                except ZeroDivisionError:
                    logging.error('ZeroDivisionError', exc_info=True)
                    print('Try enter number greater 0')
                    continue

            elif self.action == '**':
                Calculator.exponentiation(self)

            elif self.action == '^':
                try:
                    Calculator.square_root(self)
                except ValueError:
                    logging.error('ValueError', exc_info=True)
                    print('Enter num greater 0')

            elif self.action == '%':
                try:
                    Calculator.percent(self)
                except ZeroDivisionError:
                    logging.error('ZeroDivisionError', exc_info=True)
                    print("First number shouldn't be 0")

            elif self.action == 'z':
                break
            else:
                print('Try enter another action')
                continue

    def add(self):
        self.total = self._num1 + self._num2
        print(f'Result: {self.total}')

    def difference(self):
        self.total = self._num1 - self._num2
        print(f'Result: {self.total}')

    def multiplication(self):
        self.total = self._num1 * self._num2
        print(f'Result: {self.total}')

    def division(self):
        self.total = self._num1 / self._num2
        print(f'Result: {self.total}')

    def exponentiation(self):
        self.total = self._num1 ** self._num2
        print(f'Result: {self.total}')

    def square_root(self):
        print(f'Square root num_1:{sqrt(self._num1)} and num_2: {sqrt(self._num2)}')

    def percent(self):
        self.precente = 100 * float(self._num2) / float(self._num1)
        print(f'Percent of {self._num1} is {self.precente} ')


c = Calculator()
c.count()

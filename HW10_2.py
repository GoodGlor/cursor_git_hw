# import openpyxl
# import re
# 
# 
# class ErrorName(Exception):
#     pass
# 
# 
# class ErrorMail(Exception):
#     pass
# 
# 
# class Registration:
#     def __init__(self):
#         self.user = []
#         self.wb = openpyxl.load_workbook('D:\Projects\Cursor\HW10/user.xlsx')
#         self.sheet = self.wb.active
# 
#     def user_name(self):
#         try:
#             self.name = str(input('Name: '))
#             if not self.name.isalpha():
#                 print('Please use only letters, try again')
#                 return False
#             if self.name.isascii():
#                 self.check_name = [name.value for name in self.sheet['A']]
#                 if self.name.capitalize() in self.check_name:
#                     raise ErrorName()
#                 else:
#                     return self.user.append(self.name.capitalize())
#             else:
#                 print('Try enter only ascii letters')
#                 return False
#         except ErrorName:
#             print('User with this name already  created. Try another name.')
#             return False
# 
#     def user_email(self):
#         regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
#         try:
#             self.mail = str(input('Enter your email: '))
#             if not (re.search(regex, self.mail)):
#                 print('Invalid email. Enter email')
#                 return False
#             if self.mail.isascii():
#                 self.col_mail = [mail.value for mail in self.sheet['B']]
#                 if self.mail.lower() in self.col_mail:
#                     raise ErrorMail()
#                 else:
#                     return self.user.append(self.mail.lower())
#             else:
#                 print('Try enter only ascii letters')
#                 return False
#         except ErrorMail:
#             print('User with this email already  created. Try another mail.')
#             return False
# 
#     def user_pasw(self):
#         self.password = str(input('Enter your password: '))
#         return self.user.append(self.password.lower())
# 
#     def registred(self):
#         while True:
#             if Registration.user_name(self) == False:
#                 continue
#             elif Registration.user_email(self) == False:
#                 continue
#             else:
#                 Registration.user_pasw(self)
#                 self.sheet.append(self.user)
#                 self.wb.save('D:\Projects\Cursor\HW10/user.xlsx')
#                 print('200')
#                 break





from HW10_2 import Registration
import unittest
from unittest import mock


class TestRegistration(unittest.TestCase):
    reg = Registration()

    def test_user_name(self):
        names = ['asd123', '123456', '@!&^%', 1234, 1.2123, ' ']
        for name in names:
            with mock.patch('builtins.input', return_value=name):
                print(name)
                assert self.reg.user_name() == False

    def test_user_email(self):
        emails = ['artem@', ' ', '.com', 'ASDFGHSD.COM']
        for email in emails:
            with mock.patch('builtins.input', return_value=email):
                print(email)
                assert self.reg.user_email() == False


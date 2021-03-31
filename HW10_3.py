# import openpyxl
# import uuid
# 
# 
# class Authorization:
#     def __init__(self):
#         self.user = []
#         self.wb = openpyxl.load_workbook('D:\Projects\Cursor\HW10/user.xlsx')
#         self.sheet = self.wb.active
# 
#     def check_email(self):
#         self.emal = str(input('Enter your email: ')).lower()
#         self.ch_emal = [email.value for email in self.sheet['B']]
#         if self.emal in self.ch_emal:
#             return True
#         else:
#             print('User with this email does not exist')
#             return False
# 
#     def check_password(self):
#         self.password = str(input('Enter yor password: ')).lower()
#         self.ch_password = [paswd.value for paswd in self.sheet['C']]
#         if self.password in self.ch_password:
#             return True
#         else:
#             print('Invalid password')
#             return False
# 
#     def check_all(self):
#         while True:
#             if Authorization.check_email(self) == True and Authorization.check_password(self) == True:
#                 print(f'OK -> {uuid.uuid4()}')
#                 break
#             else:
#                 continue
# 



from HW10_3 import Authorization
import unittest
from unittest.mock import patch


class TestAuthorization(unittest.TestCase):
    auth = Authorization()

    def test_check_email(self):
        emails = ['email@asd', 1234, 'ASDASD@GMAIL.COM', 1.123, '123.123@MAIL.UA']
        for email in emails:
            with patch('builtins.input', return_value=email):
                print(email)
                assert self.auth.check_email() == False


    def test_check_password(self):
        paswds = ['email@asd', 12, 'ASDASD@GMAIL.COM', 1.123, '123.123@MAIL.UA', 'asdd1', '!```*7123']
        for pasw in paswds:
            with patch('builtins.input', return_value=pasw):
                print(pasw)
                assert self.auth.check_password() == False




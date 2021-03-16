# Task 1

task1 = open('task1.txt', 'r')
full_lst = [lst.replace('\n', '') for lst in task1]
dic = {full_lst[index]: full_lst[index + 1] for index in range(0, len(full_lst), 2)}
task1.close()
task1_2 = open('task1.txt', 'w')
text = [task1_2.write(f'{line} \n') for line in dic.values()]
task1_2.close()


# Task 2

import pickle

with open('task2', 'rb') as task2:
    unbin = pickle.load(task2)
    total = sum(unbin) / len(unbin)

# Task 3


import xlsxwriter


class OpenXlsx:
    def __init__(self, file):
        self.filename = open(file)
        self.workbook = xlsxwriter.Workbook(file)
        self.sheet = self.workbook.add_worksheet()

    def __enter__(self):
        return self.sheet

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.workbook.close()
        self.filename.close()


with OpenXlsx('cursor.xlsx') as f:
    f.write("B3", 'Cursor')

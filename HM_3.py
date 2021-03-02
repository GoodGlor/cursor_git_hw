# 1 Define the id of next variables:

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(f"id 'int_a': {id(int_a)} \nid 'str_b': {id(str_b)} \nid 'set_c': {id(set_c)} \n"
      f"id 'lst_d': {id(lst_d)} \nid 'dict_e': {id(dict_e)} ")

# 2  Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(f"same id 'lst_d': {id(lst_d)} ")

# 3 Define the type of each object from step 1.
print(f"Type 'int_a': {type(int_a)}\nType 'str_b': {type(str_b)}\nType 'set_c': {type(set_c)}\n" \
f"Type 'lst_d': {type(lst_d)}\nType 'dict_e': {type(dict_e)}")

# 4 Check the type of the objects by using isinstance.
print('Type of of objects using isinstance')
print(f"Type 'int_a': {isinstance(int_a, int)}\nType 'str_b': {isinstance(str_b, str)}\nType 'set_c': {isinstance(set_c, int)}\n" \
f"Type 'lst_d': {isinstance(lst_d, list)}\nType 'dict_e': {isinstance(dict_e, tuple)}")



# 5 - 11

print("Anna has {0} apples and {1} peaches.".format(1, 4))

print("Anna has {ten} apples and {tow} peaches.".format(ten=10, tow=2))

print("Anna has {0:5} apples and {1:3} peaches.".format( 'five', 'four'))

print(f"Anna has {0} apples and {2} peaches.")

print(f"Anna has %s apples and %s peaches." % (5, 9))

print(f"Anna has {dict_e['c']} apples and {dict_e['a']} peaches.")



# 12 - 13 Convert

lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)


list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)


print(' ')

# 14 - 15

d ={num : num ** 2 for num in range(1,11) if num % 2 == 1 }
print(d)


d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1,11)}
print(d)


# 16 - 17

dict_comprehension = {}
for x in range (10):
    if x**3 % 4 == 0:
        dict_comprehension[x] = x ** 3
print(dict_comprehension)


dict_comprehension = {}
for x in range (10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
    else:
        dict_comprehension[x] = x
print(dict_comprehension)



# 18 - 19

foo = lambda x, y: x if x < y else y
print(foo(8, 7))

def foo (x,y,z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(4,5,3))


# 20 - 22

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
print(sorted(lst_to_sort, reverse=True))
multiply_lst = list(map(lambda x: x*2, lst_to_sort))
print(multiply_lst)


#23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
mul_lst = list(map(lambda x, y: x * y, list_B, list_A ))
print(mul_lst)


#24

from functools import reduce


def add (a, b):
    total = a + b
    print(f'{a} + {b} =  {total}')
    return total


print(reduce(add, lst_to_sort))

total_of_list =  reduce(lambda a, b: a + b, lst_to_sort)
print(total_of_list)


#25

fislter_of_lst = list(filter(lambda x : (x % 2 == 1), lst_to_sort))
print(fislter_of_lst)

#26

b = range(-10, 10)

filter_b = list(filter(lambda x : (x< 0), b))
print(filter_b)

#27

list_1 = [1,2,3,5,7,9]

def  com (variable):
    list_2 = [2, 3, 5, 6, 7, 8]
    if (variable in list_2):
        return True
    else:
        False

common_list = list(filter(com,list_1))
print(common_list)













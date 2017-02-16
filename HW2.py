# 1. Написать функцию, которая спрашивает пользователя число и степень числа, возвращает число в степени.

def stepen(arg,koef):
    result = (arg ** koef)
    return result
arg = int(input('Назови число: '))
koef = int(input('выбери степень, в которую возводим: '))
print(stepen(arg,koef))


#or in endless cycle
x = int(input('Input your argument: '))
y = int(input('input multiplication range: '))
while True:
    def Multiplier(x,y):
        return(x ** y)
    print(Multiplier(x,y))
    break


# 2. Написать функцию для определения НОК для двух чисел.

x = int(input('Input your fifst argument: '))
y = int(input('Input your second argument: '))
def NOD(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        elif y > x:
            y = y % x
        else:
            print('Your numbers are equal, so we are having deal with two {}'.format(x))
            x = x % y
    return x + y
NOD = int(NOD(x, y))
NOK = int((x * y) / NOD) 
print(NOK)

# 3. Написать функцию, которая принимает список, и возвращает словарь в формате: "тип данных: количество объектов" 
#count_types([1, 4, 'd']) -> {<class 'int'>: 2, <class 'str'>: 1}

def count_types(l):
    my_dict = {}
    my_list = []
    for i in l:
        my_list.append(type(i))
    for i in my_list:
        my_dict.update({i:my_list.count(i)})
    return my_dict

# 4. Написать функцию, которая принимает два словаря, сравнивает их ключи, выдает в консоль сколько у них общих ключей

def count_equal_keys(x,y):
    equal_keys = 0
    for i in x:
        for l in y:
            if i == l:
                equal_keys +=1
    return equal_keys   

# 5. Написать функцию, которая принимает любое количество аргументов, 
#она вернуть список типов, принятых аргументов 
#find_types(1, 's', []) -> [<class 'int'>, <class 'str'>, <class 'list'>]

def find_types(*args):
    ints = 0
    strs = 0
    dicts = 0
    lists = 0
    tuples = 0
    types_list = []
    for i in args:
        types_list.append(type(i))
        if type(i) == int:
            ints += 1
        elif type(i) == str:
                strs += 1
        elif type(i) == dict:
                    dicts += 1
        elif type(i) == list:
                        lists += 1
        elif type(i) == tuple:
            tuples +=1
    return(types_list, 'ints: {}'.format(ints), 'strs: {}'.format(strs), 'dicts: {}'.format(dicts), 'lists: {}'.format(lists), 'tuples: {}'.format(tuples))  

# 6. Написать функцию, которая принимает на вход список списков (матрицу) 
#и выводит ее в виде матрицы (один ряд на одной строке) в консоль
def matrix(lst):
    for element in lst:
        print(element)

# 7. Написать функцию, которая принимает любое количество аргументов - списков, 
#она должна возвращать список из всех объектов списков, но каждый объект должен быть уникальным 
#join_lists([1, 2], ['a', 2], ['c', 1]) -> [1, 2, 'a', 'c']
def find_unique(*lst):
    result = []
    for x in lst:
        for element in x:
            if element not in result:
                result.append(element)
    return result
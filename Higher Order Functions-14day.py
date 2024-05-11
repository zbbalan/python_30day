import time
def sun_numbers(num):
    return sum(num)
def higer_order(f,lst):
    summimt = f(lst)
    return summimt

print(higer_order(sun_numbers,[1,2,3,4,5]))
'''sun_numbers(num) 函数的功能是返回列表 num 中所有元素的和。

higer_order(f,lst) 函数是一个高阶函数，它接受一个函数 f 和一个列表 lst 作为参数。
该函数将列表 lst 作为参数传递给函数 f，并返回函数 f 的返回值。

示例代码中的 higer_order(sun_numbers,[1,2,3,4,5]) 调用等价于 sun_numbers([1,2,3,4,5])，
即计算列表 [1,2,3,4,5] 中所有元素的和。最终输出结果为 15。'''
#高阶函数根据传递的参数返回不同的函数
def suoer(X):
    return X ** 2
def intermidei(X):
    return X ** 3
def absowfile(X):
    if X >= 0:
        return X
    else:
        return -(X)

def higer_orde_function(typr):
    if typr == 'suoer':
        return suoer
    elif typr == 'intermidei':
        return intermidei
    elif typr =='absowfile':
        return absowfile
    else:
        return None
resulf = higer_orde_function('suoer')
print(resulf(5))
resulf = higer_orde_function('intermidei')
print(resulf(5))
resulf = higer_orde_function('absowfile')
print(resulf(-5))

##闭包
#在Python中，闭包是通过将一个函数嵌套在另一个封装函数中，然后返回内部函数来创建的
def add_num():
    the = 10
    def add_num2(num):
        return the + num
    return add_num2

cluset_num = add_num()
print(cluset_num(5))

##Python装饰器

def uncrpper(function):
    def warpper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return warpper
@uncrpper
def say_hi():
    return 'hello world'
print(say_hi())
###装饰器传入参数
def defunce(func):
    def warpper(arg):
        print(time.time())
        func(arg)
    return warpper
@defunce
def say_hi(name):
    print('hello',name)
say_hi('james')

#因为多个函数可以同时使用一个装饰器函数，考虑到各个函数需要的参数个数不同，
#可以将装饰器函数的参数设置为可变参数
def decorator(func):
    def wargs(*args,**kwargs):
        print(time.time())
        func(*args,**kwargs)
    return wargs

@decorator
def sum(a,b):
    print(f'{a}+{b}={a+b}')
sum(1,2)

def decorator1(func):
    def wargs(*args,**kwargs):
        print('thes is a decorator1 ')
        func(*args,**kwargs)
    return wargs
def decorator2(func):
    def wargs(*args,**kwargs):
        print('thes is a decorator2 ')
        func(*args,**kwargs)
    return wargs
@decorator1
@decorator2
def name1(name):
    print(f'hello {name}')
name1('james')

#在装饰函数中接受参数
def decorator_with_parameters(funcito):
    def wrapper_accepting_parameters(priat1,priat2,priat3):
        funcito(priat1,priat2,priat3)
        print('I live in {}'.format(priat3))
        return wrapper_accepting_parameters
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name,last_name,country):
    print('I am {} {}.I am from {}'.format(first_name,last_name,country))

print_full_name('James','Bond','London')


##map函数映射
numbers = [1,2,3,4,5,6,7,8,9,10]
def square(x):
    return x ** 2
numbers_anbody = list(map(square,numbers))
print(numbers_anbody)

numbers_anbody = list(map(lambda x:x ** 2,numbers))
print(numbers_anbody)


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def change_to_upper(name):
    return name.upper()
change = list(map(change_to_upper,names))
print(change) #['ASABENEH', 'LIDIYA', 'ERMIA', 'ABRAHAM']
change = list(map(lambda name:name.upper(),names))
print(change) #['ASABENEH', 'LIDIYA', 'ERMIA', 'ABRAHAM']

##filter函数调用指定的函数，该函数为指定的可迭代对象（列表）的每个项返回布尔值。它过滤满足过滤条件的项目。
numbers1 = [1,2,3,4,5]
def square(num):
    if num % 2 == 0:
        return True
    return False
event_num = filter(square,numbers1)
print(list(event_num))

numbers3 = [1,2,3,4,5,6,7,8,9,10] 
def square2(num):
    if num % 2 != 0:
        return True
    return False  
event_num2 = filter(square2,numbers3)
print(list(event_num2))  ##[1, 3, 5, 7, 9]

def names_length(name):
    if len(name) > 7:
        return True
    return False
event_names = filter(names_length,names)
print(list(event_names))  ##['Asabeneh']
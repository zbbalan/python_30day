###当我们创建一个函数时，我们称之为声明一个函数。当我们开始使用它时，我们称之为调用或调用函数。函数可以声明为带参数或不带参数。
def naum_full():
    fist_name = 'hello'
    gull_namu = 'world'
    num_count = fist_name + gull_namu
    print(num_count)

naum_full()

def add_num():
    num1 = 1
    num2 = 2
    num3 = num1 + num2
    print(num3)
add_num()
'''函数也可以返回值，如果函数没有return语句，
则函数的值为None。让我们用return重写上面的函数。
从现在开始，当我们调用函数并打印它时，我们从函数中获取一个值。'''
def add_num1():
    num1 = 1
    num2 = 2
    num3 = num1 + num2
    return num3
print(add_num1())  ##3

###在函数中，我们可以传递不同的数据类型（数字，字符串，布尔值，列表，元组，字典或集合）作为参数
def gressings(name):
    message = name + 'hello'
    return message
print(gressings('wtf'))  ##wtfhello

def addnum12(num1):
    num2 = 10
    num3 = num1 + num2
    return num3
print(addnum12(10)) ##20

def num12(num1,num2):
    num3 = num1 + num2
    return num3
print(num12(10,20)) ##30


'''两个参数：一个函数可以有也可以没有一个或多个参数。
一个函数也可以有两个或多个参数。
如果我们的函数接受参数，我们应该用参数调用它。
让我们检查一个有两个参数的函数：'''

def full_name(name1,name2):
    speca = ''
    name3 = name1 + speca + name2
    return name3
print('这是输出:',full_name('hello','world'))


##如果我们传递带有key和value的参数，那么参数的顺序并不重要。 传递带有键和值的参数
def print_full_name(firstname,lastname):
    space = ''
    fullname = firstname + space + lastname
    return fullname
print(print_full_name(firstname= 'hello',lastname= 'world'))

def num_full(num1,num3):
    num4 = num1 + num3
    print(num4)
print(num_full(num1= 1, num3= 20))


###返回列表： 范例：
def find_even_num(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_num(10))

'''###有时候我们在调用函数的时候，
会将默认值传递给参数。如果我们在调用函数时不传递参数，
则将使用它们的默认值'''

def Hello_name(name = 'pater'):
    message = name + 'hello python'
    return message
print(Hello_name())  ##paterhello python
print(Hello_name('Alan')) ##Alanhello python


def clear_age(birth_num,currle_num = 10):
    age = currle_num - birth_num
    return age
print(clear_age(8)) ###2 
print(clear_age(1990,2020)) ###30

###任意数量的参数
##如果我们不知道传递给函数的参数的数量，我们可以通过在参数名前添加 * 来创建一个可以接受任意数量参数的函数。
def sun_nmu(*age):
    tola = 0
    for num in age:
        tola += num
    return tola
print('is:',sun_nmu(1,2,3,4,5,6,7,8,9,10)) ###55

##函数中的默认参数和任意数量的参数
def greann_num(num_sum,*age):
    print(num_sum)
    for i in age:
        print(i)
print(greann_num(10,20,30,40,50,60,70,80,90,100))

##函数作为另一个函数的参数
def squn_num(n):
    return n * n
def somthing(func,num):
    #return func(num)
    print(func(num))
print(somthing(squn_num,10))

#练习
def declare(age,age2):
    age3 = age + age2
    return age3
print(declare(10,20))  

def yuan(num):
    pai = 3.14
    num1 = pai * num * num
    return num1
print(yuan(10))

def zi(*age):
    if type(age) == tuple:
        num3 =  age + age
        return num3
    else:
        print('error')
print(zi("hello"))

def num12(input_list = []):
    #list = []
    out_list = reversed(input_list)
    print(out_list)
print(num12([1,2,3,4,5,6,7,8,9,10]))


def reverse_list(input_list):
    reversed_list = list(reversed(input_list))
    return reversed_list
print(reverse_list([1,2,3,4,5,6,7,8,9,10]))

def add_item(name):
    inputy_type = ['Potato', 'Tomato', 'Mango', 'Milk',]
    if not isinstance(name, list):
        raise TypeError('error')
    inputy_type.extend(name)
    return inputy_type
print(add_item(['accca']))


'''def add_itemA(name):
    inputy_type = ['Potato', 'Tomato', 'Mango', 'Milk',]
    if not isinstance(name, list):
        raise TypeError('error')
    new_list = inputy_type.copy()
    new_list.remove(name)
    return new_list
print(add_itemA('Potato'))'''
#inputy_type = ['Potato', 'Tomato', 'Mango', 'Milk',]
#print(inputy_type.index('Potato'))

def add_itemA(name):
    inputy_type = ['Potato', 'Tomato', 'Mango', 'Milk',]
    if not isinstance(name, list):
        raise TypeError('error')
    age = inputy_type.index(name)
    input_list = inputy_type.copy()
    input_list.pop(age)
    print (input_list)
print(add_itemA('Potato'))

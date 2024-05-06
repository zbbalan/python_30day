#函数是可重用的代码块或编程语句，旨在执行特定任务。为了定义或声明一个函数，Python提供了def关键字。下面是定义函数的语法。只有当函数被调用时，代码的函数块才被执行
def funcion_name():
    print("Hello World")


funcion_name()

def generate_full_name ():
    one_name = "Asabeneh"
    tow_name = "Yetayeh"
    space = one_name+tow_name
    return space
print(generate_full_name()) 
##在函数中，我们可以传递不同的数据类型（数字，字符串，布尔值，列表，元组，字典或集合）作为参数
def sum_func_name(name):
    message = name + "hello"
    return message
print(sum_func_name("zbb"))

def add_numbers(num1):
    ten = 10
    return  num1 + ten



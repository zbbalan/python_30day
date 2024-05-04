##模块是包含一组代码或一组函数的文件，可以包含在应用程序中。模块可以是包含单个变量、函数或大型代码库的文件
##我们可以在一个文件中有许多函数，我们可以以不同的方式导入所有函数。
import os
import string
#但是如果我们想导入math模块中的所有函数，我们可以使用 *。
from os import *
import random
from mymodule import generate_full_name,sum_two_nums,person,gravity
#在导入过程中，我们可以重命名模块的名称。
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g 
import mymodule
print(mymodule.generate_full_name('Tom','Alan'))
print(mymodule.sum_two_nums(2,3))
print(mymodule.person('Tom'))
print(mymodule.gravity(100,10))

print(fullname('zbb','time'))
print(total(2,3))
print(p('Tom'))
print(g(100,10))
###与其他编程语言一样，我们也可以通过使用关键字import导入文件/函数来导入模块。让我们导入我们大部分时间都会使用的通用模块。
#一些常见的内置模块：math，datetime，os，sys，random，statistics，collections，json，re
##使用python os模块可以自动执行许多操作系统任务。
#Python中的OS模块提供了创建，更改当前工作目录，删除目录（文件夹），获取其内容，更改和识别当前目录的功能。
#os.mkdir('test')  ##创建当前目录
#os.getcwd() ###获取当前目录
#os.chdir('test') ###改变当前目录
#os.rmdir('test')
#print(random())
#print(randint(1,10))

###练习
def num_str(num):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return ran_str
print(num_str(6))



def generate_random_string(num):
    """
    生成一个由字母和数字组成的随机字符串。
    :param num: 随机字符串的长度
    :return: 生成的随机字符串
    """
    if num < 0:
        raise ValueError("num 不能为负数")
    
    return ''.join(random.sample(string.ascii_letters + string.digits, num))

def num_str(num, num2):
    """
    根据需求生成 num 个长度为 num2 的随机字符串数组，并打印这些字符串。
    :param num: 随机字符串的数量
    :param num2: 每个随机字符串的长度
    """
    if num < 0 or num2 < 0:
        raise ValueError("num 和 num2 不能为负数")
    
    # 生成 num 个随机字符串
    random_strings = [generate_random_string(num2) for _ in range(num)]
    
    # 打印生成的随机字符串
    for i, str in enumerate(random_strings):
        print(f"随机字符串 {i+1}: {str}")

# 调用示例
num_str(6, 6)

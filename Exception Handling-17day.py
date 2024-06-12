#Python使用try和except来优雅地处理错误。
#错误的优雅退出（或优雅处理）是一种简单的编程习惯-程序检测到严重的错误条件并以受控的方式“优雅退出”。
#程序通常会在优雅退出时向终端或日志打印一条描述性错误消息，这使我们的应用程序更加健壮。
#异常的原因通常是程序本身的外部原因。异常的一个例子可能是错误的输入、
#错误的文件名、找不到文件、IO设备故障。
#优雅的错误处理可以防止我们的应用程序崩溃。
def num_add_name():
    try:
        result = 15+int('5')
        print(result)
    except Exception as e:
        print('Something went wrong: ', str(e))

num_add_name()

def num_name(name,year_bore):
    try:
        name = input('Enter your name: ')
        year_bore = input('Enter your year of birth: ')
        age = 2019 - int(year_bore)
        print(name)
        print(age)
    except:
        print('Something went wrong')
    return name,year_bore
num_name(name=(),year_bore=())

def sum_name(name,year_bore):
    try:
        name = input('Enter your name: ')
        year_bore = input('Enter your year of birth: ')
        age = 2019 - int(year_bore)
        print(name,age)
    except ValueError:
        print('Something went wrong')
    except TypeError:
        print('Something went wrong')
    except:
        print('Something went wrong')
    return name,year_bore 
sum_name(name=(),year_bore=())

###简写方式使用
'''except Exception as e:
        print(e) '''
def sela_num(num_name,num_year_bor):
    try:
        num_name = input('输入姓名')
        num_your_bor = input('输入年龄')
        age = 2019 - int(num_your_bor)
        print(num_name,age)
    except Exception as e:
        print(e)
    return num_name,num_year_bor
sela_num(num_name=(),num_year_bor=())

def sun_of_num(a,b,c,d):
    return a+b+c+d
lst = [1,2,3,4]
print(sun_of_num(*lst)) ###10

##从列表中解包
numes = range(1,10)
print(list(numes)) ##[1,2,3,4,5,6,7,8,9]
ages = [2,7]
numbers = range(*ages)
print(list(numbers)) ##[2,3,4,5,6,7]

Tmples = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fir,*rest,tme,aln = Tmples
print(*rest)


##解包字典
def info_unicode(name,city,age,county):
    return f'your{name}last{city},is{age},and{county}'
dect = {'name':'alan','city':'beijing','age':'18','county':'china'}
print(info_unicode(**dect))

##打包,有时候，我们永远不知道有多少参数需要传递给一个Python函数。
#我们可以使用packing方法来允许我们的函数接受无限数量或任意数量的参数
def num_all(*agr):
    s = 0
    for i in agr:
        s += i
    return s
print(num_all(1,2,3,4,5,6,7,8,9,10)) 

def packing_dictionary(**kwargs):
    for key in kwargs:
        print(f'{key} = kwargs[key]')
    return kwargs
print(packing_dictionary(name='alan',city='beijing',age='18',county='china'))

##如果我们对一个列表的索引感兴趣，我们使用enumerate内置函数来获取列表中每个项目的索引。
for index,item in enumerate([20,30,40]):
    print(index,item)

countries = ['Findlond','Sweden','Norway','Denmark','Iceland']
for index,i in enumerate(countries):
   # print('hi')
    if i == 'Findlond':
        print(f'The country {i} has been found at index {index}')

 
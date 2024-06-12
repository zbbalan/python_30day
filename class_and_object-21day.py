class classNamed:
    pass
print(classNamed)
p = classNamed()
print(p)
####Python也有一个内置的init（）构造函数。
####初始化构造函数有一个self参数，它是对类的当前实例的引用 示例
class pason:
    def __init__(self,name):
        self.name = name
p = pason('alan')
print(p.name) 
print(p)

class pasonON:
    def __init__(self,name,age,tag):
        self.name = name
        self.age = age
        self.tag = tag
myclass = pasonON('alan',18,'python')
print(myclass.name)
print(myclass.age)
print(myclass.tag)

class pasonTO:
    def __init__(self,name,age,tag,country):
        self.name = name
        self.age = age
        self.tag = tag
        self.country = country
    def pason_info(self):
        return f'{self.name},{self.age},{self.tag},{self.country}'
pasonclass = pasonTO('tain',18,'python','china')
print(pasonclass.pason_info())

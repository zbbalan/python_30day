class classNamed:
    pass
print(classNamed)
p = classNamed()
print(p)
####Python也有一个内置的init（）构造函数。.
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


##对象方法
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

##对象默认方法
##对象方法有一个默认值。如果我们给予构造函数中参数的默认值，
#就可以避免在调用或实例化不带参数的类时出错
class pasonWO:
    def __init__(self,name='AlaN',age=19,tag='java',country='chinan'):
        self.name = name
        self.age = age
        self.tag = tag
        self.country = country
    def pason_info(self):
        return f'{self.name},{self.age},{self.tag},{self.country}'
p1 = pasonWO()
print(p1.pason_info())
p2 = pasonWO('Alan',20,'html','China')
print(p2.pason_info())

###修改类默认值
class pasonMO:
    def __init__(self,name='Make',age=21,tag='work',country='China'):
        self.name = name
        self.age = age
        self.tag = tag
        self.country = country
        self.skills=[]
    def pason_info(self):
        return f'{self.name},{self.age},{self.tag},{self.country}'
    def add_skill(self,skill):
        self.skills.append(skill)

p1=pasonMO()
print(p1.pason_info())
p1.add_skill('PYTHON')
p1.add_skill('HTML')
p1.add_skill('CSS')
p2=pasonMO('jack',23,'html','CHINA')
print(p2.pason_info())
print(p1.skills)
print(p2.skills)

'''class student(Person):
    def __init__(self, firstname='jackMake', age=21, tag='work', country='China'):
        self.country = country
        super().__init__(firstname, age,tag,country)
    def Person_info(self):
        return f'{self.firstname},{self.age},{self.tag},{self.country}'

s1 = student('Alan',18)
s2= student('jack',23)
print(s1.Person_info())'''

class Base(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
class A(Base):
    def __init__(self, a, b,c):
        super().__init__(a, b)
        self.c = c
D = A(1,2,3)
print("a=%d,b=%d,c=%d" % (D.a,D.b,D.c))

class Prant:
    def show(self):
        print("父类方法")
class Chiad(Prant):
    def show(self):
        super().show()
        print("子类方法")

obj= Chiad()
obj.show()


class Prant1:
    def show(self):
        print("父类方法-1")
class Prant2:
    def show(self):
        print("父类方法-2")
class Chiad1(Prant1,Prant2):
    def show(self):
        super().show()
        print("子类方法")
obj1= Chiad1()
obj1.show()


class Prant3:
    def __init__(self,name):
        self.name = name
class Chiad2(Prant3):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

obj3= Chiad2('Alan',18)
print(obj3.name,obj3.age)
    

class Prant4:
    def show(self):
        print("父类方法")
class Chiad4(Prant4):
    def show(self):
        super().show()
        print("子类方法")
obj4 = Chiad4()
obj4.show()
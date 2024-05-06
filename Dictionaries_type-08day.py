##字典是无序的、可修改的（可变的）成对（键：值）数据类型的集合
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(dct['key1'])
print(person['address']['street']) #我们可以通过引用它的键名来访问字典项。
print(dct.get('key1')) #通过get()方法，我们可以通过键名来访问字典项。
dct['key5'] = 'value5'
print(dct) #我们可以向字典中添加新的键值对
person['skills'].append('Java')
print(person['skills']) 
dct['key1'] = 'value-one'
print(dct['key1'])  #更改键值对
print('key1' in dct)  ##判断键值对是否存在
###删除键值对
del dct['key1'] ###删除指定键值对
print(dct)
dct.pop('key2')##删除指定键值对
print(dct)
dct.popitem() ##删除最后一个键值对
print(dct)
dct.clear()  ##清空键值对
print(dct)
print(person.items()) ##items（）方法将字典更改为元组列表
person_copy = person.copy()
print(person_copy)   ###我们可以使用copy（）方法复制字典。使用复制可以避免对原始字典的变异。
person = person.values()
print(person)  ###values（）方法将字典更改为值列表
person_copy = person_copy.keys()
print(person_copy)   ###keys（）方法将字典更改为键列表


####练习
dog = {
    'name': '小黑',
    'color': '黑色',
    'breed': '拉布拉多',
    'owner': '小明',
}
student = {
    'name': '小明',
    'age': 18,
    'sex': '男',
    'score': 100,
}
print(len(student))
print(type(student['age']))
student['number'] = '1000'
dog['num'] = '200'
dog_copy = dog.copy()
dog = dog.values()
print(dog)
student_copy = student.copy()
student = student.keys()
print(student)
print(dog_copy.items())
student_copy.pop('name')
student_copy.clear()
print(student_copy)
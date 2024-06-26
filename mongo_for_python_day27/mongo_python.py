from flask import Flask, render_template
import os
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
MONGODB_URL = 'mongodb://root:12345@localhost:30002/'
client = pymongo.MongoClient(MONGODB_URL)
print(client.list_database_names())
db = client.thirty_day_of_python
#db.student.insert_one({'name': 'Mike', 'age': 23})
student = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for students in student:
    db.student.insert_one(students)
#print(client.list_database_names())
#first_student = db.student.find_one() #find_one()方法返回第一个文档
#first_student = db.student.find_one({'_id':ObjectId('667a705b053e7eb137c9817c')}) #更据返回的id查文档
#first_student = list(db.student.find()) ##使用list方法返回所有文档
'''query = {
    'name':'Sami' #更据条件查找
}'''
'''query = {'name':'David',
         'city':'London'
         }'''
query = {'name':'David'}

#first_students = db.student.find(query)
delete_result = db.student.delete_one(query)
deleted_count = delete_result.deleted_count
print(f"根据查询条件，已删除 {deleted_count} 个文档。")
remaining_students = list(db.student.find())
for student in remaining_students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 30003))
    app.run(debug=True,host='0.0.0.0', port=port)
   


    

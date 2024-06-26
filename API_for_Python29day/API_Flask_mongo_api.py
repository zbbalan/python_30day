from flask import Flask,Response, request
from bson import ObjectId
#import datetime
import json
import os
import pymongo
from bson.json_util import dumps
from datetime import datetime


app = Flask(__name__)
MONGODB_URL = 'mongodb://root:12345@localhost:30002/'
client = pymongo.MongoClient(MONGODB_URL)
db = client['thirty_day_of_python']

@app.route('/api/v1.0/student',methods=['GET'])
def student():
    all_students = list(db.student.find())
    for student in all_students:
        student['_id'] = str(student['_id'])
   # print(all_students)
    return Response(json.dumps(all_students),mimetype='application/json')

@app.route('/api/v1.0/student/<id>',methods=['GET'])
def single_student (id):
    student = db.student.find({'_id':ObjectId(id)})
    return Response(dumps(student),mimetype='application/json')

@app.route('/api/v1.0/student',methods=['POST'])
def create_student():
    name = request.form.get('name')
    country = request.form.get('country')
    city = request.form.get('city')
    skills = request.form('skills')
    bio = request.form.get.get('bio')
    birthyear = request.form['birthyear']
    created_at = datetime.datetime.now()
    student = {
        'name':name,
        'country':country,
        'city':city,
        'skills':skills,
        'bio':bio,
        'birthyear':birthyear,
        'created_at':created_at
    }
    db.students.insert_one(student)
    return ;
#def update_student(id):
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True,host='0.0.0.0', port=5001)

#报错werkzeug.exceptions.BadRequestKeyError: 400 Bad Request: The browser (or proxy) sent a request that this server could not understand.
KeyError: 'name'
    ##报错from flask import Flask,Response, request
from bson import ObjectId
#import datetime
import json
import os
import pymongo
from bson.json_util import dumps
from datetime import datetime


app = Flask(__name__)
MONGODB_URL = 'mongodb://root:12345@localhost:30002/'
client = pymongo.MongoClient(MONGODB_URL)
db = client['thirty_day_of_python']

@app.route('/api/v1.0/student',methods=['GET'])
def student():
    all_students = list(db.student.find())
    for student in all_students:
        student['_id'] = str(student['_id'])
   # print(all_students)
    return Response(json.dumps(all_students),mimetype='application/json')

@app.route('/api/v1.0/student/<id>',methods=['GET'])
def single_student (id):
    student = db.student.find({'_id':ObjectId(id)})
    return Response(dumps(student),mimetype='application/json')

@app.route('/api/v1.0/student',methods=['PUT'])
def create_student():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(',')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.datetime.now()
    student = {
        'name':name,
        'country':country,
        'city':city,
        'skills':skills,
        'bio':bio,
        'birthyear':birthyear,
        'created_at':created_at
    }
    db.students.insert_one(student)
    return ;
#def update_student(id):
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True,host='0.0.0.0', port=5001)


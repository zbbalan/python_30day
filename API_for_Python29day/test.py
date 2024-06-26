
from flask import Flask,  Response
import json
import pymongo
import os


app = Flask(__name__)

#
MONGODB_URI='mongodb://root:12345@localhost:30002/'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_day_of_python'] # accessing the database

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(students), mimetype='application/json')


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
from flask import Flask, Response
import json
import os
app = Flask(__name__)
@app.route('/api/v1.0/hello_world',methods=['GET'])
def hello_world():
    hello_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(hello_list), mimetype='application/json')
    

if __name__ == '__main__':
    prot = os.environ.get('PORT')
    app.run(host='0.0.0.0', port=2008)
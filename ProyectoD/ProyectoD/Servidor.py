from flask import Flask, jsonify, request, Response
from flask_cors import CORS 

app= Flask(__name__)
CORS(app)

@app.route('/nombre',methods=['GET'])
def getDatos():
  return "yo puedo"


if __name__== '__main__':
    app.run(host='0.0.0.0',debug=True, port=4000)


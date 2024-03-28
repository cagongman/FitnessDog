from flask import Flask, request, jsonify
import os


def StartVideo(name, val):
    print(name, type(name))
    print(val, type(val))

    if val:
        print("true!")
    else:
        print("false!")


app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_data():
    data = request.json
    variable_name = data['name']
    value = data['value']
    
    print(f"Received: {variable_name} = {value}")
    
    if variable_name == "start":
        StartVideo(variable_name, value)
    # ...

    return jsonify({"message": "Data received successfully!"})

@app.route('/test')
def hello_world():
    return '<h1>Hello World!</h1><input type="textbox"/>'

if __name__ == '__main__':
    # run server!!
    app.run(host='0.0.0.0', port=5000)

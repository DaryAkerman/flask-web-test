from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/age', methods=['GET'])
def get_age():
    return jsonify({'age': 22})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
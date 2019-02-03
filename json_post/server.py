from flask import Flask, request

app = Flask(__name__)

@app.route("/data",  methods=['POST'])
def data():
    data = request.json
    name = data['name']
    age = data['age']
    print('Name: ', name)
    print('Age: ', age)
    return name + '_' + str(age)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug = True, port=1000)

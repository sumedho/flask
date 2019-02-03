from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calc", methods=['GET','POST'])
def calc():
    if request.method == 'POST':
        result = request.form
        username = result['username']
        number_a = float(result['number_a'])
        number_b = float(result['number_b'])
        answer = number_a * number_b
        print(username, number_a, number_b)
        return render_template('result.html', username = username, answer = answer)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug = True, port=1000)

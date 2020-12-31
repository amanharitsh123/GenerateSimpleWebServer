from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello0():
	return "Hello from /!"
@app.route('/abc/xyz')
def hello1():
	return "Hello from /abc/xyz!"
@app.route('/custom/')
def hello2():
	return "Hello from /custom/!"
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80)

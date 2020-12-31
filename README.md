# Generate Simple flask webserver with custom Endpoints
This is a simple python script that can generate a small flask application with the urls specified in the urls.txt file.
For example:
if the urls.txt file has this content.
```
/
/abc/xyz
/custom/
```
You can edit the urls.txt file to add the endpoints you want.

After running main.py
```
python main.py
```

An output folder ./webapp will be generated which has 3 files:

```
app.py
requirements.txt
Dockerfile
```

Content of app.py will be like this:

```
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
```

Here functions hello0(), hello1(), hello2() are handling different urls specified in the urls.txt file earlier.

The generated webapp is dockerized, so inorder to build an image and the container from the image use the below commands.


```
cd ./webapp
sudo docker build -t my_image .
sudo docker run -d -p 80:80 my_image
```

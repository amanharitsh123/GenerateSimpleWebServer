class Generator:
    def __init__(self):
        self.header = 'from flask import Flask\napp = Flask(__name__)'
        self.footer = '''if __name__ == '__main__':\n\tapp.run(host="0.0.0.0", port=80)'''
        self.endpoints = '''@app.route('{path}')\ndef hello{number}():\n\treturn "Hello from {path}!"''' 

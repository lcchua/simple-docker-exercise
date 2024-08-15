import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	sys_username = os.getlogin()
	message = f"Hello, {sys_username}!"
	return message

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)

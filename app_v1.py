import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
#	message = "Hello Mary to the world! (app_v1)"
	message = "Hello Mary to the universe! (app_v1)"
#	message = "Hello Mary to the galaxy! (app_v1)"
	return message

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)

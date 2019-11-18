from flask import Flask
from flask import request
import requests

app = Flask(__name__)

ip = #endir

@app.route('/posts',methods=['POST'])
def createMarkers():
	content = request.get_json()
	r = requests.post(url="http://"+ip+":4444/posts",json=content)
	return r.json()

@app.route('/',methods=['GET'])
def markers():
	r = requests.get(url="http://"+ip+":4444/")
	return r.json()[0]




if __name__ == "__main__":

	app.run("0.0.0.0")

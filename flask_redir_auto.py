
from flask import Flask
from flask import request
from flask.json import jsonify
import requests

app = Flask(__name__)

ip = #end

@app.route('/posts',methods=['POST'])
def createMarkers():
        content = request.get_json()
        r = requests.post(url="http://"+str(ip)+"/posts",json=content)
        return jsonify(r.json())

@app.route('/',methods=['GET'])
def markers():
        r = requests.get(url="http://"+str(ip)+"/")
        return jsonify(r.json())


@app.route('/healthcheck',methods=['GET'])
def healthcheck():
        return jsonify({"state":"good"})



if __name__ == "__main__":

        app.run(host="0.0.0.0")


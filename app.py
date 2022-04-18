#Python App to run chatbot 

from urllib import response
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
   return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #TODO: check if text is valid 
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

#Used to host and direct IP address
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")

from flask import Flask, render_template,url_for
import requests
from flask import request as req


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarization",methods=["GET","POST"])
def Summarize():
        if req.method=="POST":
            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
            headers = {"Authorization": "Bearer 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"}
            

            data = req.form["data"]
            minValue = 10
            maxValue =int(req.form["inputValue"])
            
            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

           
            Output = query({
            "inputs": data,
            "parameter": {"min_length": minValue, "max_length": maxValue},
            })[0]
            return render_template('index.html',result=Output['summary_text'])
        else:
            return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()


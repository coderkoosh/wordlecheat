from flask import Flask
from datetime import datetime
import json
from urllib import request

app = Flask(__name__)


@app.route("/")
def wordlecheat():
    dt = datetime.now()
    link = "https://www.nytimes.com/svc/wordle/v2/" + dt.strftime("%Y-%m-%d") + ".json"
    urlopen = request.urlopen(link)
    data = urlopen.read()
    js = json.loads(data)
    #print(f"Solution: \n{js['solution']}\nEditor: \n{js['editor']}")    
    return f"<p>Solution: {js['solution']} Editor: {js['editor']}<p/>"

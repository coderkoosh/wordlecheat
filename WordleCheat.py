from datetime import datetime
import json
from urllib import request
# This imports everything and the code below gets the time
dt = datetime.now()

#Creates the link and formats dt

link = "https://www.nytimes.com/svc/wordle/v2/" + dt.strftime("%Y-%m-%d") + ".json"

# Creates requests the data

urlopen = request.urlopen(link)

# Reads the data

data = urlopen.read()

# jsonread = json.loads(data)

# Makes the json into a python dict

js = json.loads(data)

# Print from the dict

print(f"Solution: \n{js['solution']}\nEditor: \n{js['editor']}")

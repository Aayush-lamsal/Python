# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template

import json





# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the applic
# ation which URL should call 
# the associated function.
@app.route('/')
def hello_world():
	
    dif={
		"my student names":["hari","ram","shyam","Ayush"],
		"details":[{"hari":[{"subject1":123}]},{"shyam":[{"subject1":23423}]}]
    }
    dif=json.dumps(dif)
    return render_template("indes.html",dif=dif)

# main driver function
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)

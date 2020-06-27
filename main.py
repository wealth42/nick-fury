# Imports
from flask import Flask, render_template
from get_data import main


app = Flask(__name__)

# Routing in Flask to render "index.html" template
@app.route("/")
def index():
	data = main()[0] # Now 'data' variable contains the Pandas DataFrame df
	info = main()[1]
	length = len(data)
	return render_template("index.html", data=data,length=length, info=info)


# Running the Flask Application
if __name__ == '__main__':
	app.run(debug=True)

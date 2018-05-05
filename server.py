import random
import time
from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = "yellowsparrow231"




@app.route("/")
def index():
	x = int(random.randrange(0,101))
	session["randKey"] = x
	print(session["randKey"])
	return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
	print(session["randKey"])
	while int(request.form["box"]) != session["randKey"]:
		if int(request.form["box"]) > session["randKey"]:
			print ("Too darn High")
			return render_template("index.html")
		else:
			print ("Too Low")
			return render_template("index.html")
		session.pop(randKey)
	return redirect("/")

	
if __name__ == "__main__":
	app.run(debug=True)
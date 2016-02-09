from flask import Flask, render_template

app=Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
	return render_template("index.html", title="Home")

@app.route("/about")
def about():
	return render_template("about.html", title="About")

@app.route("/works")
def works():
	return render_template("works.html", title="Works")

if __name__ == "__main__":
	app.run()
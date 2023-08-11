# flask app for the project relationg to art integration

# Imports
from flask import *

# Flask app
app = Flask("Art-Integration-MA4")

# Define path ways
app.static_folder = "./static"
app.template_folder = "./templates"

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/credits")
def credits():
    return render_template("credits.html")

@app.route("/compare")
def compare():
    return render_template("compare.html")

@app.route("/ContactUs")
def ContactUs():
    return render_template("contact.html")

# Run webserver
def run_webserver():
    app.run(host='0.0.0.0', debug=True, port=8082)

if __name__ == "__main__":
    run_webserver()
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
    return render_template("home.html")


# Run webserver
def run_webserver():
    app.run(debug=True, port=5004)

if __name__ == "__main__":
    run_webserver()
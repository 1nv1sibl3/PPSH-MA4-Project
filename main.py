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

@app.route("/feedback")
def ContactUs():
    return render_template("feedback.html")


# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# MAHARASHTRA and its sub topics
@app.route("/MH/")
def MH_etymology():
    return render_template("MH/etymology.html")

@app.route("/MH/history")
def MH_history():
    return render_template("MH/history.html")

@app.route("/MH/geography")
def MH_geography():
    return render_template("MH/geography.html")

@app.route("/MH/governance")
def MH_governance():
    return render_template("MH/governance.html")

@app.route("/MH/culture")
def MH_culture():
    return render_template("MH/culture.html")

@app.route("/MH/media")
def MH_media():
    return render_template("MH/media.html")

@app.route("/MH/education")
def MH_education():
    return render_template('MH/education.html')

@app.route("/MH/cuisine")
def MH_cuisine():
    return render_template('MH/cuisine.html')

@app.route("/MH/sports")
def MH_sports():
    return render_template('MH/sports.html')

@app.route("/MH/tourism")
def MH_tourism():
    return render_template('MH/tourism.html')


# Run webserver
def run_webserver():
    app.run(host='0.0.0.0', debug=True, port=8080)#, ssl_context=('/home/invisible/ppsh/ssl/ppshinjewadi.me.crt' , '/home/invisible/ppsh/ssl/ppshinjewadi.me.key'))

if __name__ == "__main__":
    run_webserver()
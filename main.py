# flask app for the project relationg to art integration

# Imports
from flask import *
import json
import os
from datetime import datetime

def save_feedback(feedback_data):
    feedback_file_path = './templates/feedbacks.json'

    if not os.path.exists(feedback_file_path):
        with open(feedback_file_path, 'w') as f:
            json.dump([], f)

    with open(feedback_file_path, 'r') as f:
        existing_data = json.load(f)

    feedback_data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    existing_data.append(feedback_data)

    with open(feedback_file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)

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
    return render_template("contact.html")

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    feedback = request.form.get('feedback')
    
    feedback_data = {
        'name': name,
        'feedback': feedback
    }

    save_feedback(feedback_data)
    return render_template("feedback_submitted.html", submitted=True)


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


# SIKKIM ROUTES and ITS SUB TOPICS
@app.route("/SK/")
def SK_etymology():
    return render_template("SK/etymology.html")

@app.route("/SK/history")
def SK_history():
    return render_template("SK/history.html")

@app.route("/SK/geography")
def SK_geography():
    return render_template("SK/geography.html")

@app.route("/SK/governance")
def SK_governance():
    return render_template("SK/governance.html")

@app.route("/SK/culture")
def SK_culture():
    return render_template("SK/culture.html")

@app.route("/SK/media")
def SK_media():
    return render_template("SK/media.html")

@app.route("/SK/education")
def SK_education():
    return render_template('SK/education.html')

@app.route("/SK/cuisine")
def SK_cuisine():
    return render_template('SK/cuisine.html')

@app.route("/SK/sports")
def SK_sports():
    return render_template('SK/sports.html')

@app.route("/SK/tourism")
def SK_tourism():
    return render_template('SK/tourism.html')


# Run webserver
def run_webserver():
    app.run(host='0.0.0.0', debug=True, port=8082, ssl_context=('/home/invisible/ppsh/ssl/ppshinjewadi.me.crt' , '/home/invisible/ppsh/ssl/ppshinjewadi.me.key'))

if __name__ == "__main__":
    run_webserver()
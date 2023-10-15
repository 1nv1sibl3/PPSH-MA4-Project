# flask app for the project relationg to art integration

# Imports
from flask import *
import json
import os
from datetime import datetime

HARDCODED_USERNAME = 'admin'
HARDCODED_PASSWORD = 'Omp@12345'

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
app.secret_key = "Inv1s1bl3-the-great"

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

# Hindi links
# MAHARASHTRA and its sub topics
@app.route("/MH/hn")
def MH_hn_etymology():
    return render_template("MH_hn/etymology.html")

@app.route("/MH/history/hn")
def MH_hn_history():
    return render_template("MH_hn/history.html")

@app.route("/MH/geography/hn")
def MH_hn_geography():
    return render_template("MH_hn/geography.html")

@app.route("/MH/governance/hn")
def MH_hn_governance():
    return render_template("MH_hn/governance.html")

@app.route("/MH/culture/hn")
def MH_hn_culture():
    return render_template("MH_hn/culture.html")

@app.route("/MH/media/hn")
def MH_hn_media():
    return render_template("MH_hn/media.html")

@app.route("/MH/education/hn")
def MH_hn_education():
    return render_template('MH_hn/education.html')

@app.route("/MH/cuisine/hn")
def MH_hn_cuisine():
    return render_template('MH_hn/cuisine.html')

@app.route("/MH/sports/hn")
def MH_hn_sports():
    return render_template('MH_hn/sports.html')

@app.route("/MH/tourism/hn")
def MH_hn_tourism():
    return render_template('MH_hn/tourism.html')


# SIKKIM ROUTES and ITS SUB TOPICS
@app.route("/SK/hn")
def SK_hn_etymology():
    return render_template("SK_hn/etymology.html")

@app.route("/SK/history/hn")
def SK_hn_history():
    return render_template("SK_hn/history.html")

@app.route("/SK/geography/hn")
def SK_hn_geography():
    return render_template("SK_hn/geography.html")

@app.route("/SK/governance/hn")
def SK_hn_governance():
    return render_template("SK_hn/governance.html")

@app.route("/SK/culture/hn")
def SK_hn_culture():
    return render_template("SK_hn/culture.html")

@app.route("/SK/media/hn")
def SK_hn_media():
    return render_template("SK_hn/media.html")

@app.route("/SK/education/hn")
def SK_hn_education():
    return render_template('SK_hn/education.html')

@app.route("/SK/cuisine/hn")
def SK_hn_cuisine():
    return render_template('SK_hn/cuisine.html')

@app.route("/SK/sports/hn")
def SK_hn_sports():
    return render_template('SK_hn/sports.html')

@app.route("/SK/tourism/hn")
def SK_hn_tourism():
    return render_template('SK_hn/tourism.html')

# ADMIN

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
            session['logged_in'] = True
            return redirect('/admin')
        else:
            return "Invalid username or password"

    return render_template('login.html')

@app.route('/logout')
def logout():

    session['logged_in'] = False
    return redirect('/')

@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    with open('./templates/feedbacks.json', 'r') as f:
        feedback_data = json.load(f)

    return render_template('admin.html', feedback_entries=feedback_data)


# Run webserver
def run_webserver():
    app.run(host='0.0.0.0', debug=False, port=8082, ssl_context=('/home/invisible/ppsh/ssl/ppshinjewadi.me.crt' , '/home/invisible/ppsh/ssl/ppshinjewadi.me.key'))

if __name__ == "__main__":
    run_webserver()

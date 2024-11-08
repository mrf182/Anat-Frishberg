from flask import app, render_template, Flask

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # חשוב להגדיר SECRET_KEY


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")  # מעביר את הרשימה לעמוד

port_number = 3000
if __name__ == '__main__':
    app.run(port=port_number)

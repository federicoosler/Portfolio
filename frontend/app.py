from flask import Flask, render_template
from flask_mail import Mail
from routes.contacto import contacto_bp

from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

app.register_blueprint(contacto_bp)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

app.secret_key = os.getenv('SECRET_KEY')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/proyectos")
def pagina_proyectos():
      return render_template("proyectos.html")

@app.route("/sobre_mi")
def pagina_sobre_mi():
      return render_template("sobre_mi.html")

@app.route("/contacto")
def pagina_contacto():
      return render_template("contacto.html")

if __name__ == "__main__":
       app.run(debug=True,port = 5001)

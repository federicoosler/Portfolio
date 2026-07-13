from flask import Flask, render_template
#from routes.servicios_extra import servicios_extra_bp

app = Flask(__name__) 

#app.register_blueprint(servicios_extra_bp)

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

from flask import Flask, render_template
#from routes.servicios_extra import servicios_extra_bp

app = Flask(__name__) 

#app.register_blueprint(servicios_extra_bp)

@app.route("/")
def home():
    return render_template("index.html")
    
if __name__ == "__main__":
       app.run(debug=True,port = 5001)

from flask import Blueprint,redirect,request, current_app, flash
from services.email import enviar_email
from flask_mail import Mail

contacto_bp = Blueprint('contacto', __name__)

@contacto_bp.route('/contacto', methods=['POST'])
def envio_email():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']
    mail=Mail(current_app)

    enviar_email(nombre,email,mensaje,mail)
    flash("Mensaje enviado correctamente")
    return redirect("/contacto")
from flask_mail import Message
import os

def enviar_email(nombre,mensajero_email,mensaje,mail):
    msg = Message('Nuevo mensaje de contacto', sender=os.getenv('MAIL_SENDER'), recipients=[os.getenv('MAIL_RECEIVER')])
    msg.body = f'De: {nombre}, {mensajero_email} \n Mensaje: {mensaje}'
    mail.send(msg)
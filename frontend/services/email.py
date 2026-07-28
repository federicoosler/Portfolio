from flask_mail import Message

def enviar_email(nombre,mensajero_email,mensaje,mail):
    msg = Message('Nuevo mensaje de contacto', sender='federicoosler549@gmail.com', recipients=['federicoosler549@gmail.com'])
    msg.body = f'De:{nombre},{mensajero_email} \n Mensaje:{mensaje}'
    mail.send(msg)

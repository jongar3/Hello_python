import smtplib
from email.message import EmailMessage
import random

# Configuración
my_email_gmail = "jongarcicuevas@gmail.com"
my_password = "XXX"  # Reemplaza con tu contraseña real
my_email_yahoo = "jongarcicuevas@yahoo.com"

frases = [
    "¡Hola! Espero que tengas un buen día 😊",
    "Este es un mensaje de prueba desde Python con ñ y tildes: acción, corazón, camión.",
    "Prueba automática: mañana, año, español.",
]

# Crear mensaje
msg = EmailMessage()
msg["Subject"] = "Saludos desde Python"
msg["From"] = my_email_gmail
msg["To"] = my_email_yahoo
msg.set_content(random.choice(frases))  # Maneja UTF-8 automáticamente

# Enviar
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(my_email_gmail, my_password)
    connection.send_message(msg)

print("Correo enviado correctamente.")

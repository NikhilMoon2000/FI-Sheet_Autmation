import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import pywhatkit

# =======================
# CONFIGURATION
# =======================
ALERT_MSG = "⚠️ Alert: Something needs your attention!"

# Email settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "youremail@gmail.com"
SENDER_PASSWORD = "your_app_password"  # use App Password, not your main one
RECEIVER_EMAIL = "targetemail@gmail.com"

# Twilio (SMS)
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_token"
FROM_PHONE = "+1234567890"  # Twilio number
TO_PHONE = "+9198xxxxxxxx"  # Your number

# WhatsApp
WHATSAPP_NUMBER = "+9198xxxxxxxx"


# =======================
# FUNCTIONS
# =======================

def send_email_alert(message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = "Python Alert"
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("✅ Email alert sent!")
    except Exception as e:
        print("❌ Failed to send email:", e)


def send_sms_alert(message):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=FROM_PHONE,
            to=TO_PHONE
        )
        print("✅ SMS alert sent!")
    except Exception as e:
        print("❌ Failed to send SMS:", e)


def send_whatsapp_alert(message):
    try:
        pywhatkit.sendwhatmsg_instantly(WHATSAPP_NUMBER, message, wait_time=10)
        print("✅ WhatsApp message sent!")
    except Exception as e:
        print("❌ Failed to send WhatsApp:", e)


# =======================
# MAIN ALERT LOGIC
# =======================
def trigger_alert():
    send_email_alert(ALERT_MSG)
    send_sms_alert(ALERT_MSG)
    send_whatsapp_alert(ALERT_MSG)


if __name__ == "__main__":
    trigger_alert()

import smtplib
import time
import RPi.GPIO as GPIO
from email.mime.text import MIMEText

GPIO.setmode(GPIO.BCM)
moisture_pin = 17
GPIO.setup(moisture_pin, GPIO.IN)

sender = "your_email@gmail.com"
password = "your_app_password"
receiver = "3160189098@qq.com"

def read_moisture():
    return GPIO.input(moisture_pin)

def send_email(status):
    if status == "low":
        body = "Soil moisture is too low. Please water the plant."
        subject = "Plant Watering Alert - ACTION NEEDED"
    else:
        body = "Soil moisture is adequate. No watering needed."
        subject = "Plant Status Check - All Good"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

while True:
    moisture_level = read_moisture()
    if moisture_level == 0:
        send_email("low")
    else:
        send_email("ok")
    time.sleep(3600)

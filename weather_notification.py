import requests
import smtplib
from email.message import EmailMessage
import schedule
import time
# Configuration
EMAIL_USERNAME =  "your@email.com"
EMAIL_PASSWORD =   "yourpassword"  # or your actual email password if using less secure apps
RECIPIENT_EMAIL = "recipient@gmail.com"



def send_weather_notification():
    city = "city"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=yourapikey&units=metric"
    
    # Rest of your code for fetching weather data and creating email content
    response = requests.get(url)
    weather_data = response.json()

    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]

    notification_title = "Weather Forecast"
    notification_text = f"Temperature: {temperature}°C\nDescription: {description}"

    # Set up email notification
    msg = EmailMessage()
    msg.set_content(notification_text)
    msg["Subject"] = notification_title
    msg["From"] = EMAIL_USERNAME
    msg["To"] = RECIPIENT_EMAIL

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com") as smtp:
        smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        smtp.send_message(msg)

# Schedule the email to be sent every day at 16:00 (4:00 PM)
schedule.every().day.at("8:00").do(send_weather_notification)

while True:
    schedule.run_pending()
    time.sleep(1)

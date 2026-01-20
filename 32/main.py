# whtasapp msg send

import pywhatkit as kit
import datetime

def send_whatsapp_msg():
    phone_number = "+91 9999999999"

    message = "Hello! This is an automated message."

    now = datetime.datetime.now()

    send_hour = now.hour
    send_minute = now.minute + 2

    print(f"Scheduling message to send at {send_hour}:{send_minute}.")

    try:
        kit.sendwhatmsg(phone_number,message,send_hour,send_minute)
        print("Message sent success..")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    send_whatsapp_msg()
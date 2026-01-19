import pywhatkit as kit
import datetime

def send_whatsapp_msg():
    # Target phone number (with country code) and message
    phone_number = "+919408961050"  # Example number
    message = "Hello! This is an automated message for Day 32 of my Python challenge. 🐍"

    # Get the current time
    now = datetime.datetime.now()
    
    # Schedule for 2 minutes from now
    send_hour = now.hour
    send_minute = now.minute + 2

    print(f"Scheduling message to {phone_number} at {send_hour}:{send_minute}...")

    try:
        # This will open the web browser and send the message automatically
        kit.sendwhatmsg(phone_number, message, send_hour, send_minute)
        print("✅ Message scheduled successfully!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    send_whatsapp_msg()
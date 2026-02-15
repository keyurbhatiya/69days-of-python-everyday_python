import speech_recognition as sr

def listen_to_sir():
    # 1. Initialize the recognizer
    recognizer = sr.Recognizer()

    # 2. Use the system microphone as the source
    with sr.Microphone() as source:
        print("\n🎤 Listening... (Speak now, Sir)")
        
        # Adjust for ambient noise for better accuracy
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            print("🤖 Recognizing...")
            # 3. Using Google Web Speech API (Free & Accurate)
            text = recognizer.recognize_google(audio)
            print(f"✅ You said: {text}")
            
            # Simple Command Logic
            if "hello" in text.lower():
                print("👋 Hello Sir! How can I help you today?")
            elif "exit" in text.lower():
                print("🔒 Shutting down voice systems...")
                return False

        except sr.UnknownValueError:
            print("❌ Sorry Sir, I couldn't understand the audio.")
        except sr.RequestError:
            print("❌ Network error. Please check your internet.")
            
    return True

if __name__ == "__main__":
    active = True
    while active:
        active = listen_to_sir()
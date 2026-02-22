# Build Your Personal JARVIS Assistant 🤖 (Day 65)
# pip install SpeechRecognition pyttsx3 groq python-dotenv pyaudio

import speech_recognition as sr
import pyttsx3
import os
import datetime
import webbrowser
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# --- Groq AI Client ---
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# --- Text-to-Speech Engine ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)  # speaking speed

# Try to use a good voice (index 1 is often female/clearer on Windows)
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)


def speak(text):
    """Convert text to speech."""
    print(f"🤖 JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to microphone and convert speech to text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            print(f"👤 You: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            print("   ❌ Could not understand audio")
            return ""
        except sr.RequestError:
            print("   ❌ Speech recognition service unavailable")
            return ""


def ask_ai(prompt):
    """Get AI response from Groq."""
    try:
        completion = client.chat.completions.create(
            model="Llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are JARVIS, a personal AI assistant inspired by Iron Man's JARVIS. "
                        "You are polite, witty, and helpful. Address the user as 'Sir'. "
                        "Keep responses concise (2-3 sentences max) since they will be spoken aloud."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"I apologize Sir, I encountered an error: {str(e)}"


def handle_command(command):
    """Process voice commands and take action."""

    # --- Time ---
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}, Sir.")

    # --- Date ---
    elif "date" in command or "today" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {today}, Sir.")

    # --- Open Websites ---
    elif "open youtube" in command:
        speak("Opening YouTube for you, Sir.")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google, Sir.")
        webbrowser.open("https://google.com")

    elif "open github" in command:
        speak("Opening GitHub, Sir.")
        webbrowser.open("https://github.com")

    elif "open instagram" in command:
        speak("Opening Instagram, Sir.")
        webbrowser.open("https://instagram.com")

    # --- Google Search ---
    elif "search" in command:
        query = command.replace("search", "").replace("for", "").strip()
        if query:
            speak(f"Searching Google for {query}, Sir.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What would you like me to search for, Sir?")

    # --- System Info ---
    elif "who made you" in command or "who created you" in command:
        speak("I was created as a Day 65 project in the 69 Days of Python series, Sir. Inspired by the legendary JARVIS from Iron Man!")

    elif "your name" in command:
        speak("I am JARVIS, your personal AI assistant, Sir. Just A Rather Very Intelligent System!")

    # --- Goodbye ---
    elif "goodbye" in command or "bye" in command or "stop" in command or "exit" in command:
        speak("Goodbye, Sir. It was a pleasure assisting you. Have a great day!")
        return False

    # --- AI Response (anything else) ---
    else:
        speak("Let me think about that, Sir...")
        response = ask_ai(command)
        speak(response)

    return True


# --- Main Loop ---
def main():
    print("=" * 60)
    print("🤖 J.A.R.V.I.S — Personal AI Assistant | Day 65")
    print("   Just A Rather Very Intelligent System")
    print("=" * 60)

    speak("JARVIS online. Good day, Sir. How may I assist you?")

    running = True
    while running:
        print("\n" + "-" * 40)
        print("Say 'Jarvis' to activate or speak a command...")
        command = listen()

        if not command:
            continue

        # Wake word activation (optional — can respond to any command)
        if "jarvis" in command:
            command = command.replace("jarvis", "").strip()
            if not command:
                speak("Yes, Sir? I'm listening.")
                command = listen()
                if not command:
                    continue

        if command:
            running = handle_command(command)

    print("\n✅ JARVIS shutdown complete.")


if __name__ == "__main__":
    main()

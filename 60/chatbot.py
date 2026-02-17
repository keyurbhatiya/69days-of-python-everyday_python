# Build a Desktop AI Chatbot in Python! 🤖 (Day 60)

import customtkinter as ctk
from groq import Groq
import threading
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class JarvisChatbot(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Jarvis AI - Day 60")
        self.geometry("500x600")
        ctk.set_appearance_mode("dark")

        # --- UI LAYOUT ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Chat Display area
        self.chat_display = ctk.CTkTextbox(self, state="disabled", corner_radius=10)
        self.chat_display.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Input Area Frame
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")

        self.user_input = ctk.CTkEntry(self.input_frame, placeholder_text="Ask me anything, Sir...")
        self.user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", lambda event: self.send_message())

        self.send_button = ctk.CTkButton(self.input_frame, text="Send", width=80, command=self.send_message)
        self.send_button.pack(side="right")

    def append_message(self, role, message):
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"{role}: {message}\n\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")

    def send_message(self):
        prompt = self.user_input.get()
        if not prompt: return

        self.append_message("You", prompt)
        self.user_input.delete(0, "end")

        # Use threading so the UI doesn't freeze
        threading.Thread(target=self.get_ai_reply, args=(prompt,), daemon=True).start()

    def get_ai_reply(self, prompt):
        try:
            completion = client.chat.completions.create(
                model="Llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are Jarvis, a helpful desktop assistant. Address the user as Sir."},
                    {"role": "user", "content": prompt}
                ]
            )
            response = completion.choices[0].message.content
            self.append_message("Jarvis", response)
        except Exception as e:
            self.append_message("System", f"Error: {e}")

if __name__ == "__main__":
    app = JarvisChatbot()
    app.mainloop()
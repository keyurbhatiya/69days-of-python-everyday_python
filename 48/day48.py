import customtkinter as ctk

# 1. System Settings
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("Everyday Python - Day 48")
        self.geometry("400x300")

        # 2. UI Elements (Widgets)
        self.label = ctk.CTkLabel(self, text="Welcome back, Sir!", font=("Roboto", 24))
        self.label.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter your project name...")
        self.entry.pack(pady=10)

        self.button = ctk.CTkButton(self, text="Launch Project", command=self.button_callback)
        self.button.pack(pady=20)

        self.appearance_switch = ctk.CTkSwitch(self, text="Dark Mode", command=self.toggle_mode)
        self.appearance_switch.pack(pady=10)
        self.appearance_switch.select() # Start with switch ON

    # 3. Logic Functions
    def button_callback(self):
        project = self.entry.get()
        print(f"🚀 Launching: {project}")
        self.label.configure(text=f"Project: {project}")

    def toggle_mode(self):
        if self.appearance_switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

if __name__ == "__main__":
    app = App()
    app.mainloop()
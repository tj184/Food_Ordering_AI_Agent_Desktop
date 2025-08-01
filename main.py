import tkinter as tk
import threading
from voice_agent import VoiceAgent

class MayaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maya - Your Voice Assistant")
        self.root.geometry("400x200")
        self.agent = VoiceAgent()

        self.label = tk.Label(root, text="Click the button and say 'Maya'", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.listen_button = tk.Button(root, text="Start Listening", command=self.start_listening, font=("Helvetica", 12))
        self.listen_button.pack(pady=10)

        self.status_label = tk.Label(root, text="", font=("Helvetica", 10), fg="green")
        self.status_label.pack(pady=10)

    def start_listening(self):
        self.status_label.config(text="Listening...")
        threading.Thread(target=self.process_audio).start()

    def process_audio(self):
        result = self.agent.listen_for_command()
        if result == "WAKE":
            self.status_label.config(text="Hello! Maya is now active.")
            print("Wake word detected!")
        else:
            self.status_label.config(text=f"Heard: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MayaApp(root)
    root.mainloop()

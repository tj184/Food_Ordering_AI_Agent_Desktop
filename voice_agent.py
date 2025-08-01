import speech_recognition as sr

class VoiceAgent:
    def __init__(self, wake_word="maya"):
        self.recognizer = sr.Recognizer()
        self.wake_word = wake_word.lower()

    def listen_for_command(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
        try:
            command = self.recognizer.recognize_google(audio).lower()
            print(f"Recognized: {command}")
            if self.wake_word in command:
                return "WAKE"
            return command
        except sr.UnknownValueError:
            return "Could not understand"
        except sr.RequestError:
            return "API unavailable"

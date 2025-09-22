import speech_recognition as sr
import webbrowser
import pyttsx3
from WebBrowser_links import web_links , music_links
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

try:
    if __name__ == "__main__":
        speak("Initiating Jarvis...")
        while True:
            # STEP 1: Listen for wake word, which is "Jarvis"
            with sr.Microphone() as source:
                print("Say 'Jarvis' to activate...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    wake_word = recognizer.recognize_google(audio).lower()
                    print(f"You said (wake word check): {wake_word}")
                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    continue
                wake_variants = ["jarvis", "jervis", "jarbis", "jarbiss", "javis", "javis", "jar", "jer"] 
                if any(word in wake_word for word in wake_variants):
                    speak("Yes")
                    time.sleep(0.5)
                    print("Did he say Yes?")

                # STEP 2: Listen for actual command
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    try:
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio).lower()
                        print(f"Command: {command}")
                    except sr.UnknownValueError:
                        speak("Sorry, I didn't catch that.")
                        continue
                    except sr.WaitTimeoutError:
                        continue

                # STEP 3: Match command with web_links and music_links
                opened = False
                for web_name, web_link in web_links.items():
                    if web_name.lower() in command:
                        webbrowser.open(web_link)
                        speak(f"Opening {web_name}")
                        opened = True
                        break
                
                for music_name, music_link in music_links.items():
                    if music_name.lower() in command:
                        webbrowser.open(music_link)
                        speak(f"Playing {music_name}")
                        opened = True
                                
                if not opened:
                    print("No matching website found.")

except KeyboardInterrupt:
    speak("Shutting down. Goodbye.")

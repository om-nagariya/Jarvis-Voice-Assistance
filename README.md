# Jarvis - Virtual Assistant

Jarvis is a simple Python-based voice assistant that uses **speech recognition** and **text-to-speech** to interact with users.  
It can open websites, play music, and respond to predefined voice commands.

---

## 🚀 Features
- Activates on the wake word **"Jarvis"**.
- Opens popular websites like YouTube, Google, GitHub, etc.
- Plays music tracks via YouTube links.
- Provides voice responses using `pyttsx3`.

---

## 📂 Project Structure
├── main.py # Main script for running Jarvis
├── WebBrowser_links.py # Contains website and music links
├── README.md # Documentation
├── requirements.txt # Python dependencies
├── .gitignore # Ignore unnecessary files
└── LICENSE # MIT License

---

## 🛠️ Installation
Install the required dependencies:
```bash
pip install -r requirements.txt

 Note:
You also need PyAudio for speech recognition.

## 🪟 On Windows:
pip install pipwin
pipwin install pyaudio

---
On Linux/macOS:
sudo apt-get install portaudio19-dev
pip install pyaudio

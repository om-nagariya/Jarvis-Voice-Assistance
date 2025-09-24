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
```yaml
├── main.py # Main script for running Jarvis
├── WebBrowser_links.py # Contains website and music links
├── README.md # Documentation
├── requirements.txt # Python dependencies
├── .gitignore # Ignore unnecessary files
└── LICENSE # MIT License
```
---

## 🛠️ Installation
Install the required dependencies:
```bash
pip install -r requirements.txt
```
### Note:
You also need PyAudio for speech recognition.

### 🪟 On Windows:
```bash
pip install pipwin
pipwin install pyaudio
```

### 🐧 On Linux/macOS:
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

---

## ▶️ Usage:

### 1. Clone this repository:
```bash
git clone https://github.com/om-nagariya/Jarvis-Voice-Assistance.git
cd jarvis-assistant

```

### 2. Run the assistant:
```bash
python main.py
```

### 3. Say "Jarvis" to activate, then speak your command.
#### Example commands:

**• "_Open YouTube_"**<br>
**• "_Open GitHub_"**<br>
**• "_Play gigachad_"**<br>

---

## **🔗 Customization**
**To add or edit websites/music, modify WebBrowser_links.py:**
```bash
web_links = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
}

music_links = {
    "softcore": "link_to_music"
    "your_fav_music": "link_to_music"
}

```

## **⚠️ Known Issues**

**• Speech recognition may misinterpret commands if background noise is high.**<br>
**• PyAudio installation can be tricky on some systems.**<br>
**• Currently no NLP, so commands must match exactly with `WebBrowser_links.py`.**<br>

---

## 📄 **License**

This project is licensed under the **MIT License**.  
```yaml
MIT License

Copyright (c) 2025 OM Nagariya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

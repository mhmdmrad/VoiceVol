# 🎙 VoiceVol – Voice-Controlled Volume Adjuster

VoiceVol is a Python-based voice assistant that allows you to control your system's volume using simple voice commands. Say "increase volume," "decrease volume," "mute," or "max volume" to adjust your sound settings hands-free!

## 🚀 Features
- ✅ **Increase or decrease volume** using voice commands
- ✅ **Mute or set to max volume** instantly
- ✅ **Hands-free control** for a seamless experience
- ✅ **Uses SpeechRecognition and Pycaw** for speech-to-text and audio control

## 🛠 Requirements
Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- `speechrecognition`
- `pycaw`
- `comtypes`
- `pyaudio`

### Install Dependencies
Run the following command to install the required libraries:
```bash
pip install speechrecognition pycaw comtypes pyaudio
```

## ▶️ How to Use
1. Run the script:
   ```bash
   python voicevol.py
   ```
2. Speak one of the following commands:
   - **"Increase volume"** – Increases volume by 25%
   - **"Decrease volume"** – Decreases volume by 25%
   - **"Mute"** – Sets volume to 0%
   - **"Max volume"** – Sets volume to 100%
3. Enjoy hands-free audio control!

## ⚙️ How It Works
- The script uses `speech_recognition` to capture voice input from your microphone.
- It then processes the speech and converts it into text using Google Speech Recognition.
- Based on the recognized command, it adjusts the system volume using `pycaw`.

---
🚀 **Developed by [Mohammad Mrad]**

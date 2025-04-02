import speech_recognition as sr
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

# Initialize the audio interface
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Function to change volume
def change_volume(amount):
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(0.0, min(1.0, current_volume + amount))
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    print(f"Volume changed to {int(new_volume * 100)}%")

# Voice recognition function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'increase volume' or 'decrease volume'...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")

        if "increase" in command:
            change_volume(0.25)  # Increase by 25%
        elif "decrease" in command:
            change_volume(-0.25)  # Decrease by 25%
        elif "mute" in command:
            volume.SetMasterVolumeLevelScalar(0.0, None)  # Mute
            print("Muted volume")
        elif "max" in command:
            volume.SetMasterVolumeLevelScalar(1.0, None)  # Max volume
            print("Volume set to 100%")
        else:
            print("Command not recognized")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Speech recognition service error")

# Run the voice control loop
while True:
    recognize_speech()
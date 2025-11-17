import speech_recognition as sr
import os

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")

        if "run my script" in command:
            os.system("uirelated.py")  # Replace with your script name
        else:
            print("Command not recognized.")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Could not request results; check your internet connection.")

listen_for_command()

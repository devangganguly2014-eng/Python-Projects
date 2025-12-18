import speech_recognition as sr
import win32com.client
from openai import OpenAI
import datetime
import os
import subprocess

# ================== OPENAI ==================
client = OpenAI(
    api_key="Paste Your API Key here"

def chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are J.A.R.V.I.S, a smart voice assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


# ================== VOICE (WINDOWS) ==================
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    print("JARVIS:", text)
    speaker.Speak(text)


# ================== LISTEN ==================
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        return ""


# ================== MAIN ==================
speak("Jarvis is online. How can I help you Today?")

while True:
    command = listen()

    if command == "":
        continue

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
        continue

    if "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye sir")
        break

    reply = chatgpt_response(command)
    speak(reply)

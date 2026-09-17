import shutil

import speech_recognition as sr
import pyaudio
from prompt_toolkit import prompt
import webbrowser
import pyttsx3
import os
import platform
import subprocess
import sys
import ollama
import urllib

mode= "text"

def ollamaai(prompt):  # <-- Changed { to :
    try:
        stream = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}],
            stream=True
        )
        
        # <-- Added proper indentation here
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
            
        print() # <-- Prints a blank line after the AI finishes so your next terminal prompt is clean

    except Exception as e:
        print(f"\nError communicating with Ollama: {e}")
        print("Make sure the Ollama app is running locally and the 'llama3' model is installed.")

def listen():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening... Speak now.")

            # Capture the audio
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=10)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            
            # Allow the user to edit the transcribed text in the terminal
            edited_text = prompt("You said (edit if needed, then press Enter): ", default=text)
            
            return edited_text

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; check your internet connection. Error: {e}")
            
    except Exception as e:
        print(f"Failed to access the microphone: {e}")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    # Wait for the speech to finish
    engine.runAndWait()

def process(com):
    global mode
    os_name = sys.platform

    if not com or not isinstance(com, str):
        print("Invalid command")
        return
    
    token = com.split()
    if len(token) < 2:
        print("Not enough arguments")
        return
    
    # Normalize action to lowercase for safer matching
    action = token[0].lower()
    target = " ".join(token[1:])
    
    if action in ["open", "run", "search"]:
        
        if len(token) == 2 and action != "search":
            # 1. Attempt to launch local application
            app_launched = False
            
            try:
                if os_name == "win32":
                    # os.startfile is native, safer, and doesn't require shell=True
                    try:
                        os.startfile(target)
                        app_launched = True
                    except FileNotFoundError:
                        pass # Let it fall through to the web fallback

                elif os_name == "darwin":
                    # Use run() to check the exit code. 'open' returns > 0 if app isn't found.
                    result = subprocess.run(["open", "-a", target], capture_output=True)
                    if result.returncode == 0:
                        app_launched = True

                elif os_name.startswith("linux"):
                    # Use shutil.which to verify the binary exists in PATH
                    if shutil.which(target):
                        # Use Popen to launch without blocking the Python script
                        subprocess.Popen([target])
                        app_launched = True

                else:
                    raise NotImplementedError(f"Unsupported OS: {os_name}")

                # 2. Handle Success or Fallback to Website
                if app_launched:
                    print(f"Successfully launched {target} on {platform.system()}")
                else:
                    url = f"https://{target}.com"
                    print(f"App '{target}' not found. Opening {url}")
                    webbrowser.open(url)

            except Exception as e:
                print(f"Failed to launch application: {e}")

        else:
            # Multi-word or explicit "search" command
            # Safely encode the search query (converts spaces and special chars)
            safe_target = urllib.parse.quote(target)
            search_url = f"https://www.bing.com/search?q={safe_target}"
            print(f"Searching for: {target}")
            webbrowser.open(search_url)

    elif action == "change" and token[1] == "mode":
            if len(token) > 2 and token[2] in ["speak", "text"]:
                mode = token[2]
                print(f"Mode changed to {mode}.")
            else:
                print("Error: Please specify a valid mode ('speak' or 'text').")
            
    else:
        ollamaai(com)


if __name__ == "__main__":
    speak("Hello, Neelesh")
    
    while True:
        # 1. Gather input based on the current mode
        if mode == "speak":
            t = listen()
        elif mode == "text":
            t = input("Prompt: ")
        else:
            print("Error: Unknown mode.")
            break
            
        # Optional: Handle case where listen() might return None if it didn't hear anything
        if not t:
            continue 

        # 2. Check for exit command or process the input
        if t.lower() == "stop":  # .lower() makes it case-insensitive
            break
        else:
            process(t)


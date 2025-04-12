import speech_recognition as sr
import webbrowser
import pyttsx3
import json
from google import genai
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
#https://www.youtube.com/results?search_query=
def mcrecognizer(platform,url):
     with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            try:
                audio = recognizer.listen(source)
                query = recognizer.recognize_google(audio)
                print(f"{platform} search query: {query}")
                
                # Encode the query and construct the URL
                search_url = f"{url}{query}"
                webbrowser.open(search_url)
                speak(f"Searching {platform} for {query}")
                
            except sr.UnknownValueError:
                speak("I couldn't understand your search query.")
                print(f"Could not understand the {platform} search query.")
            except sr.RequestError as e:
                print(f"Request error: {e}")

def processcommand(c):
    if "open google" in c.lower():
          webbrowser.open("https://www.google.com/")

    elif "open youtube" in c.lower():
          webbrowser.open("https://www.youtube.com/")

    elif "search" in c.lower() and "youtube" in c.lower():
        # Extract the query
        speak("What do you want to search on YouTube?")
        print("Listening for YouTube search query...")
        
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            try:
                audio = recognizer.listen(source)
                query = recognizer.recognize_google(audio)
                print(f"YouTube search query: {query}")
                
                # Encode the query and construct the URL
                search_url = f"https://www.youtube.com/results?search_query={query}"
                webbrowser.open(search_url)
                speak(f"Searching YouTube for {query}")
                
            except sr.UnknownValueError:
                speak("I couldn't understand your search query.")
                print("Could not understand the YouTube search query.")
            except sr.RequestError as e:
                print(f"Request error: {e}")
        # mcrecognizer("youtube","https://www.youtube.com/results?search_query=")

    elif "search" in c.lower() and "google" in c.lower():
          speak("What do you want to search on google?")
          print("Listening for google search query...")
        #   with sr.Microphone() as source:
        #         recognizer = sr.Recognizer()
        #         try:
        #             audio = recognizer.listen(source)
        #             query = recognizer.recognize_google(audio)
        #             print(f"YouTube search query: {query}")
                    
        #             # Encode the query and construct the URL
        #             search_url = f"https://www.google.com/search?q={query}"
        #             webbrowser.open(search_url)
        #             speak(f"Searching YouTube for {query}")

        #         except sr.UnknownValueError:
        #             speak("I couldn't understand your search query.")
        #             print("Could not understand the YouTube search query.")wr1
        #         except sr.RequestError as e:
        #             print(f"Request error: {e}")
          mcrecognizer("Google","https://www.google.com/search?q=")

    elif "open" in c.lower() and "linkedin" in c.lower():
            webbrowser.open("https://www.linkedin.com")

    elif "open" in c.lower() and "facebook" in c.lower():
          webbrowser.open("https://www.facebook.com")
        
    elif "open" in c.lower() and "instagram" in c.lower():
            webbrowser.open("https://www.instagram.com")

    else:
            client = genai.Client(api_key="AIzaSyAH8p2aV54Zl4HzbLgX8NE4FSTKmiPz6-Q")
            response = client.models.generate_content( model="gemini-2.0-flash", contents= c)
            print(str(response.text))
            speak("task done. what's next sir?")
            
            
# main program

if __name__  == "__main__":
    speak("initializing jarvis.....")
    while True:
        # obtain audio from the microphone 
        r = sr.Recognizer()
        print("recognizing...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source,duration = 1)
                print("listening...")   
                audio = r.listen(source,phrase_time_limit=3,timeout=2)
            # storing recognized data in command variable 
                command = r.recognize_google(audio)
                print(command)
            if "jarvis" in command.lower() :
                speak("yes sir") 
                print("recognized")

                with sr.Microphone() as source:
                    
                    print("listening...")
                    audio = r.listen(source, phrase_time_limit=6)
                    command = r.recognize_google(audio)
                    processcommand(command)
                # listen from commandS
        except sr.UnknownValueError:
                    print("Could not understand audio.")
        except sr.RequestError as e:
                    print(f"Request error from Google Speech Recognition API: {e}")
        except Exception as e:
                    print(f"Unexpected error: {e}")


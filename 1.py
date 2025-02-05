import webbrowser
import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)
            print(f"Voice Input: {query}")
            return query
        except sr.UnknownValueError:
            print("Could not understand audio, try again!")
        except sr.RequestError:
            print("Could not request results, check your internet connection!")

def open_youtube():
    print("Choose input method:\n1. Text Input\n2. Voice Input")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        query = input("Enter what you want to watch on YouTube: ")
    elif choice == "2":
        query = get_voice_input()
        if not query:
            return
    else:
        print("Invalid choice! Exiting.")
        return

    print(f"Opening YouTube for: {query}")
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)

open_youtube()

YouTube Search Using Voice and Text


This Python program allows users to search YouTube by either typing a query or speaking it aloud. It provides two input methods, and the program opens the browser with the search results for the entered query.


Features:

Text Input: Allows users to manually type their query to search on YouTube.
Voice Input: Users can speak their query, and the program will recognize the voice and open YouTube with the search results.
Error Handling: Handles errors like unclear voice input or connectivity issues.
Web Browser Integration: Opens YouTube directly in your default web browser with the search results.
Installation
Clone this repository or download the code to your local machine.

bash
Copy
Edit
git clone https://github.com/yourusername/youtube-search-voice-text.git
Navigate to the project directory.


Install the required dependencies:


bash
Copy
Edit
pip install SpeechRecognition webbrowser
Usage


Run the Python script.


bash
Copy
Edit
python youtube_search.py
The program will prompt you to choose between Text Input or Voice Input.


For Text Input:

Simply type your query and press Enter to search YouTube.
For Voice Input:


Click or press Enter, then speak your query clearly when prompted.
The program will process your speech and show the corresponding query.
The script will then open YouTube in your default browser with the search results for the given query.


Example:

bash
Copy
Edit


Choose input method:


1. Text Input
2. Voice Input
Enter 1 or 2: 1
Enter what you want to watch on YouTube: Python tutorials
Opening YouTube for: Python tutorials


Requirements:
Python 3.x
Internet connection for speech recognition and opening YouTube.
License
This project is licensed under the MIT License - see the LICENSE file for details.



Acknowledgements:
This project uses SpeechRecognition for voice recognition and webbrowser to open URLs.

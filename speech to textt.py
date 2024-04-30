import speech_recognition as sr
import tkinter as tk

def convert_speech_to_text(language='en-US'):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Transcribing...")
        text = r.recognize_google(audio, language=language)
        print("Text: " + text)
        text_label.config(text="Text: " + text)  # Update the label with the transcribed text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        text_label.config(text="Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Sorry, my speech recognition service is currently unavailable.")
        text_label.config(text="Speech recognition service is unavailable.")

def on_language_selected():
    language_choice = language_var.get()

    if language_choice == '1':
        language_code = 'en-US'
    elif language_choice == '2':
        language_code = 'hi-IN'
    elif language_choice == '3':
        language_code = 'mr-IN'
    else:
        print("Invalid choice. Defaulting to English.")
        language_code = 'en-US'

    # Converting speech to text
    convert_speech_to_text(language=language_code)

# Create the GUI window
window = tk.Tk()
window.title("Speech to Text Converter")

# Language selection
language_label = tk.Label(window, text="Please select a language:")
language_label.pack()

language_var = tk.StringVar(window, '1')
language_radio1 = tk.Radiobutton(window, text="English", variable=language_var, value='1')
language_radio2 = tk.Radiobutton(window, text="Hindi", variable=language_var, value='2')
language_radio3 = tk.Radiobutton(window, text="Marathi", variable=language_var, value='3')
language_radio1.pack()
language_radio2.pack()
language_radio3.pack()

# Convert button
convert_button = tk.Button(window, text="Convert", command=on_language_selected)
convert_button.pack()

# Text label to display the converted text
text_label = tk.Label(window, text="")
text_label.pack()

# Run the GUI
window.mainloop()

import speech_recognition as sr
import pyttsx3
import openai
import google.generativeai as palm

# Initialize Text-to-Speech engine
def init_tts():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    return engine

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()

# Recognize speech input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("There was an error with the speech recognition service.")
        return ""

# Chat with OpenAI GPT
def chat_with_gpt(prompt):
    
    openai.api_key = ""  # Replace with your OpenAI API key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        message = response['choices'][0]['message']['content']
        return message
    except Exception as e:
        return f"Error in GPT response: {e}"

# Use Google PaLM API for advanced generative tasks
def palm_interaction(prompt):
    palm.configure(api_key="AIzaSyDqjNmBa4Xc7oRafD7w2KHjI1B2JJ-ce6k")  # Replace with your Google PaLM API key
    try:
        response = palm.generate_text(prompt=prompt)
        return response.result
    except Exception as e:
        return f"Error in PaLM response: {e}"

# Main assistant logic
def main():
    tts_engine = init_tts()
    speak(tts_engine, "Hello, how can I assist you today?")

    while True:
        user_input = listen()
        if user_input.lower() in ["exit", "quit"]:
            speak(tts_engine, "Goodbye!")
            break

        if "Google" in user_input:
            response = palm_interaction(user_input)
        else:
            response = chat_with_gpt(user_input)

        print(f"Assistant: {response}")
        speak(tts_engine, response)

if __name__ == "__main__":
    main()

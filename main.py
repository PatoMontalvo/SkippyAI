import speech_recognition as sr
import pyttsx3
import openai
import os

#Initializing pyttsx3
listening = True
engine = pyttsx3.init()

#Get environment variable to set the openai api key
openai.api_key = os.getenv("OPENAI_API_KEY")

#Customizing the chatgpt role
messages = [{"role": "system", "content": "Your name is Skippy and give answers in 2 lines"}]

#Customizing The output voice
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

#Changing voice
engine.setProperty('voice', voices[1].id)

#Test the voice
engine.say("Hello World!")
engine.runAndWait()
engine.stop()


def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


while listening:
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = 3000

        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5.0)
            response = recognizer.recognize_google(audio)
            print(response)
           
            if "skippy" in response.lower():
           
                response_from_openai = get_response(response)
                print(response_from_openai)
                engine.setProperty('rate', 120)
                engine.setProperty('volume', volume)
                engine.setProperty('voice', 'greek')
                engine.say(response_from_openai)
                engine.runAndWait()
               
           
               
            else:
                print("Didn't recognize 'skippy'.")
           
        except sr.UnknownValueError:
            print("Didn't recognize anything.")

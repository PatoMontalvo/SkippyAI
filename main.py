import speech_recognition as sr
import pyttsx3
import openai

#Initializing pyttsx3
listening = True
engine = pyttsx3.init()

#Set your openai api key and customizing the chatgpt role
#openai.api_key = "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" # David
openai.api_key = "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" # Sebas
messages = [{"role": "system", "content": "Your name is Skippy and give answers in 2 lines"}]

#Customizing The output voice
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
#Changing voice
engine.setProperty('voice', voices[1].id)

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
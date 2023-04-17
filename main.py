import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Configurar o reconhecimento de voz
r = sr.Recognizer()

# Configurar a síntese de voz
engine = pyttsx3.init()

# Definir a voz padrão
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# Definir a assistente virtual
def assistant(text):
    if "Olá Tina" in text:
        speak("Olá senhor trajano, como posso ajudar?")
    elif "que horas são" in text:
        now = datetime.datetime.now()
        speak("São " + str(now.hour) + " horas e " + str(now.minute) + " minutos.")
    elif "pesquise por" in text:
        query = text.replace("pesquise por", "")
        speak("Pesquisando por " + query)
        wikipedia.set_lang("pt")
        results = wikipedia.summary(query, sentences=2)
        speak(results)
    else:
        speak("Desculpe, não entendi o que você disse.")


# Definir a função para sintetizar a voz
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Configurar o microfone
with sr.Microphone() as source:
    print("Ouvindo...")
    audio = r.listen(source)

    try:
        print("Processando...")
        text = r.recognize_google(audio, language="pt-BR")
        print("Você disse: {}".format(text))
        assistant(text)
    except:
        print("Desculpe, não consegui entender o que você disse.")

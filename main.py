import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os


audio = sr.Recognizer()
cerebro = pyttsx3.init()
cerebro.say("Olá Doutor Trajano, Bem vindo!")
cerebro.say("Como posso ajudar o senhor?")
cerebro.runAndWait()

vozes = cerebro.getProperty("voices")
cerebro.setProperty("voz", vozes[1].id)


def executa_comando():
    try:
        with sr.Microphone(2) as source:
            print("Ouvindo..")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            if "Samira" in comando:
                comando = comando.replace("Samira", "")
                cerebro.say(comando)
                cerebro.runAndWait()

    except:
        print("Microfone não está ok")

    return comando


def comando_voz_usuario():
    comando = executa_comando()
    if "horas" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        cerebro.say("Agora são" + hora)
        cerebro.runAndWait()
    elif "procure por" in comando:
        procurar = comando.replace("procure por", "")
        wikipedia.set_lang("pt")
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        cerebro.say(resultado)
        cerebro.runAndWait()
    elif "toque" in comando:
        musica = comando.replace("toque", "")
        resultado = pywhatkit.playonyt(musica)
        cerebro.say("Tocando música")
        cerebro.runAndWait()
    elif "desligar o computador" in comando:
        os.system("shutdown /s /t 5")
        cerebro.say("Desligando Computador")
        cerebro.runAndWait()


comando_voz_usuario()

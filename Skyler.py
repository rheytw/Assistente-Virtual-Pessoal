import pyttsx3
import datetime

texto_fala = pyttsx3.init()

def falar(audio):
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate",175) #alteração de velocidade da fala
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice',voices[2].id) #alteração de voz
    texto_fala.say(audio)
    texto_fala.runAndWait()

def tempo_e_data():
    agora = datetime.datetime.now()
    tempo = agora.strftime("%I:%M")
    dia = agora.day
    mes = agora.month
    ano = agora.year
    falar(f"Agora são {tempo}. Hoje é dia {dia} do mês {mes} de {ano}")

def bem_vindo():
    agora = datetime.datetime.now()
    tempo = agora.strftime("%I:%M")
    dia = agora.day
    mes = agora.month
    ano = agora.year
    falar(f"Oie mestre. Bem vindo de volta! Agora são {tempo}. Hoje é dia {dia} do mês {mes} de {ano}")

    hora = datetime.datetime.now()

    if hora >= 6 and hora <12:
        falar(f"bom dia mestre!")
    elif hora >= 12 and hora < 18:
        falar(f"boa tarde mestre!")
    elif hora >= 18 and hora <=24:
        falar(f"boa noite mestre!")
    else:
        falar(f"Ta estudando ou ta jogando? Vamo criar um sistemas?")
    
    falar(f"Skaíler a sua disposição! prontinha pra te ajudar Parker!")

bem_vindo()



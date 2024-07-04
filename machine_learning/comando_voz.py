print("Testando...")

import speechd_recognition as sr 
import os

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuario
    microfone = sr.Recognizer()

    #usando o micrfone
    with sr.Microphone() as source:

        #Chama um algoritmo de redução de ruidos no som
        microfone.ajust_for_ambient_noise(source)

        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        #Armazena o que foi dito numa variavel 
        audio = microfone.listen(source)
    
    try:

        #Passa a variavel para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio,language='pt-br')

        if "navegador" in frase:
            os.system("start Chrome.exe")
            return False

        elif "Excel" in frase:
            os.system("start Excel.exe")
            return False
        
        elif "PowerPoint" in frase:
            os.system("start POWERPNT.exe")
            return False

        elif "Fechar" in frase:
            os.system("exit")
            return True

        print("Você disse: " + frase)

    except sr.UnkownValueError:
        print("Não entendi")

    return frase

while True:
    if ouvir_microfone():
        break

    
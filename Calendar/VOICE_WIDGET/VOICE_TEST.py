import speech_recognition as sr
from WIDGJETS.services.apointmentClass import createNewApointment
from WIDGJETS.services.data.auxFunctions.auxFunctions import SumHours
#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    #return "marcar massagem dia 16 do 2 de 2023 às 14:20 durante 20 minutos"
 #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
    #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source,10)
    try:
    #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-PT')
    #Após alguns segundos, retorna a frase falada
        print("Você disse: " + frase)
        return frase
    #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except:
        print("Não entendi")
def createNewApointmentVoice():
    actionSTR = ouvir_microfone()
    words = actionSTR.split(" ")
    day = getDayMonthYearVoice(words)
    typeOfService = getTypeOfServiceVoice(words)
    print(typeOfService)
    time= getServiceTime(words)
    beggining = getBeggining(actionSTR,words)
    finish = SumHours(time,beggining)       
    newApointment = createNewApointment(day,typeOfService,time,beggining,finish)
    ##fazer com que apareça uma mensagem de voz ou de texto a confirmar a marcação

def getTypeOfServiceVoice(wordsSplited):


    # Find the index of "py"
    index = wordsSplited.index("marcar")
    typeOfService = wordsSplited[index + 1]
    # Get the word that comes after "py"
    return typeOfService

def getDayMonthYearVoice(wordsSplited):


    # Find the index of "py"
    index = wordsSplited.index("dia")

    # Get the word that comes after "py"
    day = wordsSplited[index+1]
    month = wordsSplited[index+3]
    year = wordsSplited[index+5]

    return day + "-" + month + "-" + year
def getBeggining(sentece,wordsSplited):

    # Find the index of "py"
    if "às" in sentece:
        index = wordsSplited.index("às")
    elif "as" in sentece:
        index = wordsSplited.index("as")
    else: 
        print("begginig Not Found")
        return
    # Get the word that comes after "py"
    beggining = wordsSplited[index+1]
    print(beggining)
    return beggining
def getServiceTime(wordsSplited):

    index = wordsSplited.index("minutos")
    time = wordsSplited[index-1]
    print("00:"+time)

    return "00:"+time
    
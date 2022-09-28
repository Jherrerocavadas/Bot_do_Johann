import speech_recognition as Speech
import pyttsx3


class TTS():

    def __init__(self):#, voz, voices):
        self.voz = pyttsx3.init()
        self.voices = self.voz.getProperty('voices')

        #self.voz = voz
        #self.voices = voices


    def Bot_fala(self, texto='texto padrão'):
        self.voz.say(texto)#Voz pt br do teste = Letícia-F123
        self.voz.runAndWait()

    def Bot_ouve(self):#Resolver depois

        # Recog = Speech.Recognizer()
        #
        # with Speech.Microphone() as Mic:
        #     while True:
        #         Audio = Recog.listen(Mic)
        #         print(Recog.recognize_google(Audio, language='pt'))#Reconhecimento de voz online
        pass

    def Bot_debug(self):
        # print(self.voices)
         for voice in self.voices:
              print(f'voice.name = {voice.name}')
              print(f'voice.id = {voice.id}')
              print(f'voice.language = {voice.languages}')
              print(f'voice.gender = {voice.gender}')
              print(f'voice.age = {voice.age}')

         print('***************<Configurações gerais>***************')
         print(f'Volume: {self.voz.getProperty("volume")}')
         print(f'Taxa de fala: {self.voz.getProperty("rate")} palavras por minuto')


              #for x in range(3):
                #print(f'voices[{x}].name = {self.voices[x].name}')
            #  if(voice.name == 'Letícia-F123'):
            #       print(self.voz.setProperty('voice', voice.id))
                #print(f'voices[{x}].id = {self.voices[x].id}')

    def Config(self, **kwargs):#não detecta se a voz estiver escrita errada
        voz_modelo = kwargs.get('voice')
        volume = kwargs.get('volume')
        taxa_fala = kwargs.get('rate')

        if(voz_modelo!= None):
            for voice in self.voices:
                 if(voice.name == voz_modelo):
                      self.voz.setProperty('voice', voice.id)

        if(volume!= None):
            if(volume >=0.0 and volume <=1.0):
                self.voz.setProperty('volume', volume)
            else:
                print("Insira um valor de volume entre 0,0 e 1,0")

        if(taxa_fala!= None):
            self.voz.setProperty('rate', taxa_fala)

        self.voz.runAndWait()#pra validar todos os valores


#para fins de teste da classe
if __name__ == '__main__':
    print('Modo debug')
    Debug = TTS()

    Debug.Bot_debug()
    Debug.Config(voice='Letícia-F123', rate=175)
    Debug.Bot_fala('Salve meu mano, tudo certinho com vossa pessoa?')

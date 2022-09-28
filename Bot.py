from tkinter import *
from tkinter import ttk
import os
import json

#import re
from Modulos import TTS,Teste,Teams #síntese de voz do programa(BETA)
#import Bot_voice #síntese de voz do programa(BETA)
#import Bot_Janela #Classe do Tkinter

#importar os módulos do Bot
#import Teste
#import Teams

#Inicialização dos componentes
Bot_voice = TTS.TTS()

#Ver de colocar as configurações no arquivo config Json
Bot_voice.Config(voice='Letícia-F123', rate=175, volume =0.7)


#Função dos Botões:

def Sair():
    print("Encerrando programa...")#Terminal
    Bot_voice.Bot_fala('Encerrando programa...')
    Bot_app.destroy()

def Ajuda():
    print("Ajuda")
    Bot_voice.Bot_fala('Você selecionou o modo de ajuda.')
    Bot_voice.Bot_fala('Eu lhe mostrarei alguns comandos.')
    Bot_voice.Bot_fala('Menti fofo! Esse botão ainda não está implementado com os comandos')


def run():
    #Reiniciar = True
    Comando = Comando_input.get().lower()#Receber os comandos digitados
    print(Programas['values'])#printar os módulos a serem selecionados

    #Ver de colocar essa lista de comandos em algum json ou algo do tipo
    if(Comando == "executar"):
        isRestart = Configurar()#Reiniciar)
        print(isRestart)#Terminal
        #while(isRestart == "Restart"):
    #    isRestart = Configurar()#Reiniciar)

    elif(Comando == "resetar dados"):
    #    Reiniciar = False
        Reset()#Reiniciar)

    else:
        Bot_voice.Bot_fala('Comando não reconhecido. Por favor, tente novamente')
        print("Comando não reconhecido")#Terminal
        error_status(Comando_input,'Entry','Error.Bot.TEntry','Comando não reconhecido')



def error_status(Elemento, Element_type, style='', texto = ''):
    #Talvez nem precisasse de Element_type, mas enfim
    if(style ==''):#pra rodar a biblioteca padrão
        compara = [#Basicamente uma AND de quatro entradas(pq tudo tem que dar true. Diferente=true,nesse caso)
        Element_type != "ProgressBar",
        Element_type != "Scale",
        Element_type != "Scrollbar",
        Element_type != "Treeview"
        ]
        if all(compara):
                style =f'Bot.T{Element_type}'
                print("TESTANDO")#teste
                print(style)#teste
        else:#BETA
            style =f'Bot.{Element_type}'
            print("TESTANDO")#teste
            print(style)#teste

    Elemento['style'] = style
    if(texto != ''):
        #Elemento.clear()
        Elemento.insert(0,texto)
        #Elemento_status.set(texto)


def reset_text_entry():#tentar juntar em alguma outra função
    Comando = Comando_input.get().lower()
    if(Comando.startswith('Comando não reconhecido')):#provisório
         Element_status.set('')
         print("Cmd not recog")#Terminal



#ver de melhorar essa atribuição de módulos e comandos
def exec_modulo(Dados_salvos, modulo):
        print("Executando {} \n".format(modulo))
        if(modulo == "Teste"):
            Bot_voice.Bot_fala('Executando módulo de testes')
            Teste.run(Bot_app)
        elif(modulo == "Teams.Assignment"):
            Bot_voice.Bot_fala('Executando módulo de tarefas do ("Tins")')#("palavras 'aportuguesadas' para fala do bot")
            Teams_Tarefas = Teams.Teams_resources(Bot_app)
            Teams_Tarefas.run()
        #elif(modulo == "NOVOS_MODULOS")
            #NOVOS_MODULOS.run()
        else:
            Bot_voice.Bot_fala('Módulo não encontrado')
            print("Módulo não encontrado")#Terminal
            return "ModuloNotFound"




def Configurar():#Reiniciar):#comando executar
    Comando_input['style'] = 'Bot.TEntry' #Voltar a cor do entry ao normal
    error_status(Comando_input,'Entry')
    def Enter_Config(mod): #Usada no Botão
        global User
        global Senha
        User = User_input.get()
        Senha = Senha_input.get()
        print(f'User {User} e Senha {Senha}')
        Cadastro.destroy()

        #Salvar Dados no arquivo json de UserData
        with open("Data/UserData.json", "r+") as Data_User:
            try:
                Data_json = json.load(Data_User)
            except:
                pass

            #Salva os dados do módulo
            Data_json[mod] = {}
            Data_json[mod]["User"] = User
            Data_json[mod]["Senha"] = Senha
            #mod

        with open("Data/UserData.json", 'w') as Data_User:
            Data_User.write("")

            json.dump(Data_json, Data_User, indent = 3)

        #Diz ao programa que existem dados salvos para aquele modulo agora
        #Tá executando o 'insira módulo novamente'
        ler[mod]["Dados_salvos"] = True #definir pros manos abaixo
        modulo = ler[mod]["Modulo"] #definir pros manos abaixo

        with open("Data/Config.json", 'w') as Config:
            Config.write("")

            #adiciona ler na Config com indentação organizada
            json.dump(ler, Config, indent = 3)

        #executar o módulo após a configuração
        exec_app = exec_modulo(ler[mod]["Dados_salvos"], modulo)#Dados salvos é necessário?
        while(exec_app == "ModuloNotFound" ):
            #print("não achou")

            mod = Programas.get()
            while(mod == " "):
                pass

            exec_app = exec_modulo(ler[mod]["Dados_salvos"], modulo)#Dados salvos é necessário?
            Bot_voice.Bot_fala('Deseja executar outro módulo?')



    try:  #criação do arquivo de dados, se não existir
        with open("Data/UserData.json", "x") as Criar:
            pass
    except:
        pass


    with open("Data/Config.json", 'r+') as Config:
        ler = json.load(Config)

        #print("Módulos existentes: {}".format(ler.keys()))
        Programas["values"] = [*ler]
        mod = Programas.get()
        print(mod)#Teste
        #while(mod == ""):#amigão não funfa, por conta do loop do tkinter
            #mod = Programas.get()

        if(mod == "voltar"):
            pass #implementar um retorno à aba de comandos depois
        try:
        #Rola uma exceção aqui, pq mod não existe
            modulo = ler[mod]["Modulo"]
            Dados_salvos = ler[mod]["Dados_salvos"]
        except KeyError:
            print("SEM")#Terminal
            modulo = None #Valor padrão
            Dados_salvos = None #Valor padrão


        #Dados da aplicação encontrados
        if(Dados_salvos == None):
            print("Exceção do amigão sendo criada")#terminal

        elif(Dados_salvos == True):
            #Sendo executado novamente quando coloca os dados
            exec_app = exec_modulo(Dados_salvos, modulo)

            #Ver de colocar isso numa função
            while(exec_app == "ModuloNotFound" ):
                print("Erro no módulo")

                mod = Programas.get()
                while(mod == " "):
                    pass
                #mod = input("Insira o módulo a ser executado: ")
                modulo = ler[mod]["Modulo"]
                Dados_salvos = ler[mod]["Dados_salvos"]
                exec_app = exec_modulo(Dados_salvos, modulo)

            Bot_voice.Bot_fala('Deseja executar outro módulo?')

        #Dados da aplicação não existem
    #    elif(Dados_salvos == False): #com o valor de none dá loop
        else:

            Bot_voice.Bot_fala('Dados de usuário não encontrados para essa aplicação!')
            print("Dados de usuário não encontrados para essa aplicação!")
            Cadastro = Toplevel(Bot_app)
            Cadastro.title("Cadastro dados")
            Cadastro.configure(background = '#373737')#OK
            Cadastro.resizable(0,0)
            Cadastro_header = ttk.Frame(Cadastro, style='Bot.TFrame')#frame para inserir dados do cabeçalho
            #formato: Programa_header
            frame1_1 = ttk.Frame(Cadastro, style='Bot.TFrame')
            frame2_1 = ttk.Frame(Cadastro, style='Bot.TFrame')
            frame3_1 = ttk.Frame(Cadastro, style='Bot.TFrame')

            Cadastro_header.pack()
            frame1_1.pack()
            frame2_1.pack()
            frame3_1.pack()
            ttk.Label(Cadastro_header, text = "Insira os dados da aplicação: ", style ="Bot.TLabel").pack()

            ttk.Label(frame1_1, text="Usuário: ", style ="Bot.TLabel").pack()
            User_input = Entry(frame1_1, width = 30)
            User_input.pack()

            ttk.Label(frame1_1, text="Senha: ", style ="Bot.TLabel").pack()
            Senha_input = Entry(frame2_1)#, width = 15)
            Senha_input.pack()

            Enter = ttk.Button(frame3_1, text = "Enter", command = lambda : Enter_Config(mod))
            Cadastro.bind('<Return>', lambda event : Enter_Config(mod))
            Enter.pack()

            Cadastro.mainloop()
        #else:
        #    print("Deu Zica")



def Reset():#Reiniciar):#Comando resetar dados
    Comando_input['style'] = 'Bot.TEntry' #Voltar a cor do entry ao normal
    #if(Reiniciar == False):
    with open("Data/UserData.json", "r+") as Resetar:
        ler_Reset = json.load(Resetar)
        #print("ler_Reset: {}".format(ler_Reset))
        #print("Módulos com dados existentes: {}".format(ler_Reset.keys()))
        #Label(TELA, text="insira o módulo que sofrerá reset nos dados: ")
        Programas["values"] = [*ler_Reset]
        Reset_mod = Programas.get()
        print("Reset_mod:", Reset_mod)
        if(Reset_mod != ''):
            try:
                ler_Reset[Reset_mod].pop("User")
                ler_Reset[Reset_mod].pop("Senha")
                Teste = ler_Reset.pop(Reset_mod)
                Resetar.seek(0)#move o cursor para o inicio
                json.dump(ler_Reset, Resetar, indent = 3)
                Resetar.truncate()

                with open("Data/Config.json", 'r+') as Config:
                    ler = json.load(Config)
                    ler[Reset_mod]["Dados_salvos"] = False #definir pros manos abaixo

                with open("Data/Config.json", 'w') as Config:
                    Config.write("")

                    #adiciona ler na Config com indentação organizada
                    json.dump(ler, Config, indent = 3)
                print('Dados do módulo resetados com sucesso!')
                Bot_voice.Bot_fala('Dados do módulo resetados com sucesso!')
            except KeyError:
                print("Deu KeyError no reset")#terminal

#***************************Criação da janela TKinter***************************

Bot_app = Tk()

Bot_app.title("Bot do Johann")
Bot_app.geometry("250x125") #Tamanho bom para janela de login (400x200)
Bot_app.configure(background = '#373737')#OK
Bot_app.resizable(0,0)

#Variáveis Tkinter
Element_status = StringVar()

#Imagens
Icone = PhotoImage(file = "Data/Imagens/Icone.png")
#Icone = Photoimage(file="Data/Imagens/Bot do Johann.png")
Bot_app.iconphoto(True, Icone)

#Estilos
Estilo = ttk.Style()#método para gerenciar estilos

#dá pra fazer uma classe pra importar os estilos
Estilo.configure('Bot.TLabel', background='#373737',foreground='#f0f0f0',font=('Consolas', 11))
Estilo.configure('Bot.TEntry', background='#373737',foreground='#6d6d6d',font=('Consolas', 11))
Estilo.configure('Error.Bot.TEntry',foreground='red',font='bold')
#Ver de fazer isso no próprio entry se pá ^
Estilo.configure('Bot.TButton', background="#6d6d6d",foreground='#373737',font=('Consolas', 9))#bugado
Estilo.configure('2.Bot.TButton', width = 5)
Estilo.configure('TButton.label', background="#6d6d6d",foreground='#6d6d6d',font=('Consolas', 9))#bugado
Estilo.configure('Bot.TFrame', background='#373737')#OK
#Estilo.configure('Bot.TCombobox', fieldbackground='#373737',background='blue')#Não tá entrando
#Estilo.configure("TCombobox", fieldbackground= "orange", background= "white")
#Estilo.configure('.', background="Blue", fieldbackground ="Green")
Estilo.configure('TButton', background="#6d6d6d",activebackground= "orange",foreground='#373737',font=('Consolas', 9))#bugado
print(Estilo.element_names())
#print(Estilo.element_options(input("Opção")))
#style = { "background":"#6d6d6d", "activebackground": "orange", "foreground":'#373737'}

#Frames
frame1 = ttk.Frame(Bot_app, style='Bot.TFrame')
frame2 = ttk.Frame(Bot_app, style='Bot.TFrame')
frame3 = ttk.Frame(Bot_app, style='Bot.TFrame')

frame1.pack()#side = TOP)
frame2.pack()#side = BOTTOM)
frame3.pack()#side = BOTTOM)

#Labels
txt=ttk.Label(frame1, text = "Insira o comando: ", style='Bot.TLabel')
txt.pack( pady = 2, anchor ="n")

#Entry e bind keys
Comando_input = ttk.Entry (frame1, style = 'Bot.TEntry',textvariable=Element_status)
Comando_input.pack(side = LEFT, pady = 2)
#Comando_input.focus()
Comando_input.bind ( '<Return>' , lambda event: run())
Comando_input.bind ( '<Enter>' ,  lambda event:reset_text_entry())
error_status(Comando_input,'Entry')

#Botões
Enter = Button(frame1, text= "Enter", command= run, bg="Green")#Gostei do resultado
#Enter = ttk.Button(frame1, text= "Enter", command= lambda: run(),style = 'TButton')# **style)#Tentar fazer esse funfar
Ajuda = ttk.Button(frame2, text= "Ajuda", command= Ajuda, style='2.Bot.TButton')#Ajuda ainda não implementado
Sair = ttk.Button(frame2, text= "Sair", command=Sair, style='2.Bot.TButton')
print(Ajuda.winfo_class())
Enter.pack(side = LEFT, padx = 2, pady = 2)
Ajuda.pack(side = LEFT, padx = 2, pady = 2)
Sair.pack(side = LEFT,padx = 2, pady = 2)


Programas = ttk.Combobox(frame3, style ='Bot.TCombobox',textvariable = "Módulos")#, values = ["Módulo"])
#Programas.current(-1)
print(Programas.keys())#Terminal
Programas.pack(anchor = "s", side = BOTTOM)


Bot_app.mainloop()

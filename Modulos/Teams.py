from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup
#import sys
import re
from datetime import datetime
import json
import tkinter as tk
from tkinter import ttk


#import VGet

#Constantes
#tentar automatizar a inserção dos cursos
Mat_name = 'Matematica Discreta'
TIC_name = 'Tecnologia da Informação e Comunicação'
MKT_name = 'Principios de Marketing'
TAP_name = 'Tecnicas de Apresentação de Portfolio'
ADM_name = 'Administração Geral'
IPT_name = 'Interpretação e produção de Textos'
ING_name = 'Ingles'

isDebug = False


class Teams_resources():
    def __init__(self, root):
        self.root = root


    def run(self):
        print("Leitor de tarefas Teams - V1.5")

    #Criação da janela
        Tarefas_window = ttk.Notebook(self.root)
        Tarefas_window.pack(pady=10, expand=True)

        # create frames
        #frame1 = ttk.Frame(Tarefas_window, width=400, height=280)
        #frame2 = ttk.Frame(Tarefas_window, width=400, height=280)

        #frame1.pack(fill='both', expand=True)
        #frame2.pack(fill='both', expand=True)

        # add frames to notebook

        #Tarefas_window.add(frame1, text='General Information')
        #Tarefas_window.add(frame2, text='Profile')


        ADM= ttk.Frame(Tarefas_window, width=200, height=280)
        TIC= ttk.Frame(Tarefas_window, width=200, height=280)
        TAP= ttk.Frame(Tarefas_window, width=200, height=280)
        MAT= ttk.Frame(Tarefas_window, width=200, height=280)
        ING= ttk.Frame(Tarefas_window, width=200, height=280)
        MKT= ttk.Frame(Tarefas_window, width=200, height=280)
        Other = ttk.Frame(Tarefas_window, width=200, height=280)


        ADM.pack(fill='both', expand=True)
        TIC.pack(fill='both', expand=True)
        TAP.pack(fill='both', expand=True)
        MAT.pack(fill='both', expand=True)
        ING.pack(fill='both', expand=True)
        MKT.pack(fill='both', expand=True)
        Other.pack(fill='both', expand=True)

        Tarefas_window.add(ADM, text= ADM_name)
        Tarefas_window.add(TIC, text= TIC_name)
        Tarefas_window.add(TAP, text= TAP_name)
        Tarefas_window.add(MAT, text= Mat_name)
        Tarefas_window.add(ING, text= ING_name)
        Tarefas_window.add(MKT, text= MKT_name)
        Tarefas_window.add(Other, text= 'Outros')


    #Encerrando Criação da janela

        try:
            with open("Data/UserData.json", "x") as Criar:
                pass
        except FileExistsError:
            with open("Data/UserData.json", "r") as UserData:
                #leitura dos dados de usuário e senha
                ler = json.load(UserData)
                User = ler["Teams.Tarefas"]["User"]
                Senha = ler["Teams.Tarefas"]["Senha"]

                print(f"Usuário: {User}")#Terminal
                #print(Senha) #Se quiser visualizar a senha

                #formatação:
                #User: email@dominio
                #Senha: senha

        #substituir essa parte pela janela do Tkinter
        try:
            with open("Dados.txt", "x") as Criar:
                pass
        except FileExistsError:
            pass


        def assignments():
            time.sleep(30)
            Iframe = Teams.switch_to.frame("embedded-page-container")
            time.sleep(15)
            print("Tarefas: ")
            Tarefas_matriz = BeautifulSoup(Teams.page_source, 'html.parser')
            Descricao = Tarefas_matriz.find_all("span", class_="title__3Kp3L")
            Materia = Tarefas_matriz.find_all("span", class_="assignment-card-class-name__3sMyJ")
            Data = Tarefas_matriz.find_all("span", class_="")
            Alerta_entrega = ""


#Editar

            #with open("Dados.txt", "w") as Dados:
            for i in range(len(Descricao)):
                #print("Descrição.texto:", Descricao[i].get_text(), "")
                #print("Materia.texto:", Materia[i].get_text(),"")
                #print("Data.texto:", Data[i].get_text(), "")

                Dia = datetime.now().strftime('%d')
                Mes_completo = datetime.now().strftime('%B')
                Horas = datetime.now().strftime('%H')
                Minutos = datetime.now().strftime('%M')

                if(re.search(f'Vence {Dia} de {Mes_completo}', Data[i].get_text())):
                    Alerta_entrega = "ENTREGAR HOJE"
                else:
                    Alerta_entrega = "VAI DEMORAR PRA VENCER AINDA"

                if(Materia[i].get_text() == ADM_name):
                    tk.Label(ADM, text=f'- {Descricao[i].get_text()} <{Data[i].get_text()}>').pack()
                    tk.Label(ADM, text=Alerta_entrega).pack()

                elif(Materia[i].get_text() == re.search(TAP_name, Materia[i])):
                    tk.Label(TAP, text=f'- {Descricao[i].get_text()} <{Data[i].get_text()}>').pack()
                    tk.Label(TAP, text=Alerta_entrega).pack()

                elif(Materia[i].get_text() == re.search(Mat_name, Materia[i])):
                    tk.Label(MAT, text=f'- {Descricao[i].get_text()} <{Data[i].get_text()}>').pack()
                    tk.Label(MAT, text=Alerta_entrega).pack()

                elif(Materia[i].get_text() == re.search(TIC_name, Materia[i])):
                    tk.Label(TIC, text=f'- {Descricao[i].get_text()} <{Data[i].get_text()}>').pack()
                    tk.Label(TIC, text=Alerta_entrega).pack()

                elif(Materia[i].get_text() == re.search(MKT_name, Materia[i])):
                    tk.Label(MKT, text=f'- {Descricao[i].get_text()} <{Data[i].get_text()}>').pack()
                    tk.Label(MKT, text=Alerta_entrega).pack()

                elif(Materia[i].get_text() == re.search(IPT_name, Materia[i])):
                    tk.Label(IPT, text=f'- {Descricao[i].get_text()} <{Data[i].get_text()}>').pack()
                    tk.Label(IPT, text=Alerta_entrega).pack()

                elif(Materia[i].get_text() == re.search(ING_name, Materia[i])):
                    tk.Label(ING, text=f'- {Descricao[i].get_text()} <{Data[i].get_text()}>').pack()
                    tk.Label(ING, text=Alerta_entrega).pack()
                else:
                    tk.Label(Other, text=f'- De {Materia[i].get_text()}: {Descricao[i].get_text()} <{Data[i].get_text()}>').pack()
                    tk.Label(Other, text=Alerta_entrega).pack()
                #Dados.write("Atividade {}: {} \n".format(i+1, Descricao[i].get_text()))
                #Dados.write("Matéria {}: {} \n".format(i+1, Materia[i].get_text()))
                #Dados.write("Data {}: {} \n".format(i+1, Data[i].get_text()))
                #Dados.write("{} \n \n".format(Alerta_entrega))


        Teams_login = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6IjhjNGYyYjNjLTRlZGQtNDdlNy04ODg2LTQ4ZWFjNTRlOWJlYSIsInRzIjoxNjQ1NTcxNzkxLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=f1c902df-688b-4140-a259-eb311ff414ea&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=2513711a-4c5a-4832-a16e-dbd784e57e05&response_mode=fragment'

        Teams = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #Navegador. Verificar modos de adicionar outros
        Teams.implicitly_wait(20) #Espera implícita
        Teams.get(Teams_login) #url
        #time.sleep(10)
        #Inserir Usuário
        username = Teams.find_element(By.ID, "i0116")
        username.send_keys(User)
        username.send_keys(Keys.ENTER)
        print("Usuário inserido!")
        time.sleep(5)

        #Inserir Senha
        password = Teams.find_element(By.ID, "i0118")
        password.send_keys(Senha)
        password.send_keys(Keys.ENTER)
        print("Senha inserida!")

        #Confirmar a conta
        #time.sleep(15)
        confirma_login = Teams.find_element(By.XPATH, "//*[@id='tilesHolder']/div[1]/div/div[1]")
        confirma_login.click()
        print("Perfil Selecionado!")

        #Abre as Tarefas
        time.sleep(30)
        print("Pagina Carregada!")
        tarefas = Teams.find_element(By.XPATH, "//*[@id='app-bar-66aeee93-507d-479a-a3ef-8f494af43945']")
        tarefas.click()
        print("Aba Tarefas selecionada!")
        time.sleep(25)

        assignments()

        input("Pressione ENTER para encerrar ")
        Teams.quit()



    def debug(self):


        print("Leitor de tarefas Teams - V1.5")
        Tarefas_window = ttk.Notebook(self.root)
        Tarefas_window.pack(pady=10, expand=True)

        ADM= ttk.Frame(Tarefas_window, width=200, height=280)
        TIC= ttk.Frame(Tarefas_window, width=200, height=280)
        TAP= ttk.Frame(Tarefas_window, width=200, height=280)
        MAT= ttk.Frame(Tarefas_window, width=200, height=280)
        ING= ttk.Frame(Tarefas_window, width=200, height=280)
        MKT= ttk.Frame(Tarefas_window, width=200, height=280)
        Other = ttk.Frame(Tarefas_window, width=200, height=280)


        ADM.pack(fill='both', expand=True)
        TIC.pack(fill='both', expand=True)
        TAP.pack(fill='both', expand=True)
        MAT.pack(fill='both', expand=True)
        ING.pack(fill='both', expand=True)
        MKT.pack(fill='both', expand=True)
        Other.pack(fill='both', expand=True)

        Tarefas_window.add(ADM, text= 'ADM')
        Tarefas_window.add(TIC, text= 'TIC')
        Tarefas_window.add(TAP, text= 'TAP')
        Tarefas_window.add(MAT, text= 'MAT')
        Tarefas_window.add(ING, text= 'ING')
        Tarefas_window.add(MKT, text= 'MKT')
        Tarefas_window.add(Other, text= 'Outros')


        print("Tarefas.DEBUG: ")
        Descricao = ['Lição1', 'Lição2 - Teste muito bala', 'Lição 3 - Lição 2 aprimorada']
        Materia = ['Matematica Discreta - DMD Alts nights',
         'Tecnicas de Apresentação de Portfolio', 'Interpretação e Produção de Textos - O mito']
        Data = ['Vence em 15 de Janeiro de 2022', 'Vence em 21 de Abril', 'Vence em 24 de Abril']
        Alerta_entrega = ""

        for i in range(len(Descricao)):
            Dia = datetime.now().strftime('%d')
            Mes_completo = datetime.now().strftime('%B')
            Horas = datetime.now().strftime('%H')
            Minutos = datetime.now().strftime('%M')


            if(re.search(f'Vence {Dia} de {Mes_completo}', Data[i])):
                Alerta_entrega = "ENTREGAR HOJE"
            else:
                Alerta_entrega = "VAI DEMORAR PRA VENCER AINDA"



            if(Materia[i] == re.search(ADM_name, Materia[i])):#ADM
                tk.Label(ADM, text=f'- {Descricao[i]} <{Data[i]}>').pack()
                tk.Label(ADM, text=Alerta_entrega).pack()

            elif(re.search(TAP_name, Materia[i])):#TAP
                tk.Label(TAP, text=f'- {Descricao[i]} <{Data[i]}>').pack()
                tk.Label(TAP, text=Alerta_entrega).pack()

            elif(re.search(Mat_name, Materia[i])):#MAT
                tk.Label(MAT, text=f'- {Descricao[i]} <{Data[i]}>').pack()
                tk.Label(MAT, text=Alerta_entrega).pack()

            elif(re.search(TIC_name, Materia[i])):#TIC
                tk.Label(TIC, text=f'- {Descricao[i]} <{Data[i]}>').pack()
                tk.Label(TIC, text=Alerta_entrega).pack()

            elif(re.search(MKT_name, Materia[i])):#MKT
                tk.Label(MKT, text=f'- {Descricao[i]} <{Data[i]}>').pack()
                tk.Label(MKT, text=Alerta_entrega).pack()

            elif(re.search(IPT_name, Materia[i])):#IPT
                tk.Label(IPT, text=f'- {Descricao[i]} <{Data[i]}>').pack()
                tk.Label(IPT, text=Alerta_entrega).pack()

            elif(re.search(ING_name, Materia[i])):#ING
                tk.Label(ING, text=f'- {Descricao[i]} <{Data[i]}>').pack()
                tk.Label(ING, text=Alerta_entrega).pack()
            else:#Não encontrado
                tk.Label(Other, text=f'- De {Materia[i]}: {Descricao[i]} <{Data[i]}>').pack()
                tk.Label(Other, text=Alerta_entrega).pack()






































        # print("Leitor de tarefas Teams - DEBUG MODE")
        # Teste_in = "https://www.linkedin.com/in/jherrerocavadas/"
        # #version = VGet.Browser()
        # #versao_browser = list(filter(None,[version.Browser_version(p)for p in version.paths]))[0]
        # #print(versao_browser)
        # #Esse mano usa o ChromeDriver sem ficar precisando instalar :pray:
        # Teste = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #Navegador. Verificar modos de adicionar outros
        # #Teste = webdriver.Chrome(f"./chromedriver_{versao_browser}.exe") #Navegador. Verificar modos de adicionar outros
        # if 'browserVersion' in Teste.capabilities:
        #     print(Teste.capabilities['browserVersion'])
        # else:
        #     print(Teste.capabilities['version'])
        # Teste.implicitly_wait(20) #Espera implícita
        # Teste.get(Teste_in) #url
        # input("Pressione ENTER para encerrar ")
        # #Teams.quit()


if __name__ == '__main__':
    isDebug = True
    Janela = tk.Tk()
    Testando = Teams_resources(Janela)
    Testando.debug()

    Janela.mainloop()
    #run()
    #debug()

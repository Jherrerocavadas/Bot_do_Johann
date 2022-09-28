from tkinter import *
#import tkinter as *
from tkinter import ttk
from Modulos import TTS

#configurações:
#Alterar voz - OK
#Alterar volume e speech rate - OK
#Alterar face central
#alterar nome de usuário(na plataforma)
#Alterar método de Saudação
#Alterações específicas dos aplicativos

class Configs():
    def __init__(self, root, TTS):
        self.root = root
        self.root.geometry('450x400')
        #self.root.configure(bg='SystemWindow')
        self.TTS = TTS
        self.style = ttk.Style(self.root)#método para gerenciar estilos
        #self.enviar = Button(root,text='Salvar alterações',command=lambda:print(Configura_ai.Alt_voz.get()))
        #self.enviar.pack()

    def Ajustar(self):
        #self.style.configure('TLabelframe', width = 400, background='yellow')#,foreground='red',font=('Consolas', 11))
        self.style.configure('TNotebook', width = 400, background='orange')#,foreground='green',font=('Consolas', 11))
        #self.style.configure('TFrame', width = 400, height = 300, background='red')#,foreground='green',font=('Consolas', 11))




        def Geral():
            #Ideia: colocar os textos em alguma lista e/ou arquivo e ler de lá.
            #Aí é só alterar lá no esquema
            def Isforegner_func():
                print(self.Isforegner_value.get())
                if(self.Isforegner_value.get() == '1'):
                    self.User2_L.pack()
                    self.Alt_User2.pack()
                else:
                    self.User2_L.pack_forget()
                    self.Alt_User2.pack_forget()



            #Variáveis
            vozes_name = [voice.name for voice in self.TTS.voices]
            self.Isforegner_value = StringVar()

            #LabelFrame - Voz
            TTS_LF = LabelFrame(frame1, text = 'Voz')
            TTS_LF.pack()

            #Escolha da Voz
            Label(TTS_LF, text= 'Alterar voz').pack()
            #Alt_voz_L.pack()

            self.Alt_voz = ttk.Combobox(TTS_LF)
            self.Alt_voz['values'] = vozes_name
            self.Alt_voz.pack()

            #Ajuste de volume
            Label(TTS_LF, text= 'Alterar volume').pack()

            self.Alt_vol = Scale(TTS_LF, from_= 0, to_= 100 ,orient = HORIZONTAL)
            self.Alt_vol.pack()

            #Ajuste da velocidade da fala
            Label(TTS_LF, text= 'Alterar velocidade de fala').pack()
            self.Alt_fala = Scale(TTS_LF, from_= 0, to_= 300 ,orient = HORIZONTAL)
            self.Alt_fala.pack()

            Prefs_LF = LabelFrame(frame1, text = 'Usuário')#, width = 100, height = 150)
            Prefs_LF.pack(expand=True)


            #Alterar nome de Usuário
            Label(Prefs_LF, text= 'Alterar nome de Usuário').pack()
            self.Alt_User = ttk.Entry(Prefs_LF)
            self.Alt_User.pack()

            self.Isforegner_name = Checkbutton(
            Prefs_LF,
            command=Isforegner_func,
            text='A pronúncia é diferente da escrita',
            variable=self.Isforegner_value)


            self.Isforegner_name.pack()

            #Inserir pronúncia do nome de Usuário
            self.User2_L = Label(Prefs_LF, text= 'Inserir a pronúncia do nome de usuário')
            self.Alt_User2 = ttk.Entry(Prefs_LF)
            #self.Alt_User2.set(self.AltUser.get())







            #Label(frame1, text= 'Alterarssdfgsgfd de Usuário').pack()
            # print(Prefs_LF['style'])# = 'TLabelFrame'
            #
            #
            # if (self.Alt_voz.get() != ''):
            #
            #     print(self.Alt_voz.get())
            #     print('1231231')
            # else:
            #     print('This')


        def Teams_config():
            pass


        def calcs():
            pass


        Ajustes = ttk.Notebook(self.root)
        Ajustes.pack()

        frame1 = ttk.Frame(Ajustes)#, width=100, height=100)
        frame2 = ttk.Frame(Ajustes)
        frame3 = ttk.Frame(Ajustes)
        submit_frame = ttk.Frame(self.root)



        frame1.pack()
        frame2.pack()
        frame3.pack()
        submit_frame.pack()

        #frame1.pack_propagate(0)
        #frame2.pack_propagate(0)
        #frame3.pack_propagate(0)
        #submit_frame.pack_propagate(0)


        Ajustes.add(frame1, text='Geral')
        Geral()
        Ajustes.add(frame2, text='Teams')
        Teams_config()
        Ajustes.add(frame3, text='Calculadoras')
        calcs()


        self.enviar = Button(submit_frame,text='Salvar alterações',command= self.submit)
        self.cancelar = Button(submit_frame, text = 'Cancelar', command = lambda: print('cancelar'))
        self.enviar.pack(side = LEFT)
        self.cancelar.pack(side = LEFT)



    def submit(self):
        print(self.Alt_voz.get())
        #self.TTS.Config(voice=self.Alt_voz.get() rate=self.Alt_fala.get(), volume = self.Alt_vol.get()/100)
        print(self.Alt_vol.get()/100)
        print(self.Alt_fala.get())
        print(self.Alt_User.get())
        if(self.Isforegner_value.get() == '1'):
            print(self.Alt_User2.get())







            #Alterar face central
            #alterar nome de usuário(na plataforma)
            #Alterar método de Saudação





if __name__ == '__main__':
    Janelinha = Tk()
    TTS = TTS.TTS()
    Janelinha.title('Configurações')
    Configura_ai = Configs(Janelinha,TTS)
    Configura_ai.Ajustar()
    Configura_ai.cancelar['command'] = Configura_ai.root.destroy
    #Botão submit
    #Button(Janelinha,text='Salvar alterações',command=lambda:print(Configura_ai.Alt_voz.get())).pack()

    Janelinha.mainloop()

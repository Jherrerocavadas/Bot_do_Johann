import math
import sys#precisa?
from tkinter import *
from tkinter.ttk import *

class Calculadora():
#********************************<Inicializar>*********************************#
    def __init__(self, root):
        self.root = root
        self.calc_var1 = StringVar()
        self.Bskr = None
        self.calc = None
        self.complex = None


#********************************<Calculadora>*********************************#

    def calcular(self):
        self.root.withdraw()
        self.withdraw_func(self.calc)
        self.calc.title("Calculadora Simples")

        def calc_insert(texto):
            entry_value=result_calc_txt.get()
            try:
                digitos_operadores = [#Basicamente uma AND de quatro entradas
                entry_value[len(entry_value)-1] == "+",
                entry_value[len(entry_value)-1] == "-",
                entry_value[len(entry_value)-1] == "/",
                entry_value[len(entry_value)-1] == "*",
                entry_value[len(entry_value)-1] == ""
                ]
            except IndexError:
                digitos_operadores = [True == False]
            entrada = [#Basicamente uma AND de quatro entradas
            texto == "+",
            texto == "-",
            texto == "/",
            texto == "*"
            ]

            if (any(digitos_operadores) and any(entrada)):#não escrever dois operadores seguidos
                print('len entry:',len(entry_value))

            elif(texto == "="):#resultado
                try:
                    print(eval(entry_value))
                    self.calc_var1.set(eval(entry_value))
                except SyntaxError:
                    self.calc_var1.set('Erro')
                except ZeroDivisionError:
                    self.calc_var1.set('Erro. Divisão por 0')

            elif(texto == "<-"):#resultado
                self.calc_var1.set(entry_value[:-1])

            elif(entry_value.startswith('Erro')):
                self.calc_var1.set('')
                result_calc_txt.insert(len(entry_value), texto)

            else:
                result_calc_txt.insert(len(entry_value), texto)
                print('digitado', texto)
        #Fim da função de cálculo

        estilo = Style()
        estilo.configure('Calc.TButton', width = 5)

        if(self.calc == None):

            self.calc = Toplevel(self.root)
            self.menus(self.calc)

            print(self.calc)
            frame0 = Frame(self.calc)
            frame1 = Frame(self.calc)
            frame2 = Frame(self.calc)
            frame3 = Frame(self.calc)
            frame4 = Frame(self.calc)

            frame0.pack()
            frame1.pack()
            frame2.pack()
            frame3.pack()
            frame4.pack()

            #Botões e Entry
            Btn_1 = Button(frame3, text='1',command=lambda:calc_insert(Btn_1["text"]) ,style='Calc.TButton')
            Btn_2 = Button(frame3, text='2',command=lambda:calc_insert(Btn_2["text"]) ,style='Calc.TButton')
            Btn_3 = Button(frame3, text='3',command=lambda:calc_insert(Btn_3["text"]) ,style='Calc.TButton')
            Btn_4 = Button(frame2, text='4',command=lambda:calc_insert(Btn_4["text"]) ,style='Calc.TButton')
            Btn_5 = Button(frame2, text='5',command=lambda:calc_insert(Btn_5["text"]) ,style='Calc.TButton')
            Btn_6 = Button(frame2, text='6',command=lambda:calc_insert(Btn_6["text"]) ,style='Calc.TButton')
            Btn_7 = Button(frame1, text='7',command=lambda:calc_insert(Btn_7["text"]) ,style='Calc.TButton')
            Btn_8 = Button(frame1, text='8',command=lambda:calc_insert(Btn_8["text"]) ,style='Calc.TButton')
            Btn_9 = Button(frame1, text='9',command=lambda:calc_insert(Btn_9["text"]) ,style='Calc.TButton')
            Btn_0 = Button(frame4, text='0',command=lambda:calc_insert(Btn_0["text"]) ,style='Calc.TButton')
            Btn_plus = Button(frame1, text='+',command=lambda:calc_insert(Btn_plus["text"]) ,style='Calc.TButton')
            Btn_minus = Button(frame2, text='-',command=lambda:calc_insert(Btn_minus["text"]) ,style='Calc.TButton')
            Btn_division = Button(frame3, text='/',command=lambda:calc_insert(Btn_division["text"]) ,style='Calc.TButton')
            Btn_multi = Button(frame4, text='*',command=lambda:calc_insert(Btn_multi["text"]) ,style='Calc.TButton')
            Btn_del = Button(frame0, text='<-',command=lambda:calc_insert(Btn_del["text"]) ,style='Calc.TButton')
            Btn_equal = Button(frame4,text='=',command=lambda:calc_insert(Btn_equal["text"]) , style='Calc.TButton')
            Btn_dot = Button(frame4, text='.',command=lambda:calc_insert(Btn_dot["text"]) ,style='Calc.TButton')
            result_calc_txt = Entry(frame0, textvariable = self.calc_var1)

            result_calc_txt.pack(side=LEFT)
            Btn_1.pack(side=LEFT)
            Btn_2.pack(side=LEFT)
            Btn_3.pack(side=LEFT)
            Btn_4.pack(side=LEFT)
            Btn_5.pack(side=LEFT)
            Btn_6.pack(side=LEFT)
            Btn_7.pack(side=LEFT)
            Btn_8.pack(side=LEFT)
            Btn_9.pack(side=LEFT)
            Btn_0.pack(side=LEFT)
            Btn_plus.pack(side=LEFT)
            Btn_minus.pack(side=LEFT)
            Btn_division.pack(side=LEFT)
            Btn_dot.pack(side=LEFT)
            Btn_multi.pack(side=LEFT)
            Btn_del.pack(side=LEFT)
            Btn_equal.pack(side=LEFT)

        else:

            self.calc.deiconify()

        self.calc.lift()
        self.calc.protocol("WM_DELETE_WINDOW", self.fechar_janela)


#**********************************<Bhaskara>**********************************#

    def Bskr_window(self):
        self.root.withdraw()
        self.withdraw_func(self.Bskr)

        def Bhaskara(a,b,c):

            a = float(a.get())
            b = float(b.get())
            c = float(c.get())
            print(a)
            print(b)
            print(c)

            if(a == 0):
                print("'a' deve ser diferente de 0")
                self.status["text"] = " 'a' deve ser diferente de 0"
                self.delta_value["text"] = 'delta = { }'
                self.x1_value["text"] = 'x2 = { }'
                self.x2_value["text"] = 'x2 = { }'
                return

            delta = (b**2)-4*(a)*(c)#executa a equação de delta

            if(delta < 0):
                print("Equação sem solução real")
                self.status["text"] = "Equação sem solução real"
                self.x1_value["text"] = 'x1 = { }'
                self.x2_value["text"] = 'x2 = { }'
            else:#solução com uma ou duas raízes reais
                x1 = (-b+math.sqrt(delta))/(2*a)
                x2 = (-b-math.sqrt(delta))/(2*a)
                print(f'x1 ={x1}')
                print(f'x2 = {x2}')

                self.status["text"] = "Equação resolvida com sucesso!"
                self.x1_value["text"] = f'x1 ={x1}'
                self.x2_value["text"] = f'x2 = {x2}'
            print(f'delta = {delta}')
            self.delta_value["text"] = f'delta = {delta}'

        if(self.Bskr == None):
            self.Bskr = Toplevel(self.root)
            self.menus(self.Bskr)
            self.Bskr.title("Calculadora de equação Bhaskara v2.0")
            self.Bskr.geometry("270x200")
            frame1 = Frame(self.Bskr)
            frame2 = Frame(self.Bskr)
            frame1.pack()
            frame2.pack()

            Label(frame1, text = "Insira os valores da equação de segundo grau").pack(side=TOP, pady = 2)#style="NOME DO ESTILO"

            #Entry e Label
            a = Entry(frame1, width = 5)
            a_text=Label(frame1, text = "x²")
            b = Entry(frame1, width = 5)
            b_text=Label(frame1, text = "x")
            c = Entry(frame1, width = 5)

            a.pack(side=LEFT, padx = 2)
            a_text.pack(side=LEFT, padx = 2)
            b.pack(side=LEFT)
            b_text.pack(side= LEFT, padx = 2)
            c.pack(side= LEFT, padx = 2)

            Calcular = Button(frame1, command=lambda : Bhaskara(a,b,c), text="Calcular")
            Calcular.pack(side=BOTTOM)

            Label(frame2, text = "Resultado: ").pack(pady = 2)
            self.status = Label(frame2, text = "")
            self.status.pack(side=TOP, pady = 2)

            self.delta_value = Label(frame2, text = "")
            self.delta_value.pack(pady = 2)

            self.x1_value = Label(frame2, text = "")
            self.x1_value.pack(pady = 2)

            self.x2_value = Label(frame2, text = "")
            self.x2_value.pack(pady = 2)

        else:
            self.Bskr.deiconify()
        self.Bskr.lift()
        self.Bskr.protocol("WM_DELETE_WINDOW", self.fechar_janela)


#*****************************<Números Complexos>******************************#

    def complex_Window(self):
        self.root.withdraw()
        self.withdraw_func(self.complex)
        def complex_calc(a,b,c,d):
            a = float(a.get())
            b = float(b.get())
            c = float(c.get())
            d = float(d.get())
            t1 = a+c
            t2 = b+d

            print(t1, t2, 'i')#não printa o sinal

        if(self.complex == None):
            self.complex = Toplevel(self.root)
            self.menus(self.complex)
            self.complex.title("Calculadora de números complexos v1.0")
            self.complex.geometry("270x200")
            frame1 = Frame(self.complex)
            frame2 = Frame(self.complex)
            frame3 = Frame(self.complex)
            frame1.pack()
            frame2.pack()
            frame3.pack()

            Label(frame1, text = "Insira os valores da equação de segundo grau").pack(side=TOP, pady = 2)#style="NOME DO ESTILO"

            #Entry e Label
            a = Entry(frame1, width = 5)
            b = Entry(frame1, width = 5)
            b_text=Label(frame1, text = "i")
            c = Entry(frame1, width = 5)
            d = Entry(frame1, width = 5)
            d_text=Label(frame1, text = "i")

            a.pack(side=LEFT, padx = 2)
            b.pack(side=LEFT)
            b_text.pack(side= LEFT, padx = 2)
            c.pack(side= LEFT, padx = 2)
            d.pack(side= LEFT, padx = 2)
            d_text.pack(side= LEFT, padx = 2)

            Calcular = Button(frame1, command=lambda : complex_calc(a,b,c,d), text="Calcular")
            Calcular.pack(side=BOTTOM)

            Label(frame2, text = "Resultado: ").pack(pady = 2)
            self.status = Label(frame2, text = "")
            self.status.pack(side=TOP, pady = 2)

            self.delta_value = Label(frame2, text = "")
            self.delta_value.pack(pady = 2)

            self.x1_value = Label(frame2, text = "")
            self.x1_value.pack(pady = 2)

            self.x2_value = Label(frame2, text = "")
            self.x2_value.pack(pady = 2)


        else:
            self.complex.deiconify()
        self.complex.lift()
        self.complex.protocol("WM_DELETE_WINDOW", self.fechar_janela)


#********************************<Aba de Menus>********************************#

    def menus(self,window_menu):
        print('win_menu: ', window_menu)
        menu = Menu(window_menu)
        recursos = Menu(menu,tearoff=0)
        recursos.add_command(label ='Calculadora padrão',command=lambda:self.calcular())
        recursos.add_command(label ='Calculadora "requintada"')#pensar melhor no nome
        recursos.add_command(label = 'Bhaskara',command = lambda: self.Bskr_window())
        recursos.add_command(label = 'Numeros complexos',command = lambda: self.complex_Window())
        menu.add_cascade(label ='Abrir', menu=recursos)
        window_menu.config(menu=menu)


#******************************<Ocultar Janelas>*******************************#

    def withdraw_func(self, aba_executada):
        #Os módulos são:
        #self.Bskr.withdraw()
        #self.calc.withdraw()
        #self.complex.withdraw()

        abas = [self.Bskr, self.calc, self.complex]#tem que inserir todo módulo aqui manualmente
        abas.remove(aba_executada)

        for aba in abas:
            try:
                aba.withdraw()
                print('str: ', str(aba))
            except AttributeError:
                print(aba)


#*******************************<Fechar Janelas>*******************************#

    def fechar_janela(self):#Fechar a janela principal em qualquer janela filha,
    #encerrando o programa
        print("tá fechando")
        self.root.destroy()

#        self.root.deiconify()
        #print(self.root.destroy())


#*******************************<Janela Tkinter>*******************************#

janela = Tk()
janelas_calc = Calculadora(janela)
#estilo = Style(janela)
#estilo.configure("teste.TLabel", font=('Windows Command Prompt', 11))
janela.title("Calculadora de equação Bhaskara v1.0")
janela.geometry("270x200")
# frame1 = Frame()
# frame2 = Frame()
# frame1.pack()
# frame2.pack()
janelas_calc.menus(janela)
# menu = Menu(janela)
# recursos = Menu(menu,tearoff=0)
# recursos.add_command(label ='Calculadora padrão',command=lambda:janelas_calc.calcular())
# recursos.add_command(label = 'Bhaskara',command = lambda: janelas_calc.Bskr_window())
# recursos.add_command(label = 'Numeros complexos')
#
# #recursos.add_command(label ='teste')
# #recursos.add_command(label ='TYesfas')
#
# menu.add_cascade(label ='NOME', menu=recursos)
#
#
#
# janela.config(menu=menu)


#menubar = Menu(janela)
#
# filemenu = Menu(menu, tearoff=0)
# filemenu.add_command(label="Open")
# filemenu.add_command(label="Save")
# filemenu.add_command(label="Exit")
#
# menu.add_cascade(label="File", menu=filemenu)

#janela.config(menu=menubar)
#inf = input('esconder? ')
#if(inf == 'hide'):
#    teste()





#
# Label(frame1, text = "Insira os valores da equação de segundo grau").pack(side=TOP, pady = 2)#style="NOME DO ESTILO"
#
# #Entry e Label
# a = Entry(frame1, width = 5)
# a_text=Label(frame1, text = "x²")
# b = Entry(frame1, width = 5)
# b_text=Label(frame1, text = "x")
# c = Entry(frame1, width = 5)
#
# a.pack(side=LEFT, padx = 2)
# a_text.pack(side=LEFT, padx = 2)
# b.pack(side=LEFT)
# b_text.pack(side= LEFT, padx = 2)
# c.pack(side= LEFT, padx = 2)
#
# Calcular = Button(frame1, command=lambda : janelas_calc.Bhaskara(a,b,c), text="Calcular")
# Calcular.pack(side=BOTTOM)
#
# Label(frame2, text = "Resultado: ").pack(pady = 2)
# status = Label(frame2, text = "")
# status.pack(side=TOP, pady = 2)
#
# delta_value = Label(frame2, text = "")
# delta_value.pack(pady = 2)
#
# x1_value = Label(frame2, text = "")
# x1_value.pack(pady = 2)
#
# x2_value = Label(frame2, text = "")
# x2_value.pack(pady = 2)

janela.mainloop()

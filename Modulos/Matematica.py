import re
import math
from tkinter import *
from tkinter.ttk import *

def calcular(a,b,c):

    #print("Báskara V 1.0")
    #print('Digite a equação no formato ax²+bx+c')

    #equacao = input("Equação: ")
    #a = 2 #re.findall()
    #b = 10
    #c = 8

    #txt = "20x²+10x+8"
    #a = re.findall("\d+?x²", txt)
    #a = re.findall("\d+?", a[0])
    #b = re.findall("[+|-]\d+?x", txt)
    #b = re.findall(".\d+?", b[0])
    #c = re.findall("[+|-]\d+?$", txt)
    a = float(a.get())
    b = float(b.get())
    c = float(c.get())
    print(a)
    print(b)
    print(c)

    if(a == 0):
        print("'a' deve ser diferente de 0")
        status["text"] = " 'a' deve ser diferente de 0"
        delta_value["text"] = 'delta = { }'
        x1_value["text"] = 'x2 = { }'
        x2_value["text"] = 'x2 = { }'
        return

    delta = (b**2)-4*(a)*(c)#executa a equação de delta

    if(delta < 0):
        print("Equação sem solução real")
        status["text"] = "Equação sem solução real"
        x1_value["text"] = 'x1 = { }'
        x2_value["text"] = 'x2 = { }'
    else:#solução com uma ou duas raízes reais
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print(f'x1 ={x1}')
        print(f'x2 = {x2}')

        status["text"] = "Equação resolvida com sucesso!"
        x1_value["text"] = f'x1 ={x1}'
        x2_value["text"] = f'x2 = {x2}'
    print(f'delta = {delta}')
    delta_value["text"] = f'delta = {delta}'


janela = Tk()

#estilo = Style(janela)
#estilo.configure("teste.TLabel", font=('Windows Command Prompt', 11))
janela.title("Calculadora de equação Bhaskara v1.0")
janela.geometry("270x200")
frame1 = Frame()
frame2 = Frame()
frame1.pack()
frame2.pack()

Label(frame1, text = "Insira os valores da equação de segundo grau").pack(side=TOP, pady = 2)#style="NOME DO ESTILO"
a = Entry(frame1, width = 5)
a.pack(side=LEFT, padx = 2)

a_text=Label(frame1, text = "x²")
a_text.pack(side=LEFT, padx = 2)

b = Entry(frame1, width = 5)
b.pack(side=LEFT)

b_text=Label(frame1, text = "x")
b_text.pack(side= LEFT, padx = 2)

c = Entry(frame1, width = 5)
c.pack(side= LEFT, padx = 2)

Calcular = Button(frame1, command=lambda : calcular(a,b,c), text="Calcular")
Calcular.pack(side=BOTTOM)

Label(frame2, text = "Resultado: ").pack(pady = 2)
status = Label(frame2, text = "")
status.pack(side=TOP, pady = 2)

delta_value = Label(frame2, text = "")
delta_value.pack(pady = 2)

x1_value = Label(frame2, text = "")
x1_value.pack(pady = 2)

x2_value = Label(frame2, text = "")
x2_value.pack(pady = 2)

janela.mainloop()

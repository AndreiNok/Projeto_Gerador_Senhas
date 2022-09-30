from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from unicodedata import numeric
from PIL import ImageTk,Image
import string
import random


#cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fcfcfc"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

janela = Tk()
janela.title('')
janela.geometry('295x350')
janela.configure(bg = cor2)
janela.resizable(width = False , height = False)

#SEPARANDO A TELA EM DOIS FRAMES
frame_cima= Frame(janela, width = 295, height = 50, bg = cor6 , pady = 0, padx = 0, relief = 'flat')
frame_cima.grid(row = 0, column = 0, sticky = NSEW)


frame_baixo= Frame(janela, width = 295, height = 310, bg = cor2 , pady = 0, padx = 0, relief = 'flat')
frame_baixo.grid(row = 1, column = 0, sticky = NSEW)
# TRABALHANDO NO FRAME DE CIMA 
#AQUI O ESTILO NAO SEI PQ 
estilo = ttk.Style(janela)
estilo.theme_use('clam')
#AQUI PRA CRIAR A IMAGEM NO LABEL , DEVE TER O PILLOW INSTALADO
img = Image.open('paysandu.png')
img = img.resize((55, 45), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
# BOTAR A LOGO NA TELA 
app_logo = Label(frame_cima, height = 55, image= img, compound= LEFT, padx = 10, relief = 'flat', anchor = 'nw', bg = cor6)
app_logo.place(x = 1 , y =0)
# BOTAR O NOME DO APP NA TELA
app_nome = Label(frame_cima,text = 'Gerador de Senhas',width = 20  ,height = 1, padx = 0, relief = 'flat', font= ('Ivi 16 bold'), anchor = 'nw', bg = cor6, fg = 'black')
app_nome.place(x = 70 , y =10)
# COLOCA UMA LINHA NO APP
app_linha = Label(frame_cima,text = '',width = 295  ,height = 1, padx = 0, relief = 'flat',font= ('Ivi 1'), anchor = 'nw', bg = 'red')
app_linha.place(x =0 , y =48)
 #---- função de criar a senha
def criar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    nume = '123456789'
    simbolos = '[]{}()*;/,_-'

    global combinar

    #CONDIÇÃO PARA MAIUSCULA
    if estado_1.get() == alfa_maior:
        combinar = alfa_maior 
    else:
        pass
    #CONDIÇÃO PARA MINUSCULA
    if estado_2.get() == alfa_menor:
        combinar += alfa_menor 
    else:
        pass
        #CONDIÇÃO NUMERO
    if estado_3.get() == nume:
        combinar += nume
    else:
        pass
        #CONDIÇÃO SIMBOLOS
    if estado_4.get() == simbolos:
        combinar += simbolos
    else:
        pass
    if estado_1.get() != alfa_maior and estado_2.get() != alfa_menor and estado_3.get() != nume and estado_4.get() != simbolos:
        messagebox.showerror("Erro", "Escolha uma opção")
    
    
    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))
    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)
        
        messagebox.showinfo("Sucesso","A Senha foi copiada com sucesso")
    app_copiar = Button(frame_baixo,command = copiar_senha,text = 'Copiar',width = 6  ,height = 2, relief = 'raised',overrelief = 'solid', font= ('Ivi 10 bold'), anchor = 'center', bg = cor2, fg =cor1)
    app_copiar.grid(row = 0 , column = 1, columnspan = 1, sticky = NW, padx = 5 , pady = 10)

# APP PARTE DE BAIXO 

app_senha = Label(frame_baixo,text = ' - - - - ',width = 26 ,height = 2 , padx = 0, relief = 'solid', font= ('Ivi 10 bold'), anchor = 'center', bg = cor2, fg =cor1)
app_senha.grid(row = 0 , column = 0, columnspan = 1, sticky = NSEW, padx = 3 , pady = 10)

app_info = Label(frame_baixo,text = 'Número Total de caracteres na senha',height = 1, padx = 0, relief = 'flat', font= ('Ivi 10 bold'), anchor = 'nw', bg = cor2, fg =cor1)
app_info.grid(row = 1 , column = 0, columnspan = 2, sticky = NSEW, padx = 5 , pady = 1)

#CRIANDO UM SPINBOX 
var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to = 20, width = 9, textvariable = var)
spin.grid(row = 2, column = 0,columnspan = 2, sticky = NW, padx = 5, pady =8)

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
nume = '123456789'
simbolos = '[]{}()*;/,_-'

#CRIANDO UMA CHECKBOX
frame_caracteres= Frame(frame_baixo, width = 295, height = 210, bg = cor2 , pady = 0, padx = 0, relief = 'flat')
frame_caracteres.grid(row = 3, column = 0, sticky = NSEW,columnspan= 4)
# ------------------ LETRAS MAIUSCULAS ------------
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var = estado_1,onvalue = alfa_maior, offvalue= 'off', relief = 'flat', bg =cor2)
check_1.grid(row = 0, column = 0, sticky = NW, padx = 2, pady =5)
app_info = Label(frame_caracteres,text = 'ABC Letras Maiusculas',height = 1, padx = 0, relief = 'flat', font= ('Ivi 10'), anchor = 'nw', bg = cor2, fg =cor1)
app_info.grid(row = 0 , column = 1, sticky = NW, padx = 2 , pady = 5)
# ---------------------------------------------------
# ------------------ LETRAS MINUSCULAS ------------
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var = estado_2,onvalue = alfa_menor, offvalue= 'off', relief = 'flat', bg =cor2)
check_2.grid(row = 1, column = 0, sticky = NW, padx = 2, pady =5)
app_info = Label(frame_caracteres,text = 'ABC Letras Minusculas',height = 1, padx = 0, relief = 'flat', font= ('Ivi 10'), anchor = 'nw', bg = cor2, fg =cor1)
app_info.grid(row = 1 , column = 1, sticky = NW, padx = 2 , pady = 5)
# ---------------------------------------------------
# ------------------ NÚMEROS ------------
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var = estado_3,onvalue = nume, offvalue= 'off', relief = 'flat', bg =cor2)
check_3.grid(row = 2, column = 0, sticky = NW, padx = 2, pady =5)
app_info = Label(frame_caracteres,text = '123 Números',height = 1, padx = 0, relief = 'flat', font= ('Ivi 10'), anchor = 'nw', bg = cor2, fg =cor1)
app_info.grid(row = 2 , column = 1, sticky = NW, padx = 2 , pady = 5)
# ---------------------------------------------------
# ------------------ SÍMBOLOS ------------
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var = estado_4,onvalue = simbolos, offvalue= 'off', relief = 'flat', bg =cor2)
check_4.grid(row = 3, column = 0, sticky = NW, padx = 2, pady =5)
app_info = Label(frame_caracteres,text = '$;/ Símbolos',height = 1, padx = 0, relief = 'flat', font= ('Ivi 10'), anchor = 'nw', bg = cor2, fg =cor1)
app_info.grid(row = 3 , column = 1, sticky = NW, padx = 2 , pady = 5)
# ---------------------------------------------------
#-------------------- BOTÃO GERAR SENHA------------------
app_gerador = Button(frame_caracteres,command = criar_senha,text = 'GERAR SENHA',width = 35, height = 1, relief = 'flat',overrelief ='solid', font= ('Ivi 10 bold'), anchor = 'center', bg = cor6, fg =cor1)
app_gerador.grid(row = 5 , column = 0,columnspan = 5, sticky = NSEW, padx = 3 , pady = 20)



janela.mainloop()
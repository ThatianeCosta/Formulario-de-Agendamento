# Importando o Tkinter
from cgitb import text
from tkinter import *
from tkinter import font

from tkinter import ttk
from tkinter import messagebox

##### Importando tkcalendar #####
from tkcalendar import Calendar, DateEntry

# Importando Views
from view import *

##### Cores #####
cor0 = "#f0f3f5"   # Black - Preta
cor1 = "#feffff"   # White - Branca
cor2 = "#4fa882"   # Green - Verde
cor3 = "#38576b"   # Valor
cor4 = "#403d3d"   # Letra
cor5 = "#e06636"   # - Profit
cor6 = "#038cfc"   # Blue  - Azul
cor7 = "#ef5350"   # Red   - Vermelho
cor8 = "#263238"   # + Green - Verde
cor9 = "#e9edf5"   # Sky Blue - Azul Claro

##### Criando Janela #####

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=cor9)
janela.resizable(width=FALSE, height=FALSE)

##### Dividindo a Janela #####

frame_cima = Frame(janela, width=310, height=50, background="#8A7C9B", relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, background=cor1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, background=cor1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

##### Variavel tree global
global tree

##### Função Inserir #####
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    dia = e_cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()

    lista = [nome, email, telefone, dia, estado, assunto]

    if nome=='':
        messagebox.showerror('Erro','O nome nao pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso')

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_cal.delete(0,'end')
        e_estado.delete(0,'end')
        e_assunto.delete(0,'end')
    
    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

##### Função Atualizar #####
def atualizar():
    try:
        treeview_dados = tree.focus()
        treeview_dicionario = tree.item(treeview_dados)
        treeview_lista = treeview_dicionario['values']

        valor_id = treeview_lista[0]

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_cal.delete(0,'end')
        e_estado.delete(0,'end')
        e_assunto.delete(0,'end')

        e_nome.insert(0,treeview_lista[1])
        e_email.insert(0,treeview_lista[2])
        e_telefone.insert(0,treeview_lista[3])
        e_cal.insert(0,treeview_lista[4])
        e_estado.insert(0,treeview_lista[5])
        e_assunto.insert(0,treeview_lista[6])

        ##### Função Update
        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            dia = e_cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()

            lista = [nome, email, telefone, dia, estado, assunto, valor_id]

            if nome=='':
                messagebox.showerror('Erro','O nome nao pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso','Os dados foram atualizados com sucesso')

                e_nome.delete(0,'end')
                e_email.delete(0,'end')
                e_telefone.delete(0,'end')
                e_cal.delete(0,'end')
                e_estado.delete(0,'end')
                e_assunto.delete(0,'end')
        
            for widget in frame_direita.winfo_children():
                widget.destroy()
        
            mostrar()
        
        ##### Botão Confirmar
        b_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, font=('Ivy 7 bold'), background=cor2, fg=cor1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=370)
        
   
    except IndexError:
        messagebox.showerror('Erro','Seleciona um dos dados na tabela')

##### Função Deletar #####
def deletar():
   try:
        treeview_dados = tree.focus()
        treeview_dicionario = tree.item(treeview_dados)
        treeview_lista = treeview_dicionario['values']

        valor_id = [treeview_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('sucesso','Os dados foram deletados da Tabela com sucesso')

        for widget in frame_direita.winfo_children():
                widget.destroy()
        
        mostrar()

   except IndexError:
        messagebox.showerror('Erro','Seleciona um dos dados na tabela')


##### Label Cima #####
app_nome = Label(frame_cima, text='Formulário de Agendamento', anchor=NW, font=('Ivy 13 bold'), background="#8A7C9B", fg=cor1, relief='flat')
app_nome.place(x=10, y=20)

##### Configurando o Frame Baixo #####

##### Nome
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

##### Email
l_email = Label(frame_baixo, text='Email *', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

##### Telefone
l_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_telefone.place(x=10, y=130)
e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_telefone.place(x=15, y=160)

##### Data da Consulta
l_cal = Label(frame_baixo, text='Data da consulta *', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_cal.place(x=15, y=190)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
e_cal.place(x=15, y=220)

##### Estado
l_estado = Label(frame_baixo, text='Estado da consulta *', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=160, y=220)

##### Especialidade / Sobre
l_assunto = Label(frame_baixo, text='Especialidade *', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_assunto.place(x=15, y=260)
e_assunto = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_assunto.place(x=15, y=290)

##### Botão Inserir
b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), background=cor6, fg=cor1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)

##### Botão Atualizar
b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font=('Ivy 9 bold'), background=cor2, fg=cor1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=340)

##### Botão Deletar
b_deletar = Button(frame_baixo, command=deletar, text='Deletar', width=10, font=('Ivy 9 bold'), background=cor7, fg=cor1, relief='raised', overrelief='ridge')
b_deletar.place(x=205, y=340)

##### Frame Direita #####
def mostrar():

    global tree        
    lista = mostrar_info()

    # Lista para o cabeçalho
    tabela_head = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Estado', 'Especialidade']
    
    # Criando a Tabela   
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # Vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)
        
    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 90, 80, 90, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # Ajustar a largura da coluna para String do cabeçalho
        tree.column(col, width=h[n], anchor=hd[n])
        
        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)
            

# Chamando a Função mostrar
mostrar()



janela.mainloop()
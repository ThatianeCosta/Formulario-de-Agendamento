# Importando SQLite
import sqlite3 as lite

# CRUD

# Create = Inserir / criar
# Ready = Acessar / mostrar 
# Update = Atualizar 
# Delete = Deletar / Apagar

# Criando Conexão
conexao = lite.connect('dados.db')

# Inserir Informações 
def inserir_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Acessar Informações
def mostrar_info():
    lista = []
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
       
        for i in informacao: 
            lista.append(i)
    return lista

# Atualizar Informações
def atualizar_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query,i)

# Deletar Informações
def deletar_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query,i)

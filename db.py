import sqlite3

conexao = sqlite3.connect("animais.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

TABLES = {}
TABLES['Animais'] = ('''
    CREATE TABLE IF NOT EXISTS animais(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    especie VARCHAR(255) NOT NULL,
    raca VARCHAR(255) NOT NULL,
    porte TEXT NOT NULL CHECK (porte IN ('Pequeno', 'Médio', 'Grande')),    idade VARCHAR (50) NOT NULL,
    descriacao VARCHAR(255),
    status TEXT NOT NULL CHECK (status IN ('Disponível', 'Adotado')),    ) 
''')

conexao.close()


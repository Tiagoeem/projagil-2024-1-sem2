import sqlite3
from datetime import date

# Conexão com o banco de dados
conn = sqlite3.connect('db/biblioteca.db')
cursor = conn.cursor()

# Criar tabela de Livros
cursor.execute("""
CREATE TABLE IF NOT EXISTS Livros (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Autor TEXT NOT NULL,
    AnoPublicacao INTEGER,
    Genero TEXT
);
""")

# Criar tabela de Usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    DataCadastro TEXT NOT NULL
);
""")

# Inserir registros de livros
livros = [
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia"),
    ("1984", "George Orwell", 1949, "Ficção Distópica"),
    ("Moby Dick", "Herman Melville", 1851, "Ficção"),
    ("Orgulho e Preconceito", "Jane Austen", 1813, "Romance"),
    ("O Grande Gatsby", "F. Scott Fitzgerald", 1925, "Romance"),
    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967, "Romance"),
    ("Ensaio sobre a Cegueira", "José Saramago", 1995, "Ficção Distópica"),
    ("A Revolução dos Bichos", "George Orwell", 1945, "Fábula"),
    ("Dom Quixote", "Miguel de Cervantes", 1605, "Romance"),
    ("A Divina Comédia", "Dante Alighieri", 1320, "Épico")
]
cursor.executemany("""
INSERT INTO Livros (Titulo, Autor, AnoPublicacao, Genero)
VALUES (?, ?, ?, ?);
""", livros)

# Inserir registros de usuários
hoje = date.today().strftime('%Y-%m-%d')
usuarios = [
    ("Ana Silva", "ana.silva@email.com", hoje),
    ("Pedro Mendes", "pedro.mendes@email.com", hoje),
    ("Carla Souza", "carla.souza@email.com", hoje),
    ("Roberto Alves", "roberto.alves@email.com", hoje),
    ("Julia Castro", "julia.castro@email.com", hoje)
]
cursor.executemany("""
INSERT INTO Usuarios (Nome, Email, DataCadastro)
VALUES (?, ?, ?);
""", usuarios)

# Confirmar criação das tabelas e fechar conexão
conn.commit()
conn.close()

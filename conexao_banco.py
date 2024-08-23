from System_library import Biblioteca
from class_book import Livro
from class_user import Usuario
from class_loan import Emprestimo
from class_copy import Exemplar


import sqlite3
from datetime import datetime

# Conectando ao banco de dados (ou criando se não existir)
conn = sqlite3.connect('livraria.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Executando o comando SQL para criar a tabela
cursor.execute('create table if not exists livros (id integer primary key, nome text, autor_id integer, editora_id integer)')

# Salvando as mudanças
conn.commit()

# Fechando a conexão com o banco de dados
conn.close()
biblioteca = Biblioteca()

# Adicionando um livro e um usuário
biblioteca.adicionar_livro("O Senhor dos Anéis", 1, 2)  # Supõe que editora_id 1 existe
biblioteca.adicionar_usuario("João", "123456789", "Brasileiro")

# Realizando um empréstimo
emprestimo_id = biblioteca.realizar_emprestimo(1, 1)  # Supondo que usuario_id 1 e livro_id 1 existam

# Devolver livro
biblioteca.devolver_livro(emprestimo_id)

# Renovar empréstimo
biblioteca.renovar_emprestimo(emprestimo_id, 1)

# Listar empréstimos
emprestimos = biblioteca.listar_emprestimos()
print(emprestimos)

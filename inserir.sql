INSERT INTO Editoras (nome) VALUES ('Editora A'), ('Editora B');
INSERT INTO Autores (nome, nacionalidade) VALUES ('Autor X', 'Brasileiro'), 
('Autor Y', 'Americano');
INSERT INTO Livros (titulo, editora_id, max_renovacoes) VALUES 
('Livro 1', 1, 2),
('Livro 2', 2, 1);
INSERT INTO Livros_Autores (livro_id, autor_id) VALUES 
(1, 1), 
(2, 2);

INSERT INTO Exemplares (livro_id, codigo) VALUES 
(1, 'EX-001'), 
(1, 'EX-002'), 
(2, 'EX-003');

-- Inserir usuários
INSERT INTO Usuarios (nome, telefone, nacionalidade) VALUES 
('Usuário 1', '123456789', 'Brasileiro'), 
('Usuário 2', '987654321', 'Americano');

-- Inserir empréstimos
INSERT INTO Emprestimos (usuario_id, exemplar_id, data_emprestimo, estado) VALUES 
(1, 1, '2024-08-10', 'Emprestado'),
(2, 3, '2024-08-11', 'Emprestado');


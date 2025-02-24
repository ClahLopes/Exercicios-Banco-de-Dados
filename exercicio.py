import sqlite3

conexao = sqlite3.connect('banco_exercicio')
cursor = conexao.cursor()

def loop():
    for usuario in dados:
        print(usuario)

# EXERCÍCIO 1
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

# EXERCÍCIO 2
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (1, 'Ana Souza', 22, 'Engenharia')");
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (2, 'Bruno Lima', 24, 'Ciência de Dados')");
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (3, 'Carlos Mendes', 21, 'Marketing')");
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (4, 'Daniela Rocha', 23, 'Educação Física')");
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (5, 'Eduardo Castro', 25, 'Engenharia')");
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (6, 'Fernanda Alves', 22, 'Ciência de Dados')");
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (7, 'Gabriel Nunes', 24, 'Marketing')");
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (8, 'Helena Martins', 23, 'Educação Física')");
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (9, 'Claudia', 20, 'Psicologia')");
#cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (10, 'Victor Willker', 19, 'Educação Física')")

# EXERCÍCIO 3 - a) 
#dados = cursor.execute('SELECT * FROM alunos')
#loop()

# EXERCÍCIO 3 - b) 
#dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')
#loop()

# EXERCÍCIO 3 - c) 
#dados = cursor.execute('SELECT nome,idade FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
#loop()

# EXERCÍCIO 3 - d)
#cursor.execute("SELECT COUNT(*) FROM alunos")
#quantidade = cursor.fetchone()[0]
#print("Total de alunos:", quantidade)

# EXERCÍCIO 4
#cursor.execute('UPDATE alunos SET idade = 15 WHERE nome = "Claudia"')

# EXERCÍCIO 5
#cursor.execute('CREATE TABLE clientes(id PRIMARY KEY, nome VARCHAR(20), idade INT, saldo FLOAT)')
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, 'João Silva', 30, 1500.75)");
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, 'Maria Oliveira', 25, 3200.50)");
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, 'Pedro Santos', 40, 500.00)");
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, 'Ana Costa', 35, 2750.20)");
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, 'Lucas Mendes', 28, 1800.90)");
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (6, 'Claudia', 15, 120.90)");
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (7, 'Victor Willker', 20, 11.90)");

# EXERCÍCIO 6 - a)
#dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')
#loop()

# EXERCÍCIO 6 - b)
#dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
#media = cursor.fetchone()[0]
#media_formatada = round(media,2)
#print("Média do saldo dos clientes:" , media_formatada)

# EXERCÍCIO 6 - c)
#dados = cursor.execute('SELECT MAX(saldo) FROM clientes')
#max = cursor.fetchone()[0]
#print("Saldo máximo dos clientes:" , max)

# EXERCÍCIO 6 - d)
#dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
#quantidade = cursor.fetchone()[0]
#print("Clientes com saldo maior que 1000:", quantidade)

# EXERCÍCIO 7 - a)
#cursor.execute('UPDATE clientes SET saldo = 100.00 WHERE nome = "Victor Willker"')

# EXERCÍCIO 7 - b)
#cursor.execute('DELETE FROM clientes WHERE id = 2')

# EXERCÍCIO 8 
#cursor.execute('CREATE TABLE compras(id INTEGER PRIMARY KEY,cliente_id INTEGER, produto TEXT(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

#cursor.execute("INSERT INTO compras (cliente_id, produto, valor) VALUES(1, 'Notebook', 3500.00)")
#cursor.execute("INSERT INTO compras (cliente_id, produto, valor) VALUES(2, 'Smartphone', 1800.50)")
#cursor.execute("INSERT INTO compras (cliente_id, produto, valor) VALUES(3, 'Fone de Ouvido', 200.75)")
#cursor.execute("INSERT INTO compras (cliente_id, produto, valor) VALUES(1, 'Mouse Gamer', 150.90)")
#cursor.execute("INSERT INTO compras (cliente_id, produto, valor) VALUES(2, 'Teclado Mecânico', 320.00)")

#dados = cursor.execute("SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id;")
#loop()

conexao.commit()
conexao.close

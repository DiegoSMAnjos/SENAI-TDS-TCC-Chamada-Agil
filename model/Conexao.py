import mysql.connector


def conectar_banco():
    passwd = ""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=passwd,
        )
    except:
        try:
            passwd = "1234"
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=passwd,
            )
        except:
            print("Erro de autenticacao")

    cursor = conexao.cursor()
    cursor.execute("DROP DATABASE IF EXISTS db_chamada_agil;")
    cursor.execute("CREATE DATABASE IF NOT EXISTS db_chamada_agil;")
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=passwd,
        database="db_chamada_agil"
    )
    cursor = conexao.cursor()

    cria_tb_usuario = """CREATE TABLE IF NOT EXISTS tb_usuario (
                                    idUsuario INT(4) NOT NULL AUTO_INCREMENT,
                                    nome VARCHAR(20),
                                    PRIMARY KEY(idUsuario));"""
    cursor.execute(cria_tb_usuario)

    cria_tb_tipo_chamada = """CREATE TABLE IF NOT EXISTS tb_tipo_chamada (
                                    id INT NOT NULL AUTO_INCREMENT,
                                    nome VARCHAR(50),
                                    PRIMARY KEY(id));"""
    cursor.execute(cria_tb_tipo_chamada)

    cria_tb_localizacao = """CREATE TABLE IF NOT EXISTS tb_localizacao (
                                    id INT NOT NULL AUTO_INCREMENT,
                                    nome VARCHAR(50),
                                    PRIMARY KEY(id)
                                    );"""
    cursor.execute(cria_tb_localizacao)

    cria_tb_chamada = """CREATE TABLE IF NOT EXISTS tb_chamada (
                                id INT NOT NULL AUTO_INCREMENT,
                                idTipoChamada INT NOT NULL,
                                localizacao INT NOT NULL,
                                descricao VARCHAR(500),
                                status VARCHAR(20) DEFAULT 'Em Aberto',
                                PRIMARY KEY(id),
                                FOREIGN KEY(idTipoChamada) REFERENCES tb_tipo_chamada(id),
                                FOREIGN KEY(localizacao) REFERENCES tb_localizacao(id));"""
    cursor.execute(cria_tb_chamada)

    insere_usuario = """INSERT IGNORE INTO tb_usuario 
                           VALUES
                             (1111,'Professores'),
                             (2222,'Corpo Auxiliar');"""
    cursor.execute(insere_usuario)

    insere_tipo_chamada = """INSERT IGNORE INTO tb_tipo_chamada 
                               VALUES
                                 (1,'Outro (Especificar na descrição)'),
                                 (2,'Conexão com Internet'),
                                 (3,'Limpeza'),
                                 (4,'Projetor'),
                                 (5,'Marcadores de Quadro'),
                                 (6,'Computador do Docente'),
                                 (7,'Computador(es) dos Alunos');"""
    cursor.execute(insere_tipo_chamada)

    insere_localizacao = """INSERT IGNORE INTO tb_localizacao 
                               VALUES
                                 (1,'Outra (Especificar na descrição)'),
                                 (2,'Bloco B - Lab 01'),
                                 (3,'Bloco B - Lab 02'),
                                 (4,'Bloco A - Sala 01'),
                                 (5,'Bloco A - Sala 02'),
                                 (6,'Bloco A - Sala 03'),
                                 (7,'Bloco C - Sala 01'),
                                 (8,'Auditório');"""
    cursor.execute(insere_localizacao)

    insere_chamada = """INSERT IGNORE INTO tb_chamada
                            VALUES 
                                (1,2,3,'A pasta de compartilhamento de arquivos em rede parou de funcionar','Em Aberto'),
                                (2,3,5,'O chão da sala está sujo de lama','Em Aberto');"""
    cursor.execute(insere_chamada)

    conexao.commit()
    cursor.close()

    return conexao

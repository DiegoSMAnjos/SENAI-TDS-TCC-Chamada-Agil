import mysql.connector


def conectar_banco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
    )
    cursor = conexao.cursor()
    cursor.execute("DROP DATABASE IF EXISTS db_chamada_agil;")
    cursor.execute("CREATE DATABASE IF NOT EXISTS db_chamada_agil;")
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="db_chamada_agil"
    )
    cursor = conexao.cursor()
    cria_tb_usuario = """CREATE TABLE IF NOT EXISTS tb_usuario (
                                idUsuario INT(4) NOT NULL AUTO_INCREMENT,
                                nome VARCHAR(20),
                                PRIMARY KEY(idUsuario));"""
    cursor.execute(cria_tb_usuario)
    insere_tb_usuario = """INSERT IGNORE INTO tb_usuario 
                           VALUES
                             (1111,'administracao'),
                             (2222,'professores'),
                             (3333,'corpo_tecnico');
    """
    cursor.execute(insere_tb_usuario)
    conexao.commit()
    cursor.close()

    return conexao

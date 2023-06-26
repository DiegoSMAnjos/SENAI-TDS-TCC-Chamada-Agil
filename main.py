from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from model.Conexao import conectar_banco

app = QtWidgets.QApplication([])

telaInicio = uic.loadUi("view/telaInicio.ui")
telaProf = uic.loadUi("view/telaProf.ui")
telaCorpoAux = uic.loadUi("view/telaCorpoAux.ui")
senaiLogo = QPixmap("img/senai-logo.png")
imagemInicio = QPixmap("img/imagem-inicio.png")

telaInicio.show()

conexao = conectar_banco()


def fazerLogin(self=None):
    if telaInicio.lineEdit.text() == "1111":
        telaProf.show()
    elif telaInicio.lineEdit.text() == "2222":
        getListaTiposChamada(conexao)
        telaCorpoAux.show()
    else:
        QMessageBox().warning(self, "Erro de Acesso", "Insira um código válido")
        return
    telaInicio.close()


def atenderChamada(conn, self=None):
    selected_items = telaCorpoAux.tblChamadas.selectedItems()
    if not selected_items:
        print("No row selected.")
        QMessageBox().warning(self, "Erro", "Selecione uma chamada")
        return
    row = selected_items[0].row()
    row_data = []
    for column in range(telaCorpoAux.tblChamadas.columnCount()):
        item = telaCorpoAux.tblChamadas.item(row, column)
        if item is not None:
            row_data.append(item.text())

    print("Selected row as a tuple:", row_data)

    cursor = conn.cursor()
    sql = f"""UPDATE tb_chamada SET status = 'Concluida' WHERE id = {row_data[0]};
    """
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    getListaTiposChamada(conexao)


def abreChamada(conn, self=None):
    tipoProblema = telaProf.cbTipoProblema.currentText()
    local = telaProf.cbLocal.currentText()
    descricao = telaProf.txtEditDescricao.toPlainText()

    if tipoProblema[0] == '<' or local[0] == '<':
        QMessageBox().warning(self, "Erro de Inserção", "Insira dados válidos")
    else:
        cursor = conn.cursor()
        sql = f"""SELECT id FROM tb_tipo_chamada WHERE nome = '{tipoProblema}';
        """
        cursor.execute(sql)
        resultado = cursor.fetchone()
        numTipoProblema = resultado[0]
        sql = f"""SELECT id FROM tb_localizacao WHERE nome LIKE '{local}';
                """
        cursor.execute(sql)
        resultado = cursor.fetchone()
        numLocal = resultado[0]
        sql = f"""INSERT INTO tb_chamada (idTipoChamada, localizacao, descricao) VALUES
                    ({numTipoProblema},{numLocal},'{descricao}');
                """
        cursor.execute(sql)
        telaProf.cbTipoProblema.setCurrentIndex(0)
        telaProf.cbLocal.setCurrentIndex(0)
        telaProf.txtEditDescricao.clear()
        QMessageBox.information(self, "Chamada cadastrada", "Chamada cadastrada com sucesso!")
        conn.commit()
        cursor.close()


def trocaTelas(tela01, tela02):
    tela01.close()
    tela02.show()


def getListaTiposChamada(conn):
    cursor = conn.cursor()
    sql = """
        SELECT c.id AS ID, tc.nome AS Tipo, l.nome AS Local, c.status AS Status, c.descricao AS Descrição
        FROM tb_chamada c
        INNER JOIN tb_tipo_chamada tc ON (tc.id = c.idTipoChamada)
        INNER JOIN tb_localizacao l ON (c.localizacao = l.id)
        WHERE c.status = 'Em Aberto';"""
    cursor.execute(sql)
    registros = cursor.fetchall()
    row = 0
    telaCorpoAux.tblChamadas.setRowCount(len(registros))
    for registro in registros:
        telaCorpoAux.tblChamadas.setItem(row, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
        telaCorpoAux.tblChamadas.setItem(row, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
        telaCorpoAux.tblChamadas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
        telaCorpoAux.tblChamadas.setItem(row, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
        telaCorpoAux.tblChamadas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
        row += 1
    print(registros)
    conn.commit()
    cursor.close()
    if row != 0:
        telaCorpoAux.tblChamadas.resizeColumnsToContents()


def populaListaLocalizacao(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM tb_localizacao")
    results = cursor.fetchall()
    for result in results:
        telaProf.cbLocal.addItem(result[0])
    conn.commit()
    cursor.close()


def populaListaProblema(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM tb_tipo_chamada")
    results = cursor.fetchall()
    for result in results:
        telaProf.cbTipoProblema.addItem(result[0])
    conn.commit()
    cursor.close()


populaListaProblema(conexao)
populaListaLocalizacao(conexao)
telaInicio.btnLogin.clicked.connect(lambda: fazerLogin())
telaProf.btnVoltar.clicked.connect(lambda: trocaTelas(telaProf, telaInicio))
telaProf.btnSolicitar.clicked.connect(lambda: abreChamada(conexao))
telaCorpoAux.btnVoltar.clicked.connect(lambda: trocaTelas(telaCorpoAux, telaInicio))
telaCorpoAux.btnAtenderChamada.clicked.connect(lambda: atenderChamada(conexao))

app.exec()

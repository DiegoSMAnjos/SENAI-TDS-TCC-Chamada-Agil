from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from model.Conexao import conectar_banco

app = QtWidgets.QApplication([])

telaInicio = uic.loadUi("view/telaInicio.ui")
telaProf = uic.loadUi("view/telaProf.ui")
telaCorpoAux = uic.loadUi("view/telaCorpoAux.ui")
sucesso = uic.loadUi("view/sucesso.ui")
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


telaInicio.pushButton.clicked.connect(lambda: fazerLogin())


def trocaTelas(tela01, tela02):
    tela01.close()
    tela02.show()


def getListaTiposChamada(conn):
    cursor = conn.cursor()
    sql = """
        SELECT c.id AS ID, tc.nome AS Tipo, l.nome AS Local, c.status AS Status, c.descricao AS Descrição
        FROM tb_chamada c
        INNER JOIN tb_tipo_chamada tc ON (tc.id = c.idTipoChamada)
        INNER JOIN tb_localizacao l ON (c.localizacao = l.id);"""
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


telaProf.btnVoltar.clicked.connect(lambda: trocaTelas(telaProf, telaInicio))
telaCorpoAux.btnVoltar.clicked.connect(lambda: trocaTelas(telaCorpoAux, telaInicio))



app.exec()

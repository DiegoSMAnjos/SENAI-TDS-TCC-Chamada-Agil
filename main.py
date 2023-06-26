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
        SELECT * FROM tb_chamada;
    """
    cursor.execute(sql)
    registros = cursor.fetchall()
    for registro in registros:


    print(registros)


telaProf.btnVoltar.clicked.connect(lambda: trocaTelas(telaProf, telaInicio))
telaCorpoAux.btnVoltar.clicked.connect(lambda: trocaTelas(telaCorpoAux, telaInicio))


getListaTiposChamada(conexao)
app.exec()

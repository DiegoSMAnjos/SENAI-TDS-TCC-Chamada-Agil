from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from model.Conexao import conectar_banco

app = QtWidgets.QApplication([])

telaInicio = uic.loadUi("view/telaInicio.ui")
telaAdm = uic.loadUi("view/telaAdm.ui")
telaProf = uic.loadUi("view/telaProf.ui")
telaCorpoAux = uic.loadUi("view/telaCorpoAux.ui")
sucesso = uic.loadUi("view/sucesso.ui")
senaiLogo = QPixmap("img/senai-logo.png")
userCircle = QPixmap("img/user-circle.png")
imagemInicio = QPixmap("img/imagem-inicio.png")
'''
telaInicio.lblLogoSenai.setPixmap(senaiLogo)
telaInicio.lblUserCircle.setPixmap(userCircle)
telaInicio.lblImagemCapa.setPixmap(imagemInicio)
'''
telaInicio.show()

conexao = conectar_banco()


def fazerLogin(self=None):
    '''
    if telaInicio.lineEdit.text() == "1111":
        #tela.label.setText(
        #    "<html><head/><body><p align=\"center\"><span style=\" color:red; font-size:16pt;\">Olá Administrador!<br/></span></p></body></html>")
        telaInicio.close()
        telaAdm.show()
    '''
    if telaInicio.lineEdit.text() == "2222":
        telaProf.show()
    elif telaInicio.lineEdit.text() == "3333":
        telaCorpoAux.show()
    else:
        QMessageBox().warning(self, "Erro de Acesso", "Insira um código válido")
        return
    telaInicio.close()


telaInicio.pushButton.clicked.connect(lambda: fazerLogin())

app.exec()

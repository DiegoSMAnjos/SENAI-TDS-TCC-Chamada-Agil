from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
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


def fazerLogin():
    '''
    if telaInicio.lineEdit.text() == "1111":
        #tela.label.setText(
        #    "<html><head/><body><p align=\"center\"><span style=\" color:red; font-size:16pt;\">Olá Administrador!<br/></span></p></body></html>")
        telaInicio.close()
        telaAdm.show()
    '''
    if telaInicio.lineEdit.text() == "2222":
        #tela.label.setText(
        #    "<html><head/><body><p align=\"center\"><span style=\" color:red; font-size:16pt;\">Olá Professor!<br/></span></p></body></html>")

        telaProf.show()
    elif telaInicio.lineEdit.text() == "3333":
        #tela.label.setText(
        #    "<html><head/><body><p align=\"center\"><span style=\" color:red; font-size:16pt;\">Olá Corpo Auxiliar!<br/></span></p></body></html>")
        telaCorpoAux.show()
    else:
        #tela.label.setText(
        #    "<html><head/><body><p align=\"center\"><span style=\" color:red; font-size:16pt;\">Insira um código válido! (contacte a administração em caso de dúvidas)<br/></span></p></body></html>")
        return
        # sucesso.show()
    telaInicio.close()


telaInicio.pushButton.clicked.connect(lambda: fazerLogin())

app.exec()

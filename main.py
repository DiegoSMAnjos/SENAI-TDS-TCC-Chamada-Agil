from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from model.Conexao import conectar_banco
from model.Login import fazerLogin


app = QtWidgets.QApplication([])

telaInicio = uic.loadUi("view/telaInicio.ui")
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


def testeSucesso():
    sucesso.label.setText("<html><head/><body><p align=\"center\"><span style=\" color:red; font-size:16pt;\">Código Funcionando<br/></span></p></body></html>")
    sucesso.show()


# home.pushButton.clicked.connect(lambda: testeSucesso())
telaInicio.pushButton.clicked.connect(lambda: fazerLogin(sucesso, telaInicio))

app.exec()

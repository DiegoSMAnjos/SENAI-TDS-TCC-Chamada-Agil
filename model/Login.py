
def fazerLogin(tela,telaHome):
    if telaHome.lineEdit.text() == "1111":
        tela.label.setText(
            "<html><head/><body><p align=\"center\"><span style=\" color:red; font-size:16pt;\">Olá Administrador!<br/></span></p></body></html>")
        tela.show()

from PyQt5 import uic, QtWidgets
import mysql.connector
from PyQt5.QtGui import QPixmap

app = QtWidgets.QApplication([])
home = uic.loadUi("view/home.ui")
senaiLogo = QPixmap("img/senai-logo.png")
userCircle = QPixmap("img/user-circle.png")
home.lblLogoSenai.setPixmap(senaiLogo)
home.lblUserCircle.setPixmap(userCircle)
home.show()

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="db_voluntario")

"""
def cadastrar():
    nome = home.le_nome.text()
    idade = home.le_idade.text()
    genero = home.le_genero.currentText()
    turno = ""
    if home.radioMat.isChecked():
        turno = "Matutino"
    elif home.radioVesp.isChecked():
        turno = "Vespertino"
    elif home.radioNot.isChecked():
        turno = "Noturno"

    cursor = conexao.cursor()
    sql = "insert into tb_voluntario2 (nome, idade, genero, turno) values (%s, %s, %s, %s)"
    entrada = (str(nome), str(idade), str(genero), str(turno))
    cursor.execute(sql, entrada)
    conexao.commit()
    sucesso.show()
    limpar()


def limpar():
    home.le_nome.setText("")
    home.le_idade.setText("")

    # O codigo abaixo nao esta funcionando
    '''home.radioMat.setAutoExclusive(false)
    home.radioVesp.setAutoExclusive(false)
    home.radioNot.setAutoExclusive(false)
    home.radioMat.setChecked(false)
    home.radioVesp.setChecked(false)
    home.radioNot.setChecked(false)
    home.radioMat.setAutoExclusive(true)
    home.radioVesp.setAutoExclusive(true)
    home.radioNot.setAutoExclusive(true)'''

    # home.le_genero.currentText("")


def listar():
    lista.show()
    lista.list_nome.clear()
    lista.list_idade.clear()
    lista.list_genero.clear()
    cursor = conexao.cursor()
    # sql = "SELECT * FROM tb_voluntario"
    # sql = "SELECT * FROM tb_voluntario ORDER BY nome ASC, idade DESC"
    sql = "SELECT * FROM tb_voluntario2"
    cursor.execute(sql)
    registros = cursor.fetchall()
    # print(registros)
    for linha in registros:
        lista.list_nome.addItem(str(linha[1]))
        lista.list_idade.addItem(str(linha[2]))
        lista.list_genero.addItem(str(linha[3]))
        lista.list_turno.addItem(str(linha[4]))
    conexao.commit()


home.pb_enviar.clicked.connect(cadastrar)
home.pb_lista.clicked.connect(listar)
home.pb_limpar.clicked.connect(limpar)
"""

app.exec()

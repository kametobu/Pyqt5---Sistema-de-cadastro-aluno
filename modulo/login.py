from PyQt5.QtWidgets import QApplication,QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
from db.query import Banco
from template.Login import Ui_login
import hashlib 


class login(QMainWindow):
    def __init__(self,*args, **argvs):
        super(login,self).__init__(*args, **argvs)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.pushButton_Esqueceu.clicked.connect(self.esquece)
        self.ui.pushButton_Entrar.clicked.connect(self.entrar)
 

    def entrar(self):
        from modulo.home import Home
        db = Banco()
        user = self.ui.lineEdit_login.text()
        passw = self.ui.lineEdit_senha.text()
        res = hashlib.md5(passw.encode())
        passw = res.hexdigest()
        if user =="" or passw =="":
            QMessageBox.warning(QMessageBox(),"Alerta!", "Preencha todos os campos!")
        else:
            dados = db.pegar_dados("SELECT id,login FROM user login Where login = '{}' and password= '{}'".format(user,passw))
            if dados:
                Home.userLogado = dados
                QMessageBox.information(QMessageBox(),"Login realizado!","Login efetuado com sucesso!")
                self.close()
                self.window = Home()
                self.window.show()
            else:
                QMessageBox.warning(QMessageBox(),"Login erro!","Login não efetuado com sucesso!" )

    def esquece(self):
        from modulo.Email import Email
        self.close()
        self.window = Email()
        self.window.show()


          

from PyQt5.QtWidgets import QApplication,QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
from db.query import Banco
from template.Home import Ui_Home
import hashlib 


class Home(QMainWindow):
    userLogado = None
    def __init__(self,*args, **argvs):
        super(Home,self).__init__(*args, **argvs)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.ui.pushButton_User.clicked.connect(self.cadastroUser)
        self.ui.pushButton_unidade.clicked.connect(self.cadastroUnidade)
        self.ui.pushButton_Curso.clicked.connect(self.cadastroPosto)
        self.ui.pushButton_Home.clicked.connect(self.recarregar)
        self.ui.pushButton_Atividade.clicked.connect(self.cadAtividade)
        self.ui.pushButton_recar.clicked.connect(self.recarregar)
        self.ui.pushButton_sair.clicked.connect(self.sair)
        User = self.userLogado[0][1]
        self.ui.label_2.mousePressEvent = self.openUrl
        self.ui.label_3.mousePressEvent = self.openUrl
        self.ui.label_4.mousePressEvent = self.openUrl
        self.ui.pushButton_logado.setText(str(User))
        self.ui.pushButton_Home.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"text-align: left;\n"
"background-color: rgb(43,43,43);\n"
"}")    
    def sair(self):
        from modulo.login import login
        self.close()
        self.window = login()
        self.window.show()

    def recarregar(self):
        self.close()
        self.window = Home()
        self.window.show()
        

    def cadAtividade(self):
        from modulo.CadAtiv import CadAtividade
        CadAtividade.userLogado = self.userLogado
        self.close()
        self.window = CadAtividade()
        self.window.show()

    def cadastroUser(self):
        from modulo.CadUser import CadUser
        CadUser.userLogado = self.userLogado
        self.close()
        self.window = CadUser()
        self.window.show()
        
    def cadastroUnidade(self):
        from modulo.CadUnidade import CadUnidade
        CadUnidade.userLogado = self.userLogado
        self.close()
        self.window = CadUnidade()
        self.window.show()

    def cadastroPosto(self):
        from modulo.CadPost import CadPosto
        CadPosto.userLogado = self.userLogado
        self.close()
        self.window = CadPosto()
        self.window.show()
        
    def openUrl(self,event):
        url = QtCore.QUrl('https://www.sumare.edu.br/')
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Erro!')
          

from PyQt5.QtWidgets import QApplication,QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
from db.query import Banco
from template.CadPosT import Ui_curso
import hashlib 


class CadPosto(QMainWindow):
    userLogado = None
    def __init__(self,*args, **argvs):
        super(CadPosto,self).__init__(*args, **argvs)
        self.ui = Ui_curso()
        self.ui.setupUi(self)

        self.ui.pushButton_Cad.clicked.connect(self.add)
        self.ui.pushButton_User.clicked.connect(self.cadastroUser)
        self.ui.pushButton_Unidade.clicked.connect(self.cadastroUnidade)
        self.ui.pushButton_Curso.clicked.connect(self.recarregar)
        self.ui.pushButton_Home.clicked.connect(self.Home)
        self.ui.pushButton_Atividade.clicked.connect(self.cadAtividade)
        self.ui.pushButton_Reca.clicked.connect(self.recarregar)
        User = self.userLogado[0][1]
        self.carregadados()
        self.ui.pushButton_Atual.clicked.connect(self.atualizar)
        self.ui.pushButton_cancelar.clicked.connect(self.cancelar)
        self.ui.pushButton_Deletar.clicked.connect(self.deletar)
        self.ui.pushButton_Pes.clicked.connect(self.Pesquisar)
        self.ui.pushButton_Todos.clicked.connect(self.carregadados)
        self.ui.pushButton_logado.setText(str(User))

        self.ui.pushButton_Curso.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"text-align: left;\n"
"background-color: rgb(43,43,43);\n"
"}")

        self.ui.pushButton_Sair.clicked.connect(self.sair)
    def sair(self):
        from modulo.login import login
        self.close()
        self.window = login()
        self.window.show()

    def recarregar(self):
        self.close()
        self.window = CadPosto()
        self.window.show()

    def cadAtividade(self):
        from modulo.CadAtiv import CadAtividade
        CadAtividade.userLogado = self.userLogado
        self.close()
        self.window = CadAtividade()
        self.window.show()

    def Home(self):
        from modulo.home import Home
        self.close()
        self.window = Home()
        self.window.show()
        

    def cadastroUnidade(self):
        from modulo.CadUnidade import CadUnidade
        CadUnidade.userLogado = self.userLogado
        self.close()
        self.window = CadUnidade()
        self.window.show()
    
    
    def cadastroUser(self):
        from modulo.CadUser import CadUser
        CadUser.userLogado = self.userLogado
        self.close()
        self.window = CadUser()
        self.window.show()

    
    def add(self):
        db = Banco()
        Curso = self.ui.lineEdit_Area.text()
        if Curso == "" :
            QMessageBox.information(QMessageBox(),"Erro","Erro!, por favor preencher todos os campos!")
        else:
            confirmar = db.pegar_dados("SELECT * FROM Cursos WHERE curso = '{}'".format(Curso))
            if (len(confirmar) > 0):
                QMessageBox.warning(QMessageBox(),"Erro","Erro!, Atividade j?? Cadastrada!")
                self.ui.lineEdit_Area.setStyleSheet("QLineEdit{\n"
                                                    "background-color: rgb(216, 216, 216);\n"
                                                    "border-radius: 2px;\n"
                                                    "padding: 0px 10px;\n"
                                                    "border: 1px solid  rgb(0, 0, 0);\n"
                                                    "color: red;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLineEdit:hover{\n"
                                                    "border: 1px solid  rgb(33, 122, 255);\n"
                                                    "}")
            else:
                db.inserir_apaga_atualizar("INSERT INTO Cursos (curso) VALUES ('{}')".format(Curso))
                QMessageBox.information(QMessageBox(),"Sucesso!","Dados salvos com sucesso!")
                self.ui.lineEdit_Area.setText("")
                self.ui.pushButton_Atual.setText("Atualizar")
                self.ui.lineEdit_Area.setStyleSheet("QLineEdit{\n"
                                                    "background-color: rgb(216, 216, 216);\n"
                                                    "border-radius: 2px;\n"
                                                    "padding: 0px 10px;\n"
                                                    "border: 1px solid  rgb(0, 0, 0);\n"
                                                    "color: black;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLineEdit:hover{\n"
                                                    "border: 1px solid  rgb(33, 122, 255);\n"
                                                    "}")
                self.carregadados()
    def carregadados(self):
        db = Banco()
        lista = db.pegar_dados("SELECT * FROM Cursos")
        self.ui.tableWidget.setRowCount(0)
        self.ui.label_Quantidade.setText("Quantidade : {}".format(len(lista)))
        for linha , dados in enumerate(lista):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha,coluna_n, QTableWidgetItem(str(dados)))
                
        self.ui.tableWidget.setColumnWidth(0,50)
        self.ui.tableWidget.setColumnWidth(1,800)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.ui.tableWidget.verticalHeader().setVisible(False)

    def Pesquisar(self):
        db = Banco()
        pes = self.ui.lineEdit_Pesquisa.text()
        lista = db.pegar_dados("SELECT * FROM Cursos WHERE curso='{}'".format(str(pes)))
        self.ui.tableWidget.setRowCount(0)
        self.ui.label_Quantidade.setText("Quantidade : {}".format(len(lista)))
        for linha , dados in enumerate(lista):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha,coluna_n, QTableWidgetItem(str(dados)))
                
        self.ui.tableWidget.setColumnWidth(0,50)
        self.ui.tableWidget.setColumnWidth(1,800)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.ui.tableWidget.verticalHeader().setVisible(False)


    def deletar(self):
        db = Banco()
        linha = self.ui.tableWidget.currentRow()
        if linha >=0:
            delId = self.ui.tableWidget.item(linha,0).text()
            db.inserir_apaga_atualizar("UPDATE cadastroprincipal SET curso=Null WHERE cadastroprincipal.curso='{}'".format(delId))
            db.inserir_apaga_atualizar("DELETE FROM Cursos WHERE id='{}'".format(delId) )
            QMessageBox.information(QMessageBox(),"Deletado!","User deletado com sucesso!")
            self.carregadados()
        else:
            QMessageBox.warning(QMessageBox(),"Erro!","selecinar uma linha!")

    def cancelar(self):
        self.ui.lineEdit_Area.setText("")
        self.ui.pushButton_Atual.setText("Atualizar")
        self.carregadados()

    def atualizar(self):
        test = self.ui.pushButton_Atual.text()
        if test == "Atualizar":
            db = Banco()
            linha = self.ui.tableWidget.currentRow()
            AtId = self.ui.tableWidget.item(linha,0).text()
            dados = db.pegar_dados("SELECT curso FROM Cursos WHERE id='{}'".format(AtId))
            self.ui.lineEdit_Area.setText("{}".format(dados[0][0]))
            self.ui.pushButton_Atual.setText("Salvar")
        elif test == "Salvar":
            db = Banco()
            linha = self.ui.tableWidget.currentRow()
            AtId = self.ui.tableWidget.item(linha,0).text()
            curso = self.ui.lineEdit_Area.text()
            if curso == "":
                QMessageBox.information(QMessageBox(),"Erro","Erro!, por favor preencher todos os campos!")
            else:
                db.inserir_apaga_atualizar("UPDATE Cursos SET curso='%s' WHERE Cursos.id=%s"%(str(curso),AtId))
                self.ui.pushButton_Atual.setText("Atualizar")
                self.ui.lineEdit_Area.setText("")
                self.carregadados()





          

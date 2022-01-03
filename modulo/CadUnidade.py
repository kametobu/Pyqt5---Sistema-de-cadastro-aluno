from PyQt5.QtWidgets import QApplication,QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
from db.query import Banco
from template.CadUnidade import Ui_Unidade
import hashlib 


class CadUnidade(QMainWindow):
    userLogado = None
    def __init__(self,*args, **argvs):
        super(CadUnidade,self).__init__(*args, **argvs)
        self.ui = Ui_Unidade()
        self.ui.setupUi(self)

    
        self.ui.pushButton_User.clicked.connect(self.cadastroUser)
        self.ui.pushButton_Unidade.clicked.connect(self.recarregar)
        self.ui.pushButton_Curso.clicked.connect(self.cadastroPosto)
        self.ui.pushButton_Home.clicked.connect(self.Home)
        self.ui.pushButton_Atividade.clicked.connect(self.cadAtividade)
        self.ui.pushButton_Recar.clicked.connect(self.recarregar)
        User = self.userLogado[0][1]
        self.ui.pushButton_logado.setText(str(User))
        self.ui.pushButton_Cadastrar.clicked.connect(self.add)
        self.carregadados()
        self.ui.lineEdit_CEP.setInputMask('99999-999')
        self.ui.lineEdit_CNPJ.setInputMask('99999999/9999-99')
        self.ui.pushButton_Deletar.clicked.connect(self.deletar)
        self.ui.pushButton_Todos.clicked.connect(self.carregadados)
        self.ui.pushButton_Unidade.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"text-align: left;\n"
"background-color: rgb(43,43,43);\n"
"}")

        self.ui.pushButton_sair.clicked.connect(self.sair)
        self.ui.comboBox_Regi.addItems([str("Selecionar"),"SUL", "NORTE", "LESTE", "OESTE"])
        self.ui.pushButton_Pesquisar.clicked.connect(self.Pesquisar)
        self.ui.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.ui.pushButton_Atualizar.clicked.connect(self.atualizar)
    def sair(self):
        from modulo.login import login
        self.close()
        self.window = login()
        self.window.show()


    def recarregar(self):
        self.close()
        self.window = CadUnidade()
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
        

    def cadastroPosto(self):
        from modulo.CadPost import CadPosto
        CadPosto.userLogado = self.userLogado
        self.close()
        self.window = CadPosto()
        self.window.show()
    
    
    def cadastroUser(self):
        from modulo.CadUser import CadUser
        CadUser.userLogado = self.userLogado
        self.close()
        self.window = CadUser()
        self.window.show()

    def add(self):
        db = Banco()
        Unidade = self.ui.lineEdit_NomeUn.text()
        CEP = self.ui.lineEdit_CEP.text()
        enderco = self.ui.lineEdit_Endereco.text()
        CNPJ = self.ui.lineEdit_CNPJ.text()
        Regiao = self.ui.comboBox_Regi.currentText()
        if Unidade == "" or CEP == "" or CNPJ == "" or enderco == "" or Regiao == "Selecionar":
            QMessageBox.information(QMessageBox(),"Erro","Erro!, por favor preencher todos os campos!")
        else:
            confirmar = db.pegar_dados("SELECT * FROM unidades WHERE CNPJ = '{}'".format(CNPJ))
            if (len(confirmar) > 0):
                QMessageBox.warning(QMessageBox(),"Erro","Erro!, Atividade já Cadastrada!")
                self.ui.lineEdit_CNPJ.setStyleSheet("QLineEdit{\n"
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
                db.inserir_apaga_atualizar("INSERT INTO unidades (NomeUnidade,Endereço,CNPJ,CEP,Regiao) VALUES ('{}','{}','{}','{}','{}')".format(Unidade,enderco,CNPJ,CEP,Regiao))
                QMessageBox.information(QMessageBox(),"Sucesso!","Dados salvos com sucesso!")
                self.ui.lineEdit_NomeUn.setText("")
                self.ui.lineEdit_CEP.setText("")
                self.ui.lineEdit_CNPJ.setText("")
                self.ui.lineEdit_Endereco.setText("")
                self.ui.comboBox_Regi.setCurrentIndex(0)
                self.ui.pushButton_Atualizar.setText("Atualizar")
                self.ui.lineEdit_CNPJ.setStyleSheet("QLineEdit{\n"
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
        lista = db.pegar_dados("SELECT * FROM unidades")
        self.ui.tableWidget.setRowCount(0)
        self.ui.label_Quantidade.setText("Quantidade : {}".format(len(lista)))
        for linha , dados in enumerate(lista):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha,coluna_n, QTableWidgetItem(str(dados)))

        self.ui.tableWidget.setColumnWidth(0,50)
        self.ui.tableWidget.setColumnWidth(1,180)
        self.ui.tableWidget.setColumnWidth(2,180)
        self.ui.tableWidget.setColumnWidth(3,180)
        self.ui.tableWidget.setColumnWidth(4,180)
        self.ui.tableWidget.setColumnWidth(5,180)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.ui.tableWidget.verticalHeader().setVisible(False)

    def Pesquisar(self):
        db = Banco()
        pes = self.ui.lineEdit_Pesquisa.text()
        PesCNPJ= self.ui.checkBox_CNPJ.checkState() 
        PesRegiao = self.ui.checkBox_Regiao.checkState()
        if PesCNPJ == 2:
            lista = db.pegar_dados("SELECT * FROM unidades WHERE CNPJ='{}'".format(str(pes)))
        elif PesRegiao == 2:
            lista = db.pegar_dados("SELECT * FROM unidades WHERE regiao='{}'".format(str(pes)))
        else:
            lista = db.pegar_dados("SELECT * FROM unidades WHERE NomeUnidade='{}'".format(str(pes)))

        self.ui.tableWidget.setRowCount(0)
        self.ui.label_Quantidade.setText("Quantidade : {}".format(len(lista)))
        for linha , dados in enumerate(lista):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha,coluna_n, QTableWidgetItem(str(dados)))
                
        self.ui.tableWidget.setColumnWidth(0,50)
        self.ui.tableWidget.setColumnWidth(1,180)
        self.ui.tableWidget.setColumnWidth(2,180)
        self.ui.tableWidget.setColumnWidth(3,180)
        self.ui.tableWidget.setColumnWidth(4,180)
        self.ui.tableWidget.setColumnWidth(5,180)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.ui.tableWidget.verticalHeader().setVisible(False)
          
    def deletar(self):
        db = Banco()
        linha = self.ui.tableWidget.currentRow()
        if linha >=0:
            delId = self.ui.tableWidget.item(linha,0).text()
            db.inserir_apaga_atualizar("UPDATE cadastroprincipal SET unidade=Null WHERE cadastroprincipal.unidade='{}'".format(delId))
            db.inserir_apaga_atualizar("DELETE FROM unidades WHERE id='{}'".format(delId) )
            QMessageBox.information(QMessageBox(),"Deletado!","User deletado com sucesso!")
            self.carregadados()
        else:
            QMessageBox.warning(QMessageBox(),"Erro!","selecinar uma linha!")
    
    def cancelar(self):
        self.ui.lineEdit_NomeUn.setText("")
        self.ui.lineEdit_CEP.setText("")
        self.ui.lineEdit_CNPJ.setText("")
        self.ui.lineEdit_Endereco.setText("")
        self.ui.comboBox_Regi.setCurrentIndex(0)
        self.ui.pushButton_Atualizar.setText("Atualizar")
        self.carregadados()


    def atualizar(self):
        test = self.ui.pushButton_Atualizar.text()
        if test == "Atualizar":
            db = Banco()
            linha = self.ui.tableWidget.currentRow()
            AtId = self.ui.tableWidget.item(linha,0).text()
            dados = db.pegar_dados("SELECT NomeUnidade,Endereço, CNPJ,CEP,Regiao FROM unidades WHERE id='{}'".format(AtId))
            self.ui.lineEdit_NomeUn.setText("{}".format(dados[0][0]))
            self.ui.lineEdit_Endereco.setText("{}".format(dados[0][1]))
            self.ui.lineEdit_CNPJ.setText("{}".format(dados[0][2]))
            self.ui.lineEdit_CEP.setText("{}".format(dados[0][3]))
            self.ui.comboBox_Regi.setCurrentText("{}".format(dados[0][4]))
            self.ui.pushButton_Atualizar.setText("Salvar")
        elif test == "Salvar":
            db = Banco()
            linha = self.ui.tableWidget.currentRow()
            AtId = self.ui.tableWidget.item(linha,0).text()
            Unidade = self.ui.lineEdit_NomeUn.text()
            CEP = self.ui.lineEdit_CEP.text()
            enderco = self.ui.lineEdit_Endereco.text()
            CNPJ = self.ui.lineEdit_CNPJ.text()
            Regiao = self.ui.comboBox_Regi.currentText()
            if Unidade == "" or CEP == "" or CNPJ == "" or enderco == "" or Regiao == "Selecionar":
                QMessageBox.information(QMessageBox(),"Erro","Erro!, por favor preencher todos os campos!")
            else:
                db.inserir_apaga_atualizar("UPDATE unidades SET NomeUnidade='%s', endereço='%s', CNPJ='%s',CEP='%s',Regiao='%s' WHERE Unidades.id=%s"%(Unidade,enderco,CNPJ,CEP,Regiao,AtId))
                self.ui.pushButton_Atualizar.setText("Atualizar")
                self.ui.lineEdit_NomeUn.setText("")
                self.ui.lineEdit_CEP.setText("")
                self.ui.lineEdit_CNPJ.setText("")
                self.ui.lineEdit_Endereco.setText("")
                self.ui.comboBox_Regi.setCurrentIndex(0)
                self.carregadados()
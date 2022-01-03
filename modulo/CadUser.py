from PyQt5.QtWidgets import QApplication,QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
from db.query import Banco
from template.CadUser import Ui_User
import hashlib 
import re
import base64

class CadUser(QMainWindow):
    userLogado = None
    def __init__(self,*args, **argvs):
        super(CadUser,self).__init__(*args, **argvs)
        db = Banco()
        self.ui = Ui_User()
        self.ui.setupUi(self)
        self.ui.pushButton_User.clicked.connect(self.recarregar)
        self.ui.pushButton_Unidade.clicked.connect(self.cadastroUnidade)
        self.ui.pushButton_Curso.clicked.connect(self.cadastroPosto)
        self.ui.pushButton_Home.clicked.connect(self.Home)
        self.ui.pushButton_Atividade.clicked.connect(self.cadAtividade)
        self.ui.pushButton_Recar.clicked.connect(self.recarregar)
        User = self.userLogado[0][1]
        self.ui.pushButton_Logado.setText(str(User))
        self.ui.pushButton_Sair.clicked.connect(self.sair)

        rx = QtCore.QRegExp("^[a-z0-9A-Z]+[\._]?[a-z0-9A-Z]+[@]\w+[.][a-z]+[.][a-z]+$")
        validator = QtGui.QRegExpValidator(rx, self.ui.lineEdit_Email)
        self.ui.lineEdit_Email.setValidator(validator)

        SenhaIn = QtCore.QRegExp("[a-z0-9A-Z]{0,8}")
        validatorSenha = QtGui.QRegExpValidator(SenhaIn, self.ui.lineEdit_Senha)
        self.ui.lineEdit_Senha.setValidator(validatorSenha)

        self.ui.lineEdit_CPF.setInputMask('999.999.999-99')
        self.ui.lineEdit_Login.setInputMask('9999999')
        
        self.ui.pushButton_Cadastrar.clicked.connect(self.add)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.carregadados()
        self.ui.pushButton_Deletar.clicked.connect(self.deletar)
        self.ui.pushButton_Pesquisar.clicked.connect(self.Pesquisar)
        self.ui.pushButton_Todos.clicked.connect(self.Todos)
        self.ui.pushButton_Atualizar.clicked.connect(self.atualizar)
        qp = QPixmap(':/img/img/userLogado.png')
        self.ui.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.ui.Labelimg.setPixmap(qp.scaled(100,100,Qt.KeepAspectRatio))
        self.ui.Labelimg.setStyleSheet("border:2px solid rgb(43, 43, 43);\n"
"border-radius: 10px;\n"
"padding: 1em;\n"
)
        self.ui.pushButton_User.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"text-align: left;\n"
"background-color: rgb(43,43,43);\n"
"}")    
        Atividadelist = db.pegar_dados("SELECT * FROM atividades")
        self.ui.comboBox_Atividade.addItem(str("Selecionar"))
        for i in Atividadelist:
            self.ui.comboBox_Atividade.addItem(str(i[0]) + " - " + str(i[1]) )
   

        Cursoslist = db.pegar_dados("SELECT * FROM Cursos")
        self.ui.comboBox_curso.addItem(str("Selecionar"))
        for i in Cursoslist:
            self.ui.comboBox_curso.addItem(str(i[0]) + " - " + str(i[1]))
        

        Unidadelist = db.pegar_dados("SELECT id,NomeUnidade FROM unidades")
        self.ui.comboBox_Atividade_2.addItem(str("Selecionar"))
        for i in Unidadelist:
            self.ui.comboBox_Atividade_2.addItem(str(i[0]) + " - " + str(i[1]))


    def sair(self):
        from modulo.login import login
        self.close()
        self.window = login()
        self.window.show()

    def recarregar(self):
        self.close()
        self.window = CadUser()
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

    def cadastroPosto(self):
        from modulo.CadPost import CadPosto
        CadPosto.userLogado = self.userLogado
        self.close()
        self.window = CadPosto()
        self.window.show()


    def buscar(self):
        
        test = self.ui.ImgSrc.text()
        text = self.ui.btnBuscar.text()
        if text == "Mudar":
            test = ""
        if test == "":
            imagem = QFileDialog.getOpenFileName(self,'open file','./')
            self.ui.ImgSrc.setText("{}".format(imagem[0]))
            test = self.ui.Labelimg.text()
            self.ui.btnBuscar.setText('Mudar')
            qp = QPixmap('{}'.format(imagem[0]))
            self.ui.Labelimg.setStyleSheet("border:2px solid rgb(43, 43, 43);\n"
"border-radius: 10px;\n"
"padding: 1em;\n"
)
            self.ui.Labelimg.setPixmap(qp.scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        else:
            return test


   
        
    def add(self):
        db = Banco()
        Nome = self.ui.lineEdit_Nome.text()
        Login = self.ui.lineEdit_Login.text()
        Senha = self.ui.lineEdit_Senha.text()
        Email = self.ui.lineEdit_Email.text()
        validadorE = re.findall('@\w+.\w{0,3}.?\w+?',Email)
        CPF = self.ui.lineEdit_CPF.text()
        ImgSrc = self.ui.ImgSrc.text()

        try:
            with open(ImgSrc,'rb') as stream:
                blob = stream.read()
        except:
            blob = ""
            
        Atividade = re.findall('\d+',self.ui.comboBox_Atividade.currentText())
        Curso = re.findall('\d+',self.ui.comboBox_curso.currentText())
        Unidade = re.findall('\d+',self.ui.comboBox_Atividade_2.currentText())
        if Nome == "" or Login == "" or Email == "" or CPF == "" or len(Atividade) == 0 or len(Curso) == 0 or len(Unidade) == 0:
            QMessageBox.information(QMessageBox(),"Erro","Erro!, por favor preencher todos os campos!")
        else:
            confirmar = db.pegar_dados("SELECT * FROM cadastroprincipal WHERE login='{}' or CPF='{}' or email = '{}'".format(Login,CPF,Email))
            if (len(confirmar) > 0):
                QMessageBox.warning(QMessageBox(),"Erro","Erro!, User, Email ou CPF já Cadastrados!")
                self.ui.lineEdit_Email.setStyleSheet("QLineEdit{\n"
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
                self.ui.lineEdit_CPF.setStyleSheet("QLineEdit{\n"
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

                self.ui.lineEdit_Login.setStyleSheet("QLineEdit{\n"
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
            elif len(validadorE) == 0:
                QMessageBox.warning(QMessageBox(),"Erro","Erro!, Email Incorreto!")
                self.ui.lineEdit_Email.setStyleSheet("QLineEdit{\n"
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
                res = hashlib.md5(Senha.encode())
                Senha = res.hexdigest()
                db.add(Nome,CPF,Email,Login,Senha,Atividade[0],Curso[0],Unidade[0],blob)
                db.inserir_apaga_atualizar("INSERT INTO user (login, password) VALUES ('{}','{}')".format(Login,Senha))
                CadUser.email(Email,Nome,Login)
                QMessageBox.information(QMessageBox(),"Sucesso!","Dados salvos com sucesso!")
                self.ui.lineEdit_Nome.setText("")
                self.ui.lineEdit_Login.setText("")
                self.ui.lineEdit_Email.setText("")
                self.ui.lineEdit_CPF.setText("")
                self.ui.lineEdit_Senha.setText("")
                self.ui.ImgSrc.setText("")
                self.ui.comboBox_Atividade.setCurrentIndex(0)
                self.ui.comboBox_curso.setCurrentIndex(0)
                self.ui.comboBox_Atividade_2.setCurrentIndex(0)
                self.ui.lineEdit_Email.setStyleSheet("QLineEdit{\n"
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
                self.ui.lineEdit_CPF.setStyleSheet("QLineEdit{\n"
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

                self.ui.lineEdit_Login.setStyleSheet("QLineEdit{\n"
                                                    "background-color: rgb(216, 216, 216);\n"
                                                    "border-radius: 2px;\n"
                                                    "padding: 0px 10px;\n"
                                                    "border: 1px solid  rgb(0, 0, 0);\n"
                                                    "color:black;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLineEdit:hover{\n"
                                                    "border: 1px solid  rgb(33, 122, 255);\n"
                                                    "}")
                qp = QPixmap(':/img/img/userLogado.png')
                self.ui.Labelimg.setPixmap(qp.scaled(100,100,Qt.KeepAspectRatio))
                self.ui.btnBuscar.setText("Buscar")
                self.carregadados()
    

    def carregadados(self):
        db = Banco()
        lista = db.pegar_dados("""SELECT cadastroprincipal.id,cadastroprincipal.Nome,
        cadastroprincipal.CPF,cadastroprincipal.email,cadastroprincipal.login,atividades.atividade,unidades.NomeUnidade,
        Cursos.curso  FROM cadastroprincipal 
        LEFT JOIN atividades ON cadastroprincipal.atividade = atividades.id
        LEFT JOIN Cursos ON cadastroprincipal.curso = Cursos.id
        LEFT JOIN unidades ON cadastroprincipal.unidade = unidades.id ;""")
        self.ui.tableWidget.setRowCount(0)
        self.ui.label_Quantidade.setText("Quantidade : {}".format(len(lista)))
        for linha , dados in enumerate(lista):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha,coluna_n, QTableWidgetItem(str(dados)))
                
        self.ui.tableWidget.setColumnWidth(0,30)
        self.ui.tableWidget.setColumnWidth(1,140)
        self.ui.tableWidget.setColumnWidth(2,140)
        self.ui.tableWidget.setColumnWidth(3,180)
        self.ui.tableWidget.setColumnWidth(4,140)
        self.ui.tableWidget.setColumnWidth(5,140)
        self.ui.tableWidget.setColumnWidth(6,140)
        self.ui.tableWidget.setColumnWidth(7,140)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.pushButton_Atualizar.setText("Atualizar")


    def Pesquisar(self):
        db = Banco()
        pes = self.ui.lineEdit_Pesquisa.text()
        PesRA = self.ui.checkBox_RA.checkState() 
        PesCPF = self.ui.checkBox_CPF.checkState()
        if PesRA == 2:
            lista = db.pegar_dados("""SELECT cadastroprincipal.id,cadastroprincipal.Nome,
            cadastroprincipal.CPF,cadastroprincipal.email,cadastroprincipal.login,atividades.atividade,unidades.NomeUnidade,
            Cursos.curso  FROM cadastroprincipal 
            LEFT JOIN atividades ON cadastroprincipal.atividade = atividades.id 
            LEFT JOIN Cursos ON cadastroprincipal.curso = Cursos.id
            LEFT JOIN unidades ON cadastroprincipal.unidade = unidades.id WHERE login ='{}';""".format(str(pes)))
            self.ui.label_Quantidade.setText("Quantidade : {}".format(len(lista))) 
        elif PesCPF == 2:
            lista = db.pegar_dados("""SELECT cadastroprincipal.id,cadastroprincipal.Nome,
            cadastroprincipal.CPF,cadastroprincipal.email,cadastroprincipal.login,atividades.atividade,unidades.NomeUnidade,
            Cursos.curso  FROM cadastroprincipal 
            LEFT JOIN atividades ON cadastroprincipal.atividade = atividades.id 
            LEFT JOIN Cursos ON cadastroprincipal.curso = Cursos.id
            LEFT JOIN unidades ON cadastroprincipal.unidade = unidades.id WHERE cpf ='{}';""".format(str(pes)))
            self.ui.label_Quantidade.setText("Quantidade : {}".format(len(lista))) 
        else:
            lista = db.pegar_dados("""SELECT cadastroprincipal.id,cadastroprincipal.Nome,
            cadastroprincipal.CPF,cadastroprincipal.email,cadastroprincipal.login,atividades.atividade,unidades.NomeUnidade,
            Cursos.curso  FROM cadastroprincipal 
            LEFT JOIN atividades ON cadastroprincipal.atividade = atividades.id 
            LEFT JOIN Cursos ON cadastroprincipal.curso = Cursos.id
            LEFT JOIN unidades ON cadastroprincipal.unidade = unidades.id WHERE nome='{}';""".format(str(pes)))
            self.ui.label_Quantidade.setText("Quantidade : {}".format(len(lista))) 

        self.ui.tableWidget.setRowCount(0)
        self.ui.label_Quantidade.setText("Quantidade : {}".format(len(lista)))
        for linha , dados in enumerate(lista):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha,coluna_n, QTableWidgetItem(str(dados)))
                
        self.ui.tableWidget.setColumnWidth(0,30)
        self.ui.tableWidget.setColumnWidth(1,140)
        self.ui.tableWidget.setColumnWidth(2,140)
        self.ui.tableWidget.setColumnWidth(3,180)
        self.ui.tableWidget.setColumnWidth(4,140)
        self.ui.tableWidget.setColumnWidth(5,140)
        self.ui.tableWidget.setColumnWidth(6,140)
        self.ui.tableWidget.setColumnWidth(7,140)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.pushButton_Atualizar.setText("Atualizar")


    def Todos(self):
        self.carregadados()

    def deletar(self):
        db = Banco()
        linha = self.ui.tableWidget.currentRow()
        if linha >=0:
            delId = self.ui.tableWidget.item(linha,0).text()
            user = db.pegar_dados("SELECT login FROM cadastroprincipal WHERE id='{}'".format(delId) )
            db.inserir_apaga_atualizar("DELETE FROM user WHERE login='{}'".format(user[0][0]) )
            db.inserir_apaga_atualizar("DELETE FROM cadastroprincipal WHERE id='{}'".format(delId) )
            QMessageBox.information(QMessageBox(),"Deletado!","User deletado com sucesso!")
            self.carregadados()
        else:
            QMessageBox.warning(QMessageBox(),"Erro!","selecinar uma linha!")



    def atualizar(self):
        test = self.ui.pushButton_Atualizar.text()
        if test == "Atualizar":
            db = Banco()
            linha = self.ui.tableWidget.currentRow()
            if linha >=0:
                AtId = self.ui.tableWidget.item(linha,0).text()
                Atualizar = db.pegar_dados("""SELECT cadastroprincipal.Nome,
            cadastroprincipal.CPF,cadastroprincipal.email,cadastroprincipal.login,cadastroprincipal.senha,cadastroprincipal.atividade,atividades.atividade,cadastroprincipal.unidade,unidades.NomeUnidade,
            cadastroprincipal.curso,Cursos.curso  FROM cadastroprincipal 
            LEFT JOIN atividades ON cadastroprincipal.atividade = atividades.id 
            LEFT JOIN Cursos ON cadastroprincipal.curso = Cursos.id
            LEFT JOIN unidades ON cadastroprincipal.unidade = unidades.id WHERE cadastroprincipal.id='{}';""".format(AtId))

                
                self.ui.lineEdit_Nome.setText("{}".format(Atualizar[0][0]))
                self.ui.lineEdit_Login.setText("{}".format(Atualizar[0][3]))
                self.ui.lineEdit_Email.setText("{}".format(Atualizar[0][2]))
                self.ui.lineEdit_CPF.setText("{}".format(Atualizar[0][1]))
                self.ui.lineEdit_Senha.setText("{}".format(Atualizar[0][4]))
                
                self.ui.comboBox_Atividade.setCurrentText("{} - {}".format(Atualizar[0][5],Atualizar[0][6]))
                self.ui.comboBox_Atividade_2.setCurrentText("{} - {}".format(Atualizar[0][7],Atualizar[0][8]))
                self.ui.comboBox_curso.setCurrentText("{} - {}".format(Atualizar[0][9],Atualizar[0][10]))

                img = db.pegar_dados("SELECT IMG FROM cadastroprincipal WHERE id='{}'".format(AtId))
                qp = QPixmap()
                qp.loadFromData(img[0][0],'bin')
                self.ui.Labelimg.setStyleSheet("border:2px solid rgb(43, 43, 43);\n"
"border-radius: 10px;\n"
"padding: 1em;\n"
)
                self.ui.Labelimg.setPixmap(qp.scaled(100,100,Qt.KeepAspectRatio))
                
                test =self.ui.pushButton_Atualizar.setText("Salvar")
                self.ui.btnBuscar.setText('Mudar')
            else:
                QMessageBox.warning(QMessageBox(),"Erro!","selecinar uma linha!")

        elif test == "Salvar":
            db = Banco()
            linha = self.ui.tableWidget.currentRow()
            AtId = self.ui.tableWidget.item(linha,0).text()
            loginEnt = db.pegar_dados("SELECT login FROM cadastroprincipal WHERE id='{}'".format(AtId))
      
            Nome = self.ui.lineEdit_Nome.text()
            Login = self.ui.lineEdit_Login.text()
            Senha = self.ui.lineEdit_Senha.text()
            Email = self.ui.lineEdit_Email.text()
            validadorE = re.findall('@\w+.\w{0,3}.?\w+?',Email)
            CPF = self.ui.lineEdit_CPF.text()
            ImgSrc = self.ui.ImgSrc.text()
            try:
                with open(ImgSrc,'rb') as stream:
                    blob = stream.read()
            except:
                blob = ""
            Atividade = re.findall('\d+',self.ui.comboBox_Atividade.currentText())
            Curso = re.findall('\d+',self.ui.comboBox_curso.currentText())
            Unidade = re.findall('\d+',self.ui.comboBox_Atividade_2.currentText())
            self.ui.btnBuscar.setText('Mudar')
            tamanho = len(Senha)
            res = hashlib.md5(Senha.encode())
            Senha = res.hexdigest()
            if Nome == "" or Login == "" or Email == "" or CPF == "" or len(Atividade) == 0 or len(Curso) == 0 or len(Unidade) == 0:
                QMessageBox.information(QMessageBox(),"Erro","Erro!, por favor preencher todos os campos!")
            elif ImgSrc == "" and tamanho <= 8:
                db.inserir_apaga_atualizar("UPDATE cadastroprincipal SET nome='%s',cpf='%s',email='%s',login = '%s', senha='%s',atividade='%s',curso='%s',unidade='%s' WHERE cadastroprincipal.id=%s;"%(Nome,CPF,Email,Login,Senha,Atividade[0],Curso[0],Unidade[0],AtId))
                db.inserir_apaga_atualizar("UPDATE user SET login='{}', password='{}' WHERE user.login='{}'".format(Login,Senha,loginEnt[0][0]))
            elif ImgSrc == "" and tamanho > 8:
                db.inserir_apaga_atualizar("UPDATE cadastroprincipal SET nome='%s',cpf='%s',email='%s',login = '%s', atividade='%s',curso='%s',unidade='%s' WHERE cadastroprincipal.id=%s;"%(Nome,CPF,Email,Login,Atividade[0],Curso[0],Unidade[0],AtId))
                db.inserir_apaga_atualizar("UPDATE user SET login='{}' WHERE user.login='{}'".format(Login,loginEnt[0][0]))
            elif tamanho <= 8:
                db.upgrade(Nome,CPF,Email,Login,Senha,Atividade[0],Curso[0],Unidade[0],blob,AtId)
                db.inserir_apaga_atualizar("UPDATE user SET login='{}', password='{}' WHERE user.login='{}'".format(Login,Senha,loginEnt[0][0]))
            else:
                db.upgradeS(Nome,CPF,Email,Login,Atividade[0],Curso[0],Unidade[0],blob,AtId)
                db.inserir_apaga_atualizar("UPDATE user SET login='{}' WHERE user.login='{}'".format(Login,loginEnt[0][0]))
            
            self.ui.lineEdit_Nome.setText("")
            self.ui.lineEdit_Login.setText("")
            self.ui.lineEdit_Email.setText("")
            self.ui.lineEdit_CPF.setText("")
            self.ui.lineEdit_Senha.setText("")
            self.ui.ImgSrc.setText("")
            self.ui.comboBox_Atividade.setCurrentIndex(0)
            self.ui.comboBox_curso.setCurrentIndex(0)
            self.ui.comboBox_Atividade_2.setCurrentIndex(0)
            self.ui.lineEdit_Email.setStyleSheet("QLineEdit{\n"
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
            self.ui.lineEdit_CPF.setStyleSheet("QLineEdit{\n"
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
            self.ui.lineEdit_Login.setStyleSheet("QLineEdit{\n"
                                                "background-color: rgb(216, 216, 216);\n"
                                                "border-radius: 2px;\n"
                                                "padding: 0px 10px;\n"
                                                "border: 1px solid  rgb(0, 0, 0);\n"
                                                "color:black;\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit:hover{\n"
                                                "border: 1px solid  rgb(33, 122, 255);\n"
                                                "}")
            qp = QPixmap(':/img/img/userLogado.png')
            self.ui.Labelimg.setPixmap(qp.scaled(100,100,Qt.KeepAspectRatio))
            self.ui.btnBuscar.setText("Buscar")
            test =self.ui.pushButton_Atualizar.setText("Atualizar")
            self.carregadados()

    def cancelar(self): 
            self.ui.lineEdit_Nome.setText("")
            self.ui.lineEdit_Login.setText("")
            self.ui.lineEdit_Email.setText("")
            self.ui.lineEdit_CPF.setText("")
            self.ui.lineEdit_Senha.setText("")
            self.ui.ImgSrc.setText("")
            self.ui.comboBox_Atividade.setCurrentIndex(0)
            self.ui.comboBox_curso.setCurrentIndex(0)
            self.ui.comboBox_Atividade_2.setCurrentIndex(0)
            self.ui.lineEdit_Email.setStyleSheet("QLineEdit{\n"
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
            self.ui.lineEdit_CPF.setStyleSheet("QLineEdit{\n"
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
            self.ui.lineEdit_Login.setStyleSheet("QLineEdit{\n"
                                                "background-color: rgb(216, 216, 216);\n"
                                                "border-radius: 2px;\n"
                                                "padding: 0px 10px;\n"
                                                "border: 1px solid  rgb(0, 0, 0);\n"
                                                "color:black;\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit:hover{\n"
                                                "border: 1px solid  rgb(33, 122, 255);\n"
                                                "}")
            qp = QPixmap(':/img/img/userLogado.png')
            self.ui.Labelimg.setPixmap(qp.scaled(100,100,Qt.KeepAspectRatio))
            self.ui.btnBuscar.setText("Buscar")
            self.ui.pushButton_Atualizar.setText("Atualizar")
            self.carregadados()                                                                                   
        
    def email(Email,Nome,Login):
        import time
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from PIL import Image, ImageFont, ImageDraw  
        from email.mime.image import MIMEImage

        diretorio = os.path.dirname(os.path.realpath(__file__))

        db = Banco()
        try:
            user = "Alann"
            smtp_ssl_host = 'smtp.gmail.com'
            smtp_ssl_port = 465
            username = 'alunonaoresponder@gmail.com'
            password = 'Aluno2020'
            from_addr = 'alunonaoresponder@gmail.com'
            to_addrs = Email
            message = MIMEMultipart('alternative')
            message['subject'] = 'Não Responder'
            message['from'] = from_addr
            message['to'] = Email
            #message.attach(MIMEText('<img src="C:/Users/Alann/Pictures/COmpleto/PyQt5 - Mysql - COM/a.png">','html'))
#-------    ----     --------------------------------
            image = Image.open(os.path.join('./img/', 'AssLG.png')) 
            draw = ImageDraw.Draw(image)  
            font = ImageFont.truetype(os.path.join('./img/', 'MADE Tommy Soft Black PERSONAL USE.otf'), 12)
            fontT = ImageFont.truetype(os.path.join('./img/', 'MADE Tommy Soft Black PERSONAL USE.otf'), 18)
            fontIn = ImageFont.truetype(os.path.join('./img/', 'MADE Tommy Soft Black PERSONAL USE.otf'), 10)
            textN = 'Seja Bem-vindo'
            draw.text((60, 40), textN, font = fontT, align ="left") 
            text = 'Prezado(a) {},'.format(Nome)
            draw.text((25, 100), text, font = font, align ="left")
            text = '        Seja-Bem vindo!\n{} seu login é {}\n e para baixar o app click no botão abaixo.'.format(Nome,Login)
            draw.text((25, 130), text, font = font, align ="left")
            text = 'Atenciosamente,'
            draw.text((25, 200), text, font = font, align ="left")
            text = '    Instituto Sumaré'
            draw.text((25, 220), text, font = font, align ="left")
            text = 'Avenida Doutor Arnaldo, 1793 - Sumaré'
            draw.text((100, 330), text, font = fontIn, align ="left")
            text = 'Central do Candidato: 3003-9997 |'
            draw.text((100, 340), text, font = fontIn, align ="left")
            text = 'Central do Aluno: 4118-4457'
            draw.text((100, 350), text, font = fontIn, align ="left")
            image.save('./img/a.png')  
            #---     ----------------------------------------
            with open('./img/a.png','rb') as fp:
                img = MIMEImage(fp.read())
                fp.close()
                img.add_header('content-ID','<image1>')
            message.attach(img)
            message.attach(MIMEText('''
            <div class="nH" style="">
            <div style="font-family:arial,sans-serif;width:650px;margin:0px auto;">
            <div style="width:650px;margin:5px 0px 10px 0px;background-color:#f1f1ef;border-radius:5px;box-shadow: 10px 5px 5px black;">
            <div style="width:650px;vertical-align:top;text-align:center">
            <a href="https://sumare.edu.br/" target="_blank">
            <img src="cid:image1" style="max-width:650px;border-radius:3px 3px 0 0; width: 100%; ">
            </a>
            </div>
            <table style="width:650px;padding:20px"><tbody>
            <tr>
            <td style="width:60%;text-align:left">
            <div style="font-size:21px;line-height:26px;color:#000000;font-weight:500">Baixar o App</div>
            <div style="margin-top:10px;font-size:14px;line-height:22px;color:#626262;word-wrap:break-word">
            Click no botão para Baixar o App
            </div>
            </td>
            <td style="vertical-align:bottom;text-align:right">
            <div style="float:right">
            <a href="https://sumare.edu.br/" target="_blank" style="text-decoration:none">
            <span style="padding:13px 13px 12px 13px;border-radius:3px;font-size:12px;font-weight:normal;color:#ffffff;text-decoration:none;background-color:#2cacf1;display:block;text-align:center;line-height:22px;box-shadow:1px 3px 4px #b2b2b2;white-space:normal;text-transform:uppercase">Sumare</span></a>
            </div>
            </td>
            </tr>
            <tr>
            <td style="width:60%;text-align:left">
            <div style="font-size:21px;line-height:26px;color:#000000;font-weight:500">Avaliação</div>
            <div style="margin-top:10px;font-size:14px;line-height:22px;color:#626262;word-wrap:break-word">
            Click no botão para avaliar nosso serviço
            </div>
            </td>
            <td style="vertical-align:bottom;text-align:right">
            <div style="float:right">
            <a href="http://sumarealuno.pythonanywhere.com" target="_blank" style="text-decoration:none">
            <span style="padding:13px 13px 12px 13px;border-radius:3px;font-size:17px;font-weight:normal;color:#ffffff;text-decoration:none;background-color:#2cacf1;display:block;text-align:center;line-height:22px;box-shadow:1px 3px 4px #b2b2b2;white-space:normal;text-transform:uppercase">Avaliar</span></a>
            </div>
            </td>
            </tr>

            <tr>
            <td style="width:60%;text-align:left">
            <a href="http://sumarealuno.pythonanywhere.com/termo"> Termos de Uso</a>
            </td>
            </tr>

            </tbody>
            </table>
            </div>
            </div>
            </div>
            '''.format(img), 'html'))
            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(username, password)
            server.sendmail(from_addr, to_addrs, message.as_string())
            server.quit()
        except:
            pass
         
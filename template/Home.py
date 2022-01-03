# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(self.centralwidget)
        self.top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnMenu = QtWidgets.QFrame(self.top)
        self.btnMenu.setMaximumSize(QtCore.QSize(120, 50))
        self.btnMenu.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.btnMenu.setFrameShape(QtWidgets.QFrame.Box)
        self.btnMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btnMenu.setObjectName("btnMenu")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.btnMenu)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_menu = QtWidgets.QPushButton(self.btnMenu)
        self.pushButton_menu.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_menu.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu.setIcon(icon)
        self.pushButton_menu.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.verticalLayout_10.addWidget(self.pushButton_menu)
        self.horizontalLayout_2.addWidget(self.btnMenu)
        self.menutop = QtWidgets.QFrame(self.top)
        self.menutop.setMinimumSize(QtCore.QSize(0, 50))
        self.menutop.setMaximumSize(QtCore.QSize(16777215, 50))
        self.menutop.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.menutop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menutop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menutop.setObjectName("menutop")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.menutop)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_12 = QtWidgets.QFrame(self.menutop)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_8.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.menutop)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label = QtWidgets.QLabel(self.frame_13)
        self.label.setGeometry(QtCore.QRect(30, 0, 171, 51))
        self.label.setStyleSheet("background-image: url(:/img/img/LogoP.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.menutop)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_6.addWidget(self.frame_15)
        self.frame_11 = QtWidgets.QFrame(self.frame_14)
        self.frame_11.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_recar = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_recar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/recaregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_recar.setIcon(icon1)
        self.pushButton_recar.setObjectName("pushButton_recar")
        self.horizontalLayout_7.addWidget(self.pushButton_recar)
        self.pushButton_logado = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_logado.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_logado.setStyleSheet("color: white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/userLogado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logado.setIcon(icon2)
        self.pushButton_logado.setObjectName("pushButton_logado")
        self.horizontalLayout_7.addWidget(self.pushButton_logado)
        self.pushButton_sair = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_sair.setStyleSheet("color: white;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sair.setIcon(icon3)
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.horizontalLayout_7.addWidget(self.pushButton_sair)
        self.horizontalLayout_6.addWidget(self.frame_11)
        self.horizontalLayout_8.addWidget(self.frame_14)
        self.horizontalLayout_2.addWidget(self.menutop)
        self.verticalLayout.addWidget(self.top)
        self.Conteudo = QtWidgets.QFrame(self.centralwidget)
        self.Conteudo.setStyleSheet("")
        self.Conteudo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Conteudo.setObjectName("Conteudo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Conteudo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu = QtWidgets.QFrame(self.Conteudo)
        self.menu.setMinimumSize(QtCore.QSize(50, 0))
        self.menu.setMaximumSize(QtCore.QSize(120, 16777215))
        self.menu.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.pushButton_Home = QtWidgets.QPushButton(self.menu)
        self.pushButton_Home.setGeometry(QtCore.QRect(10, 0, 100, 30))
        self.pushButton_Home.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_Home.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(43,43,43);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Home.setIcon(icon4)
        self.pushButton_Home.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.pushButton_User = QtWidgets.QPushButton(self.menu)
        self.pushButton_User.setGeometry(QtCore.QRect(10, 40, 100, 30))
        self.pushButton_User.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_User.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(43,43,43);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/userInfo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_User.setIcon(icon5)
        self.pushButton_User.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_User.setObjectName("pushButton_User")
        self.pushButton_unidade = QtWidgets.QPushButton(self.menu)
        self.pushButton_unidade.setGeometry(QtCore.QRect(10, 80, 100, 30))
        self.pushButton_unidade.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_unidade.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(43,43,43);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img/Unidades.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_unidade.setIcon(icon6)
        self.pushButton_unidade.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_unidade.setObjectName("pushButton_unidade")
        self.pushButton_Curso = QtWidgets.QPushButton(self.menu)
        self.pushButton_Curso.setGeometry(QtCore.QRect(10, 120, 100, 30))
        self.pushButton_Curso.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Curso.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(43,43,43);\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img/PostoTrabalho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Curso.setIcon(icon7)
        self.pushButton_Curso.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Curso.setObjectName("pushButton_Curso")
        self.pushButton_Atividade = QtWidgets.QPushButton(self.menu)
        self.pushButton_Atividade.setGeometry(QtCore.QRect(10, 160, 100, 30))
        self.pushButton_Atividade.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Atividade.setStyleSheet("QPushButton{\n"
"border-radius: 8px;\n"
"font: 87 8pt \"Arial Black\";\n"
"color: white;\n"
"text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(43,43,43);\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/img/Atividade.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Atividade.setIcon(icon8)
        self.pushButton_Atividade.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Atividade.setObjectName("pushButton_Atividade")
        self.horizontalLayout.addWidget(self.menu)
        self.conte = QtWidgets.QFrame(self.Conteudo)
        self.conte.setStyleSheet("background-color: rgb(83, 83, 83);")
        self.conte.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conte.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conte.setObjectName("conte")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.conte)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.conte)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("QLabel{\n"
"border-image: url(:/img/img/fundo.jpg) 0 0 0 0 stretch stretch;\n"
"border-radius: 10px;\n"
"}")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setStyleSheet("QLabel{\n"
"border-image: url(:/img/img/Promo1.jpg) 0 0 0 0 stretch stretch;;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"box-shadow: 5px 10px #888888;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);\n"
"font: 87 8pt \"Arial Black\";\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setStyleSheet("QLabel{\n"
"border-image: url(:/img/img/Promo2.jpg)0 0 0 0 stretch stretch;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);\n"
"font: 87 8pt \"Arial Black\";\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.conte)
        self.verticalLayout.addWidget(self.Conteudo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_menu.setText(_translate("MainWindow", "Menu"))
        self.pushButton_logado.setText(_translate("MainWindow", "Admin"))
        self.pushButton_sair.setText(_translate("MainWindow", "Sair"))
        self.pushButton_Home.setText(_translate("MainWindow", "Home"))
        self.pushButton_User.setText(_translate("MainWindow", " User"))
        self.pushButton_unidade.setText(_translate("MainWindow", " Unidade"))
        self.pushButton_Curso.setText(_translate("MainWindow", "Curso"))
        self.pushButton_Atividade.setText(_translate("MainWindow", " Atividade"))
        self.label_5.setText(_translate("MainWindow", "Promoção 1"))
        self.label_6.setText(_translate("MainWindow", "Promoção 2"))
import template.Principal_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

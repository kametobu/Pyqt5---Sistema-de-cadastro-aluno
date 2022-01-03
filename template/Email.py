# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Email.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_email(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 630)
        MainWindow.setMinimumSize(QtCore.QSize(200, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top = QtWidgets.QFrame(self.centralwidget)
        self.Top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Top.setStyleSheet("background-color: rgb(23, 23, 23);")
        self.Top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top.setObjectName("Top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Top)
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.Top)
        self.mid = QtWidgets.QFrame(self.centralwidget)
        self.mid.setStyleSheet("QFrame{\n"
"\n"
"    background-image: url(:/img/img/sumare.png);\n"
"background-size: 100% 100%;\n"
"background-repeat: no-repeat;\n"
"}\n"
"")
        self.mid.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid.setObjectName("mid")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mid)
        self.horizontalLayout.setContentsMargins(9, 20, 9, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login = QtWidgets.QFrame(self.mid)
        self.login.setMaximumSize(QtCore.QSize(500, 500))
        self.login.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"background-image: url();\n"
"border-radius: 5px;")
        self.login.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login.setObjectName("login")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.login)
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QFrame(self.login)
        self.logo.setMaximumSize(QtCore.QSize(16777215, 100))
        self.logo.setStyleSheet("\n"
"background-color: rgb(53, 63, 83);")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.logo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.logo)
        self.label_4.setStyleSheet("background-image: url(:/img/img/Logo.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-size: auto;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.logo)
        self.frame = QtWidgets.QFrame(self.login)
        self.frame.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setStyleSheet("background-image: url(:/img/img/email.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-size: auto;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_email = QtWidgets.QLabel(self.frame_4)
        self.label_email.setMinimumSize(QtCore.QSize(50, 30))
        self.label_email.setStyleSheet("background-color: rgb(173, 173, 173);\n"
"color: rgb(0,0,0);\n"
"font-weight: bold;\n"
"border: 1px solid rgb(0,0,0);\n"
"")
        self.label_email.setAlignment(QtCore.Qt.AlignCenter)
        self.label_email.setObjectName("label_email")
        self.horizontalLayout_4.addWidget(self.label_email)
        self.lineEdit_email = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_email.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_email.setStyleSheet("QLineEdit{\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;\n"
"padding: 0px 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid  rgb(33, 122, 255);\n"
"}\n"
"QLineEdit:pressed{\n"
"padding: 0px 10px;\n"
"border: 1px solid blue;\n"
"}")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_4.addWidget(self.lineEdit_email)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.progressBar = QtWidgets.QProgressBar(self.frame_6)
        self.progressBar.setStyleSheet("\n"
"QProgressBar{\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    color: rgb(255, 255, 255);\n"
"background-image: url(:/img/img/progs.png);\n"
"border-radius: 10px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_7.addWidget(self.progressBar)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_Login = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_Login.setStyleSheet("QPushButton{\n"
"\n"
"color: rgb(43,43,43);\n"
"font: 87 10pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0,0,0);\n"
"}\n"
"")
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.horizontalLayout_8.addWidget(self.pushButton_Login)
        self.horizontalLayout_7.addWidget(self.frame_9)
        self.horizontalLayout_6.addWidget(self.frame_8)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.login)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_Enviar = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_Enviar.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_Enviar.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(53, 63, 83);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(70, 81, 115);\n"
"    \n"
"}")
        self.pushButton_Enviar.setObjectName("pushButton_Enviar")
        self.verticalLayout_4.addWidget(self.pushButton_Enviar)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.login)
        self.verticalLayout.addWidget(self.mid)
        self.bot = QtWidgets.QFrame(self.centralwidget)
        self.bot.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bot.setStyleSheet("background-color: rgb(23, 23, 23);")
        self.bot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bot.setObjectName("bot")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bot)
        self.horizontalLayout_5.setContentsMargins(0, 20, 5, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.bot)
        self.label_2.setStyleSheet("background-color: rgb(23, 23, 23);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.bot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_email.setText(_translate("MainWindow", "E-mail "))
        self.pushButton_Login.setText(_translate("MainWindow", "Login"))
        self.pushButton_Enviar.setText(_translate("MainWindow", "Enviar"))
        self.label_2.setText(_translate("MainWindow", "Create by Alann"))
import template.Login_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_email()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
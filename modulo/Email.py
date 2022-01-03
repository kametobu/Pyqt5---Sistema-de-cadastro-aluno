from PyQt5.QtWidgets import QApplication,QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
from db.query import Banco
from template.Email import Ui_email
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image, ImageFont, ImageDraw  
from email.mime.image import MIMEImage

diretorio = os.path.dirname(os.path.realpath(__file__))

class Email(QMainWindow):
    def __init__(self,*args, **argvs):
        super(Email,self).__init__(*args, **argvs)
        self.ui = Ui_email()
        self.ui.setupUi(self)
        self.ui.pushButton_Login.clicked.connect(self.login)
        rx = QtCore.QRegExp("^[a-z0-9A-Z]+[\._]?[a-z0-9A-Z]+[@]\w+[.][a-z]+[.][a-z]+$")
        validator = QtGui.QRegExpValidator(rx, self.ui.lineEdit_email)
        self.ui.lineEdit_email.setValidator(validator)
        self.ui.pushButton_Enviar.clicked.connect(self.email)
        


    def ProgressoEmail(self):
        for i in range(101):
            time.sleep(0.05)
            self.ui.progressBar.setValue(i)


    def email(self):
        db = Banco()
        Email = self.ui.lineEdit_email.text()
        if Email =="":
            QMessageBox.warning(QMessageBox(),"Alerta!", "Preencha todos os campos!")
        else:
            dados = db.pegar_dados("SELECT nome FROM cadastroprincipal Where email='{}' ".format(Email))
            
            if len(dados)>0:
                try:
                    user = dados[0][0]
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



#-----------        --------------------------------
                    image = Image.open(os.path.join('./img/', 'AssLG.png')) 
                    draw = ImageDraw.Draw(image)  
                    font = ImageFont.truetype(os.path.join('./img/', 'MADE Tommy Soft Black PERSONAL USE.otf'), 12)
                    fontT = ImageFont.truetype(os.path.join('./img/', 'MADE Tommy Soft Black PERSONAL USE.otf'), 18)
                    fontIn = ImageFont.truetype(os.path.join('./img/', 'MADE Tommy Soft Black PERSONAL USE.otf'), 10)
                    textN = 'Recuperação de senha'
                    draw.text((60, 40), textN, font = fontT, align ="left") 
                    text = 'Prezado(a) {},'.format(user)
                    draw.text((25, 100), text, font = font, align ="left")
                    text = '    Recentemente, você solicitou a redefinição \nde senha para acessar o portal do aluno. Pa-\nra concluir o processo, clique no botão abaixo.'
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

        #---        ----------------------------------------
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
                    <div style="font-size:21px;line-height:26px;color:#000000;font-weight:500">Redefinir Senha</div>
                    <div style="margin-top:10px;font-size:14px;line-height:22px;color:#626262;word-wrap:break-word">
                    Click no botão para redefinir sua senha
                    </div>
                    </td>
                    <td style="vertical-align:bottom;text-align:right">
                    <div style="float:right">
                    <a href="#" target="_blank" style="text-decoration:none">
                    <span style="padding:13px 13px 12px 13px;border-radius:3px;font-size:12px;font-weight:normal;color:#ffffff;text-decoration:none;background-color:#2cacf1;display:block;text-align:center;line-height:22px;box-shadow:1px 3px 4px #b2b2b2;white-space:normal;text-transform:uppercase">Redefinir senha</span></a>
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
                    <a href="http://sumarealuno.pythonanywhere.com/" target="_blank" style="text-decoration:none">
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
                    self.ProgressoEmail()
                    server.quit()
                    self.ui.progressBar.setValue(101)
                    QMessageBox.information(QMessageBox(),"Email enviado","E-mail Enviado com sucesso")
                except Exception as e:
                    print(e)
                    QMessageBox.warning(QMessageBox(),"Erro","Por favor tente novamente")
            else:
                QMessageBox.warning(QMessageBox(),"Email Invalido","E-mail Invalido")



    def login(self):
        from modulo.login import login
        self.close()
        self.window = login()
        self.window.show()

       
        



          

from PyQt5.QtWidgets import QApplication,QWidget, QPushButton, QDialog
import os,sys
from modulo.login import login

sys.path.append('../')

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = login()
    window.show()
sys.exit(app.exec_())

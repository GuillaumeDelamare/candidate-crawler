# -*- coding: utf-8 -*-

'''
Created on 8 janv. 2015

@author: Julie S
'''

### External modules importation ###

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QSizePolicy, QLayout, QBoxLayout
from candidatecrawler.core import toolbox

### End of external modules importation ###
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

### Classes ###

class AdminWindowUI(object):
    def setupUi(self, AdminWindow):
        """GUI building for Admin window"""
        AdminWindow.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.centralwidget = QtGui.QWidget(AdminWindow)
        self.qbox = QBoxLayout(QBoxLayout.TopToBottom, self.centralwidget)
        self.centralwidget.setLayout(self.qbox)
        
        ### Partie haute de la fenêtre###
        self.boutton_parcourir = QtGui.QPushButton()
        self.boutton_parcourir.setText(_translate("AdminWindow", "Parcourir", None))
        
        self.chemin = QtGui.QLineEdit(self.centralwidget)
        
        self.hbox_workspace = QtGui.QHBoxLayout()
        self.hbox_workspace.addWidget(self.chemin)
        self.hbox_workspace.addWidget(self.boutton_parcourir)
        
        self.workpace = QtGui.QLabel() 
        self.workpace.setText(_translate("AdminWindow", "Répertoire de travail", None))
        
        self.vbox_workspace = QtGui.QVBoxLayout()
        self.vbox_workspace.addWidget(self.workpace)
        self.vbox_workspace.addLayout(self.hbox_workspace)
        self.vbox_workspace.setContentsMargins(0, 0, 0, 10)
        
        ###Partie centrale de la fenêtre###
        self.apec = QtGui.QLabel() 
        self.apec.setText(_translate("AdminWindow", "Identifiants APEC", None))
        
        
        #######################
        self.login = QtGui.QLabel() 
        self.login.setText(_translate("AdminWindow", "E-mail/Identifiant", None))
         
        self.champ_login = QtGui.QLineEdit(self.centralwidget)
         
        self.hbox_login = QtGui.QHBoxLayout()
        self.hbox_login.addWidget(self.login)
        self.hbox_login.addWidget(self.champ_login)
         
        ##################
        self.password = QtGui.QLabel() 
        self.password.setText(_translate("AdminWindow", "Mot de passe", None))
         
        self.champ_password = QtGui.QLineEdit(self.centralwidget)
         
        self.hbox_password = QtGui.QHBoxLayout()
        self.hbox_password.addWidget(self.password)
        self.hbox_password.addWidget(self.champ_password)
         
        ##################
        self.vbox_identifiants = QtGui.QVBoxLayout()
        self.vbox_identifiants.addWidget(self.apec)
        self.vbox_identifiants.addLayout(self.hbox_login)
        self.vbox_identifiants.addLayout(self.hbox_password)
         
        ##################
         
         
        ###Partie basse de la fenêtre### 
        self.bouton_ok = QtGui.QPushButton() 
        self.bouton_ok.setText(_translate("AdminWindow", "OK", None))
        self.bouton_ok.clicked.connect(self.save)
        #self.button_ok.accepted.connect(self.save)
        
        self.bouton_cancel = QtGui.QPushButton()
        self.bouton_cancel.setText(_translate("AdminWindow", "Annuler", None))
        self.bouton_cancel.clicked.connect(self.close)
        
        self.hbox_boutons = QtGui.QHBoxLayout()
        self.hbox_boutons.addWidget(self.bouton_ok)
        self.hbox_boutons.addWidget(self.bouton_cancel)  
        
        ###Ajout à la fenêtre principale### 
        
        self.qbox.addLayout(self.vbox_workspace)
        self.qbox.addLayout(self.vbox_identifiants)
        self.qbox.addLayout(self.hbox_boutons)
        
        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Administration", None))
        
    def save(self):    
        toolbox.writeconfigvalue("APEC", "login", self.champ_login.text())
        toolbox.writeconfigvalue("APEC", "password", self.champ_password.text())
        toolbox.writeconfigvalue("GENERALPARAMETERS", "dbfile", self.chemin.text())
        
        self.close()
    #######################  
 

class AdminWindowGUI(QtGui.QMainWindow, AdminWindowUI):
    def __init__(self, parent=None):
        super(AdminWindowGUI, self).__init__(parent)
        self.setupUi(self)
        
        self.chemin.setText(toolbox.getconfigvalue("GENERALPARAMETERS", "dbfile"))
        self.champ_login.setText(toolbox.getconfigvalue("APEC", "login"))
        self.champ_password.setText(toolbox.getconfigvalue("APEC", "password"))

### End of classes ###

### Main program ###

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = AdminWindowGUI()
    myapp.show()
    app.exec_()

### End of Main program ###


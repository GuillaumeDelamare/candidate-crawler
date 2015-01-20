# -*- coding: utf-8 -*-

'''
Created on 8 janv. 2015

@author: Julie S
'''

### External modules importation ###

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QSizePolicy, QBoxLayout, QGroupBox, QGridLayout
from candidatecrawler.core import toolbox
import os

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
        self.boutton_parcourir.clicked.connect(lambda : self.open_file())
        
        self.chemin = QtGui.QLineEdit(self.centralwidget)
        
        self.hbox_workspace = QtGui.QHBoxLayout()
        self.hbox_workspace.addWidget(self.chemin)
        self.hbox_workspace.addWidget(self.boutton_parcourir)
        
        self.groupBox_workspace = QGroupBox(_translate("AdminWindow", "Répertoire de travail", None))
        self.groupBox_workspace.setLayout(self.hbox_workspace)
        
        ###Partie centrale de la fenêtre###
        self.login = QtGui.QLabel() 
        self.login.setText(_translate("AdminWindow", "E-mail/Identifiant", None))
         
        self.champ_login = QtGui.QLineEdit(self.centralwidget)
                  
        self.password = QtGui.QLabel() 
        self.password.setText(_translate("AdminWindow", "Mot de passe", None))
         
        self.champ_password = QtGui.QLineEdit(self.centralwidget)
           
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.login, 0, 0)
        self.grid.addWidget(self.champ_login, 0, 1)
        self.grid.addWidget(self.password, 1, 0)
        self.grid.addWidget(self.champ_password, 1, 1)
        
        self.groupBox_identifiants = QGroupBox(_translate("AdminWindow", "Identifiants APEC", None))
        self.groupBox_identifiants.setLayout(self.grid)
        
         
        ###Partie basse de la fenêtre### 
        self.bouton_ok = QtGui.QPushButton() 
        self.bouton_ok.setText(_translate("AdminWindow", "OK", None))
        self.bouton_ok.clicked.connect(self.save)
        
        self.bouton_cancel = QtGui.QPushButton()
        self.bouton_cancel.setText(_translate("AdminWindow", "Annuler", None))
        self.bouton_cancel.clicked.connect(self.close)
        
        self.hbox_boutons = QtGui.QHBoxLayout()
        self.hbox_boutons.addWidget(self.bouton_ok)
        self.hbox_boutons.addWidget(self.bouton_cancel)  
        
        self.groupBox_boutons = QGroupBox()
        self.groupBox_boutons.setLayout(self.hbox_boutons)
        
        
        ###Ajout à la fenêtre principale### 
        self.qbox.addWidget(self.groupBox_workspace)
        self.qbox.addWidget(self.groupBox_identifiants)
        self.qbox.addWidget(self.groupBox_boutons)
        
        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def open_file(self):
        """Method to open directory.
           Use lambda function on browse button to know which entry has to be used"""
        path = str(self.chemin.text())
        initpath = os.path.dirname(path)
        #askedfile = QtGui.QFileDialog.getOpenFileName(self, 'Choisissez un fichier CSV', initpath,("Fichier CSV (*.csv*)"))
        askedfile = QtGui.QFileDialog.getExistingDirectory(self, u"Choisissez un répertoire de téléchargement",initpath)
        
        self.chemin.clear()
        self.chemin.setText(askedfile)

        if self.chemin.text() == "":
            self.chemin.setText(path)
            
    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Administration", None))
        
    def save(self):    
        toolbox.writeconfigvalue("APEC", "login", self.champ_login.text())
        toolbox.writeconfigvalue("APEC", "password", self.champ_password.text())
        toolbox.writeconfigvalue("GENERALPARAMETERS", "dbfile", self.chemin.text())
        self.close()
      
 

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


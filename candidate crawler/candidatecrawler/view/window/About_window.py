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

class AboutWindowUI(object):
    def setupUi(self, AboutWindow):
        """GUI building for About window"""
        AboutWindow.resize(300, 200)
        #AboutWindow.setLayout(QBoxLayout(QBoxLayout.TopToBottom, None))
        AboutWindow.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        AboutWindow.setMinimumSize(QtCore.QSize(300, 200))
        AboutWindow.setMaximumSize(QtCore.QSize(300, 200))
        self.centralwidget = QtGui.QWidget(AboutWindow)
        self.qbox = QBoxLayout(QBoxLayout.TopToBottom, self.centralwidget)
        self.centralwidget.setLayout(self.qbox)
        
        
        ### Partie haute de la fenêtre###
        self.boutton_parcourir = QtGui.QPushButton()
        self.boutton_parcourir.setText(_translate("AboutWindow", "Parcourir", None))
        
        self.chemin = QtGui.QLineEdit(self.centralwidget)
        
        self.hbox_workspace = QtGui.QHBoxLayout()
        self.hbox_workspace.addWidget(self.chemin)
        self.hbox_workspace.addWidget(self.boutton_parcourir)
        
        self.workpace = QtGui.QLabel() 
        self.workpace.setText(_translate("AboutWindow", "Répertoire de travail", None))
        
        self.vbox_workspace = QtGui.QVBoxLayout()
        self.vbox_workspace.addWidget(self.workpace)
        self.vbox_workspace.addLayout(self.hbox_workspace)
        
        
        ###Partie centrale de la fenêtre###
        self.apec = QtGui.QLabel() 
        self.apec.setText(_translate("AboutWindow", "Identifiants APEC", None))
        
        
        #######################
        self.login = QtGui.QLabel() 
        self.login.setText(_translate("AboutWindow", "E-mail/Identifiant", None))
         
        self.champ_login = QtGui.QLineEdit(self.centralwidget)
         
        self.hbox_login = QtGui.QHBoxLayout()
        self.hbox_login.addWidget(self.login)
        self.hbox_login.addWidget(self.champ_login)
         
        ##################
        self.password = QtGui.QLabel() 
        self.password.setText(_translate("AboutWindow", "Mot de passe", None))
         
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
        self.bouton_ok.setText(_translate("AboutWindow", "OK", None))
        self.bouton_ok.clicked.connect(self.save)
        #self.button_ok.accepted.connect(self.save)
        
        self.bouton_cancel = QtGui.QPushButton()
        self.bouton_cancel.setText(_translate("AboutWindow", "Annuler", None))
        self.bouton_cancel.clicked.connect(self.close)
        
        self.hbox_boutons = QtGui.QHBoxLayout()
        self.hbox_boutons.addWidget(self.bouton_ok)
        self.hbox_boutons.addWidget(self.bouton_cancel)  
        
        

        ###Ajout à la fenêtre principale### 
        
        self.qbox.addLayout(self.vbox_workspace)
        self.qbox.addLayout(self.vbox_identifiants)
        self.qbox.addLayout(self.hbox_boutons)
        
        
        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "Administration", None))
        
    def save(self):    
                
        write_dict = {}
        write_dict["login"] = self.champ_login.text()
        write_dict["password"] = self.champ_password.text()
        write_dict["dbfile"] = self.chemin.text()
        #write_dict["excludes"] = self.excludes_entry.text()
 
        toolbox.xml_writer("./config.ini", "", write_dict, backup=True)
 
        self.close()
 
        

    #######################  
 

class AboutWindowGUI(QtGui.QMainWindow, AboutWindowUI):
    def __init__(self, parent=None):
        super(AboutWindowGUI, self).__init__(parent)
        self.setupUi(self)

### End of classes ###

### Main program ###

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = AboutWindowGUI()
    myapp.show()
    app.exec_()

### End of Main program ###


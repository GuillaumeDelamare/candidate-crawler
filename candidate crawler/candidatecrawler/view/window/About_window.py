# -*- coding: utf-8 -*-

'''
Created on 8 janv. 2015

@author: Julie S
'''

### External modules importation ###

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QSizePolicy, QBoxLayout

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
        AboutWindow.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.centralwidget = QtGui.QWidget(AboutWindow)
        self.qbox = QBoxLayout(QBoxLayout.TopToBottom, self.centralwidget)
        self.centralwidget.setLayout(self.qbox)
        
        ###Titre###
        self.title = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        
        ###Description###
        self.description = QtGui.QLabel(self.centralwidget)
        self.description.setTextFormat(QtCore.Qt.RichText)
        self.description.setScaledContents(False)
        self.description.setWordWrap(True)
        
        ###Créateurs de l'application###
        self.creator = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.creator.setFont(font)
        self.creator.setAlignment(QtCore.Qt.AlignCenter)
        
        ###Ajout des composants à la fenêtre principale###
        self.qbox.addWidget(self.title)
        self.qbox.addWidget(self.description)
        self.qbox.addWidget(self.creator)
        
        AboutWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)


    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "A propos", None))
        self.title.setText(_translate("AboutWindow", "Candidate Crawler\n\n""Recherche ponctuelle\n", None))
        self.description.setText(_translate("AboutWindow", "<html><body><p align = justify>Ce programme parcours le site de l'APEC pour trouver les meilleurs CVs, à partir d'une liste de critères.</p><p align = justify>Une fois la recherche effectuée, l\'utilisateur télécharge un fichier Zip contenant un tableau Excel récapitulatif ainsi que les CVs trouvés.</p><p align = justify>Le programme exploite une base CSV pour stocker les CVs trouvés.</p></body></html>", None))
        self.creator.setText(_translate("AboutWindow", "<html><body><br>Application créée par Guillaume DELAMARE,</br><br>Jonathan SCHIEBEL, Julie SPENS,</br><br>Laura TAPIAS, Pierre THEILHARD</br></body><html>", None))

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


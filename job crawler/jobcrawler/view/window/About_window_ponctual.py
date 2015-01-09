# -*- coding: utf-8 -*-

###############################################
# Job Crawler - About                         #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

### External modules importation ###

import sys
from PyQt4 import QtCore, QtGui

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
        AboutWindow.setObjectName(_fromUtf8("AboutWindow"))
        AboutWindow.resize(275, 250)
        AboutWindow.setMinimumSize(QtCore.QSize(275, 250))
        AboutWindow.setMaximumSize(QtCore.QSize(275, 250))
        self.centralwidget = QtGui.QWidget(AboutWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.description = QtGui.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(10, 60, 251, 171))
        self.description.setTextFormat(QtCore.Qt.RichText)
        self.description.setScaledContents(False)
        self.description.setWordWrap(True)
        self.description.setObjectName(_fromUtf8("description"))
        self.creator = QtGui.QLabel(self.centralwidget)
        self.creator.setGeometry(QtCore.QRect(10, 220, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.creator.setFont(font)
        self.creator.setAlignment(QtCore.Qt.AlignCenter)
        self.creator.setObjectName(_fromUtf8("creator"))
        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "A propos", None))
        self.title.setText(_translate("AboutWindow", "Job Crawler\n"
"Recherche ponctuelle\n"
"A propos", None))
        self.description.setText(_translate("AboutWindow", "<html><head/><body><p>Ce programme parcours différent job boards pour trouver de nouvelles annonces, à partir de listes de critères ou de domaines, avec choix des jobs board à utiliser et de la région.</p><p>La recherche faite, l\'utilisateur peut ouvrir toutes les annonces dans son navigateur Internet et/ou se les faire envoyer par e-mail.</p><p>Le programme exploite une base CSV pour stoquer les annonces parcourues.</p></body></html>", None))
        self.creator.setText(_translate("AboutWindow", "Créé par RIVES Yann", None))

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
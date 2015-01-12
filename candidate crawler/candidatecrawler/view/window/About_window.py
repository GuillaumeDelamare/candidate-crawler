'''
Created on 8 janv. 2015

@author: Julie S
'''

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
        AboutWindow.resize(275, 240)
        AboutWindow.setMinimumSize(QtCore.QSize(275, 230))
        AboutWindow.setMaximumSize(QtCore.QSize(275, 240))
        self.centralwidget = QtGui.QWidget(AboutWindow)
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.description = QtGui.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(10, 40, 251, 171))
        self.description.setTextFormat(QtCore.Qt.RichText)
        self.description.setScaledContents(False)
        self.description.setWordWrap(True)
        self.creator = QtGui.QLabel(self.centralwidget)
        self.creator.setGeometry(QtCore.QRect(10, 214, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.creator.setFont(font)
        self.creator.setAlignment(QtCore.Qt.AlignCenter)
        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "A propos", None))
        self.title.setText(_translate("AboutWindow", "Candidate Crawler - A propos", None))
        self.description.setText(_translate("AboutWindow", "<html><head/><body><p>Ce programme parcours le site de l'APEC pour trouver les meilleurs CVs, à partir d'une liste de critères.</p><p></p><p>Une fois la recherche effectuée, l\'utilisateur télécharge un fichier Zip contenant un tableau Excel récapitulatif ainsi que les CVs trouvés.</p><p>Le programme exploite une base CSV pour stoquer les CVs trouvés.</p></body></html>", None))
        self.creator.setText(_translate("AboutWindow", "Créé par Jonathan SCHIEBEL, Julie SPENS, Laura TAPIAS, Pierre THEILHARD", None))

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

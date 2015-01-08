# -*- coding: utf-8 -*-

'''
Created on 7 janv. 2015

@author: Julie S
'''

### External modules importation ###

import sys
import webbrowser
from PyQt4 import QtCore, QtGui

### End of external modules importation ###

### Custom modules importation ###
from candidatecrawler.core import toolbox
from candidatecrawler.view.window import About_window_ponctual

#from CandidateCrawler.view.window import About_window_ponctual

### End of custom modules importation ###

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
class CandidateCrawlerUI(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(300, 560)
        MainWindow.setMinimumSize(QtCore.QSize(300, 560))
        MainWindow.setMaximumSize(QtCore.QSize(300, 560))
        self.centralwidget = QtGui.QWidget(MainWindow)
        
        self.keywords_label = QtGui.QLabel(self.centralwidget)
        self.keywords_label.setGeometry(QtCore.QRect(16, 10, 151, 20))
         
        self.keywords_entry = QtGui.QLineEdit(self.centralwidget)
        self.keywords_entry.setGeometry(QtCore.QRect(10, 30, 281, 20))
         
        self.region_label = QtGui.QLabel(self.centralwidget)
        self.region_label.setGeometry(QtCore.QRect(16, 65, 171, 20))
                
        self.region_combobox = QtGui.QComboBox(self.centralwidget)
        self.region_combobox.setGeometry(QtCore.QRect(10, 85, 181, 22))
          
        self.mobilite_label = QtGui.QLabel(self.centralwidget)
        self.mobilite_label.setGeometry(QtCore.QRect(16, 122, 171, 20))
                
        self.mobilite_combobox = QtGui.QComboBox(self.centralwidget)
        self.mobilite_combobox.setGeometry(QtCore.QRect(10, 142, 181, 22))
        
        self.salaire_label = QtGui.QLabel(self.centralwidget)
        self.salaire_label.setGeometry(QtCore.QRect(16, 179, 171, 20))
                
        self.salaire_combobox = QtGui.QComboBox(self.centralwidget)
        self.salaire_combobox.setGeometry(QtCore.QRect(10, 199, 181, 22))
        
        self.disponibilite_label = QtGui.QLabel(self.centralwidget)
        self.disponibilite_label.setGeometry(QtCore.QRect(16, 236, 171, 20))
                
        self.disponibilite_combobox = QtGui.QComboBox(self.centralwidget)
        self.disponibilite_combobox.setGeometry(QtCore.QRect(10, 256, 181, 22))
        
        self.cv_number_label = QtGui.QLabel(self.centralwidget)
        self.cv_number_label.setGeometry(QtCore.QRect(16, 293, 171, 20))
        
        self.cv_number_entry = QtGui.QLineEdit(self.centralwidget)
        self.cv_number_entry.setGeometry(QtCore.QRect(10, 313, 181, 20))
        self.cv_number_entry.setInputMethodHints(QtCore.Qt.ImhNone)
        self.cv_number_entry.setText("50")
                 
        self.progression_label = QtGui.QLabel(self.centralwidget)
        self.progression_label.setGeometry(QtCore.QRect(16, 348, 181, 20))
                    
        self.progression_text = QtGui.QTextBrowser(self.centralwidget)
        self.progression_text.setGeometry(QtCore.QRect(10, 368, 281, 111))
        
        self.run_button = QtGui.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(16, 494, 270, 23))
        
        
        self.job_boards_label = QtGui.QLabel(self.centralwidget)
        self.job_boards_label.setGeometry(QtCore.QRect(16, 10, 171, 16))
        
                
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuEdition = QtGui.QMenu(self.menubar)
        self.menuAide = QtGui.QMenu(self.menubar)
        
        MainWindow.setMenuBar(self.menubar)
        self.about_action = QtGui.QAction(MainWindow)
        self.exit_action = QtGui.QAction(MainWindow)
        self.reset_action = QtGui.QAction(MainWindow)
        self.menuFichier.addAction(self.exit_action)
        self.menuEdition.addAction(self.reset_action)
        self.menuAide.addAction(self.about_action)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuEdition.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Values for combobox
        staticsxmlfile = "statics.xml"

        region_list = tuple(toolbox.xml_reader(staticsxmlfile, "regions").split(','))
        mobilite_list = tuple(toolbox.xml_reader(staticsxmlfile, "regions").split(','))
        salaire_list = tuple(toolbox.xml_reader(staticsxmlfile, "salaire").split(','))
        disponibilite_list = tuple(toolbox.xml_reader(staticsxmlfile, "disponibilite").split(','))
         
        for element in region_list:
            self.region_combobox.addItem(element)

        for element in mobilite_list:
            self.mobilite_combobox.addItem(element)
        
        for element in salaire_list:
            self.salaire_combobox.addItem(element)
         
        for element in disponibilite_list:
            self.disponibilite_combobox.addItem(element)

        # Action attached to buttons
        self.about_action.triggered.connect(self.about_window)   #####################################
        self.exit_action.triggered.connect(self.close)
        self.reset_action.triggered.connect(self.reset)
        self.run_button.clicked.connect(self.run_program)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Candidate Crawler APEC", None))
        
        self.keywords_label.setText(_translate("MainWindow", "Mots-cls de recherche", None))
        
        self.cv_number_label.setText(_translate("MainWindow", "Nombre de CVs", None))
        
        self.run_button.setText(_translate("MainWindow", "Lancer la recherche", None))

        self.progression_label.setText(_translate("MainWindow", "Progression", None))
        
        self.region_label.setText(_translate("MainWindow", "Rgion", None))
         
        self.mobilite_label.setText(_translate("MainWindow", "Mobilité", None))
        
        self.salaire_label.setText(_translate("MainWindow", "Fourchette de salaire", None))
        
        self.disponibilite_label.setText(_translate("MainWindow", "Disponibilité", None)) 

        
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuEdition.setTitle(_translate("MainWindow", "Edition", None))
        self.menuAide.setTitle(_translate("MainWindow", "Aide", None))
        self.about_action.setText(_translate("MainWindow", "A propos", None))
        self.exit_action.setText(_translate("MainWindow", "Quitter", None))
        self.reset_action.setText(_translate("MainWindow", "Initialiser", None))


    # Methods for class CandidateCrawlerUI

    def about_window(self):
        """Method to generate About window"""
        self.aw = About_window_ponctual.AboutWindowGUI()
        self.aw.show()

    def reset(self):
        """Method to reset main window"""
        self.progression_text.clear()

    def close(self):
        """Method to close main window"""
        self.close()

    def _entries_retriever(self):
        """Method to get user entries"""
        self.keywords = tuple(self.keywords_entry.text().split(','))
        self.region = self.region_combobox.currentText()
        self.ml = tuple(self.cv_number_entry.text().split(','))

    def _entries_checker(self):
        """Method to check user entries"""
        error_code = False
        error_list = []

        if self.keywords[0] == "":
            error_code = True
            error_list.append("Veuillez entrer des mots-clé")

        if self.queries[0] == "":
            error_code = True
            error_list.append("Veuillez entrer des critères de filtrage")

        if self.ml[0] != "":
            for element in self.ml:
                if not "@" in element:
                    error_code = True
                    error_list.append("Une adresse e-mail semble mal formattée")

        return error_code, error_list

    def _open_in_browser(self):
        """Method to open all requested links in browser"""
        for link in self.new_links:
            webbrowser.open(link)

    def _change_open_button_status(self, status):
        """Method to change open button status"""
        self.open_in_browser_button.setEnabled(status)

    def run_program(self):
        """Method to run program on tab1: ponctual search"""
        self.progression_text.append("Lancement du programme")
        self.progression_text.append("Programme en cours ...")
        self._change_open_button_status(False)

        app.processEvents() # Window refresh

        try:
            self._entries_retriever()

            if self._entries_checker()[0]:
                self.progression_text.setTextColor(QtGui.QColor("red"))
                for element in self._entries_checker()[1]:
                    self.progression_text.append(element)
                self.progression_text.setTextColor(QtGui.QColor("black"))
                self.progression_text.append("Programme stoppé")

                return

           # runapp = core.CandidateCrawlerCore()
    
#             self.new_links = runapp.run_program(profile_name="Recherche ponctuelle", acc=self.ac, aefc=self.aefc, apecc=self.apecc,\
#                                                  caoec=self.caoec, ic=self.idc, mc=self.mc, poc=self.poc, rjc=self.rjc,\
#                                                  domain=self.domain, keywords=self.keywords, queries=self.queries, region=self.region,\
#                                                  daterange=self.daterange, cv_number=self.ml, db_management = "True")

            if len(self.new_links) > 50:
                self.progression_text.append("Trop d'annonces trouvées. Veuillez affiner vos critères")
                self.progression_text.append("Fin du programme\n")
            else:
                self.progression_text.append("{0} nouvelles annonces trouvées".format(len(self.new_links)))
                self.progression_text.append("Fin du programme\n")
                self._change_open_button_status(True)
        except:
            self.progression_text.append("Oups, quelque chose s'est mal passé")
            self.progression_text.append("Veuillez contacter l'admin")
            self.progression_text.append("Fin du programme\n")
            raise

class CandidateCrawlerGUI(QtGui.QMainWindow, CandidateCrawlerUI):
    def __init__(self, parent=None):
        super(CandidateCrawlerGUI, self).__init__(parent)
        self.setupUi(self)

### End of Classes ###

### Main program ###

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = CandidateCrawlerGUI()
    myapp.show()
    app.exec_()

### End of Main program ###

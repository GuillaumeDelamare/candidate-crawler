# -*- coding: utf-8 -*-

'''
Created on 7 janv. 2015

@author: Julie S
'''

### External modules importation ###

import sys
from PyQt4 import QtCore, QtGui

### End of external modules importation ###

### Custom modules importation ###
from candidatecrawler.core import core, toolbox
from candidatecrawler.view.window import About_window
from candidatecrawler.view.window import Admin_window
from PyQt4.QtGui import QIcon, QMessageBox, QStandardItemModel, QStandardItem, QBoxLayout
from PyQt4.QtCore import QSize, QVariant
from PyQt4.Qt import Qt


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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.qbox = QBoxLayout(QBoxLayout.TopToBottom, self.centralwidget)
        self.centralwidget.setLayout(self.qbox)
               
        #####Mots-clés###
        self.keywords_label = QtGui.QLabel(self.centralwidget)
        self.keywords_label.setText(_translate("AdminWindow", "Mots-clés de recherche", None))
         
        self.keywords_help = QtGui.QPushButton(self.centralwidget)
        self.keywords_help.setIcon(QIcon('./share/icon/point interrogation.png'))
        self.keywords_help.setIconSize(QSize(10,10))
        
        self.hbox_keywords = QtGui.QHBoxLayout()
        self.hbox_keywords.addWidget(self.keywords_label)
        self.hbox_keywords.addWidget(self.keywords_help)
        self.hbox_keywords.setContentsMargins(0, 0, 120, 0)
        
        self.keywords_entry = QtGui.QLineEdit(self.centralwidget)
        
        self.vbox_keywords = QtGui.QVBoxLayout()
        self.vbox_keywords.addLayout(self.hbox_keywords)
        self.vbox_keywords.addWidget(self.keywords_entry)
        self.vbox_keywords.setContentsMargins(0, 0, 0, 5) 
         
        ###Région### 
        self.region_label = QtGui.QLabel(self.centralwidget)
        self.region_label.setText(_translate("AdminWindow", "Région (5 choix maximum)", None))
                        
        self.region_list = QtGui.QListView(self.centralwidget)
               
        self.vbox_region = QtGui.QVBoxLayout()
        self.vbox_region.addWidget(self.region_label)
        self.vbox_region.addWidget(self.region_list)
        self.vbox_region.setContentsMargins(0, 0, 0, 5)
        
        ###Mobilité###
        self.mobilite_label = QtGui.QLabel(self.centralwidget)
        self.mobilite_label.setText(_translate("AdminWindow", "Mobilité", None))
                        
        self.mobilite_combobox = QtGui.QComboBox(self.centralwidget)
        
        self.vbox_mobilite = QtGui.QVBoxLayout()
        self.vbox_mobilite.addWidget(self.mobilite_label)
        self.vbox_mobilite.addWidget(self.mobilite_combobox)
        self.vbox_mobilite.setContentsMargins(0, 0, 0, 5)
        
        ###Salaire###
        self.salaire_label = QtGui.QLabel(self.centralwidget)
        self.salaire_label.setText(_translate("AdminWindow", "Salaire", None))
                
        self.salaire_combobox = QtGui.QComboBox(self.centralwidget)
        
        self.vbox_salaire = QtGui.QVBoxLayout()
        self.vbox_salaire.addWidget(self.salaire_label)
        self.vbox_salaire.addWidget(self.salaire_combobox)
        self.vbox_salaire.setContentsMargins(0, 0, 0, 5)
        
        ###Disponibilité###
        self.disponibilite_label = QtGui.QLabel(self.centralwidget)
        self.disponibilite_label.setText(_translate("AdminWindow", "Disponibilité", None))
                
        self.disponibilite_list = QtGui.QListView(self.centralwidget)
        
        self.vbox_disponibilite = QtGui.QVBoxLayout()
        self.vbox_disponibilite.addWidget(self.disponibilite_label)
        self.vbox_disponibilite.addWidget(self.disponibilite_list)
        self.vbox_disponibilite.setContentsMargins(0, 0, 0, 5)
        
        ###Fraîcheur###
        self.fraicheur_label = QtGui.QLabel(self.centralwidget)
        self.fraicheur_label.setText(_translate("AdminWindow", "Fraîcheur", None))
                
        self.fraicheur_combobox = QtGui.QComboBox(self.centralwidget)
        
        self.vbox_fraicheur = QtGui.QVBoxLayout()
        self.vbox_fraicheur.addWidget(self.fraicheur_label)
        self.vbox_fraicheur.addWidget(self.fraicheur_combobox)
        self.vbox_fraicheur.setContentsMargins(0, 0, 0, 5)
        
        ###Nombre de CVs###
        self.cv_number_label = QtGui.QLabel(self.centralwidget)
        self.cv_number_label.setText(_translate("AdminWindow", "Nombre de CV", None))
        
        self.cv_number_entry = QtGui.QLineEdit(self.centralwidget)
        self.cv_number_entry.setInputMethodHints(QtCore.Qt.ImhNone)
        self.cv_number_entry.setText("50")
        
        self.vbox_cv_number = QtGui.QVBoxLayout()
        self.vbox_cv_number.addWidget(self.cv_number_label)
        self.vbox_cv_number.addWidget(self.cv_number_entry)
        self.vbox_cv_number.setContentsMargins(0, 0, 0, 5)
            
        ###Progression###         
        self.progression_label = QtGui.QLabel(self.centralwidget)
        self.progression_label.setText(_translate("AdminWindow", "Progression", None))
                     
        self.progression_text = QtGui.QTextBrowser(self.centralwidget)
        
        self.vbox_progression = QtGui.QVBoxLayout()
        self.vbox_progression.addWidget(self.progression_label)
        self.vbox_progression.addWidget(self.progression_text)
        self.vbox_progression.setContentsMargins(0, 0, 0, 5)
        
        ###Bouton de lancement###
        self.run_button = QtGui.QPushButton(self.centralwidget)
        self.run_button.setText(_translate("AdminWindow", "Lancer la recherche", None))
        
        
        ###Ajout a la fenetre principale###
        
        self.qbox.addLayout(self.vbox_keywords)
        self.qbox.addLayout(self.vbox_region)
        self.qbox.addLayout(self.vbox_mobilite)
        self.qbox.addLayout(self.vbox_salaire)
        self.qbox.addLayout(self.vbox_disponibilite)
        self.qbox.addLayout(self.vbox_fraicheur)
        self.qbox.addLayout(self.vbox_cv_number)
        self.qbox.addLayout(self.vbox_progression)
        self.qbox.addWidget(self.run_button)
        
        MainWindow.setCentralWidget(self.centralwidget)

        
    ###Barre de menu###           
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuEdition = QtGui.QMenu(self.menubar)
        self.menuAide = QtGui.QMenu(self.menubar)
        
        MainWindow.setMenuBar(self.menubar)
        self.about_action = QtGui.QAction(MainWindow)
        self.admin_action = QtGui.QAction(MainWindow)
        self.exit_action = QtGui.QAction(MainWindow)
        self.menuFichier.addAction(self.admin_action)
        self.menuFichier.addAction(self.exit_action)
        self.menuAide.addAction(self.about_action)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())
        
     
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Values for combobox
        staticsxmlfile = "statics.xml"

        region_list = tuple(toolbox.xml_reader(staticsxmlfile, "regions").split(','))
        mobilite_list = tuple(toolbox.xml_reader(staticsxmlfile, "mobilite").split(','))
        salaire_list = tuple(toolbox.xml_reader(staticsxmlfile, "salaire").split(','))
        disponibilite_list = tuple(toolbox.xml_reader(staticsxmlfile, "disponibilite").split(','))
        fraicheur_list = tuple(toolbox.xml_reader(staticsxmlfile, "fraicheur").split(','))
         
        
        self.model = QStandardItemModel(self.region_list)
        for region in region_list:
            item = QStandardItem(region)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(QVariant(Qt.Unchecked), Qt.CheckStateRole)
            self.model.appendRow(item)
        self.region_list.setModel(self.model)

        self.model2 = QStandardItemModel(self.disponibilite_list)
        for disponibilite in disponibilite_list:
            item = QStandardItem(disponibilite)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(QVariant(Qt.Unchecked), Qt.CheckStateRole)
            self.model2.appendRow(item)
        self.disponibilite_list.setModel(self.model2)
         
        for element in mobilite_list:
            self.mobilite_combobox.addItem(element)
        
        for element in salaire_list:
            self.salaire_combobox.addItem(element)
         
        
        for element in fraicheur_list:
            self.fraicheur_combobox.addItem(element)
            
         

        # Action attached to buttons
        ####################################################################
        self.about_action.triggered.connect(self.about_window) 
        self.admin_action.triggered.connect(self.admin_window)  
        self.exit_action.triggered.connect(self.close)
        self.run_button.clicked.connect(self.run_program)
        self.keywords_help.clicked.connect(self.ouvrirDialogue)
        

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Candidate Crawler APEC", None))
        
        
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuAide.setTitle(_translate("MainWindow", "Aide", None))
        self.about_action.setText(_translate("MainWindow", "A propos", None))
        self.admin_action.setText(_translate("MainWindow", "Administration", None))
        self.exit_action.setText(_translate("MainWindow", "Quitter", None))
        

    # Methods for class CandidateCrawlerUI

    def about_window(self):
        """Method to generate About window"""
        self.about_w = About_window.AboutWindowGUI()
        self.about_w.show()
    
    def admin_window(self):
        """Method to generate About window"""
        self.admin_w = Admin_window.AdminWindowGUI()
        self.admin_w.show()
        
    def reset(self):
        """Method to reset main window"""
        self.progression_text.clear()

    def close(self):
        """Method to close main window"""
        self.close()
    
    def ouvrirDialogue(self):
        #TODO trUtf8 is deprecated
        QMessageBox.information(self, self.trUtf8("Aide mots-clés"),self.trUtf8("Vous pouvez entrer plusieurs mots-clés en les séparant par des espaces."))

    
    def _entries_retriever(self):
        """Method to get user entries"""
        self.keywords = self.trUtf8(self.keywords_entry.text())
    
        self.region = []
        for row in range(self.model.rowCount()):
            item = self.model.item(row)
            if item.checkState() == QtCore.Qt.Checked:
                self.region = [str(item.text())]+self.region
        
        self.mobilite = self.mobilite_combobox.currentText()
        self.salaire = self.salaire_combobox.currentText()
        
        self.disponibilite = []
        for row in range(self.model2.rowCount()):
            item = self.model2.item(row)
            if item.checkState() == QtCore.Qt.Checked:
                self.disponibilite = [str(item.text())]+self.disponibilite

        self.fraicheur = self.fraicheur_combobox.currentText()
        self.nombreCV = self.trUtf8(self.cv_number_entry.text())
        
    def _entries_checker(self):
        """Method to check user entries"""
        error_code = False
        error_list = []

        if self.keywords[0] == "":
            error_code = True
            error_list.append(_translate("MainWindow", "Veuillez entrer des mots-clés", None))

        if self.nombreCV[0] == "":
            error_code = True
            error_list.append(_translate("MainWindow", "Veuillez entrer un nombre de CVs", None))


        return error_code, error_list


    def run_program(self):
        """Method to run program on tab1: ponctual search"""
        self.progression_text.append("Lancement du programme")
        self.progression_text.append("Programme en cours ...")
        #self._change_open_button_status(False)

        app.processEvents() # Window refresh

        try:
            self._entries_retriever()

            if self._entries_checker()[0]:
                self.progression_text.setTextColor(QtGui.QColor("red"))
                for element in self._entries_checker()[1]:
                    self.progression_text.append(element)
                self.progression_text.setTextColor(QtGui.QColor("black"))
                self.progression_text.append(_translate("MainWindow", "Programme stoppé", None))

                return
            
            runapp = core.CandidateCrawlerCore(toolbox.getconfigvalue("APEC", "login"), toolbox.getconfigvalue("APEC", "password"),self.keywords, self.region
                                               , self.mobilite, self.salaire, self.disponibilite, self.fraicheur, self.nombreCV)
            print(self.keywords)
            print(self.region)
            print(self.mobilite)
            print(self.salaire)
            print(self.disponibilite)
            print(self.fraicheur)
            print(self.nombreCV)
            
            
            
            
            runapp.crawl()
#             self.new_links = runapp.run_program(profile_name="Recherche ponctuelle", acc=self.ac, aefc=self.aefc, apecc=self.apecc,\
#                                                 caoec=self.caoec, ic=self.idc, mc=self.mc, poc=self.poc, rjc=self.rjc,\
#                                                 domain=self.domain, keywords=self.keywords, region=self.region,\
#                                                 daterange=self.daterange, cv_number=self.ml, db_management = "True")
# 
#             if len(self.new_links) > 50:
#                 self.progression_text.append("Trop d'annonces trouvées. Veuillez affiner vos critères")
#                 self.progression_text.append("Fin du programme\n")
#             else:
#                 self.progression_text.append("{0} nouvelles annonces trouvées".format(len(self.new_links)))
#                 self.progression_text.append("Fin du programme\n")
#                 self._change_open_button_status(True)
        except:
            self.progression_text.append(self.trUtf8("Oups, quelque chose s'est mal passé"))
            self.progression_text.append(self.trUtf8("Veuillez vérifier les champs de l'adiministration"))
            self.progression_text.append(self.trUtf8("Fin du programme\n"))
            raise

class CandidateCrawlerGUI(QtGui.QMainWindow, CandidateCrawlerUI):
    def __init__(self, parent=None):
        super(CandidateCrawlerGUI, self).__init__(parent)
        self.setupUi(self)
        self.adjustSize()


### End of Classes ###

### Main program ###

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = CandidateCrawlerGUI()
    myapp.show()
    app.exec_()

### End of Main program ###

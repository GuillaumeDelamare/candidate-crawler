# -*- coding: utf-8 -*-

###############################################
# Job Crawler - QT GUI                        #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

### External modules importation ###

import sys
import webbrowser
from PyQt4 import QtCore, QtGui

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import core, toolbox
from jobcrawler.view.window import About_window_ponctual

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
class JobCrawlerUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(260, 640)
        MainWindow.setMinimumSize(QtCore.QSize(260, 640))
        MainWindow.setMaximumSize(QtCore.QSize(260, 640))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.regionjob_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.regionjob_checkbox.setGeometry(QtCore.QRect(120, 90, 131, 17))
        self.regionjob_checkbox.setChecked(True)
        self.regionjob_checkbox.setObjectName(_fromUtf8("regionjob_checkbox"))
        self.region_combobox = QtGui.QComboBox(self.centralwidget)
        self.region_combobox.setGeometry(QtCore.QRect(10, 290, 141, 22))
        self.region_combobox.setObjectName(_fromUtf8("region_combobox"))
        self.daterange_label = QtGui.QLabel(self.centralwidget)
        self.daterange_label.setGeometry(QtCore.QRect(16, 320, 141, 20))
        self.daterange_label.setObjectName(_fromUtf8("daterange_label"))
        self.mailing_list_label = QtGui.QLabel(self.centralwidget)
        self.mailing_list_label.setGeometry(QtCore.QRect(16, 370, 111, 20))
        self.mailing_list_label.setObjectName(_fromUtf8("mailing_list_label"))
        self.aeroemploiformation_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.aeroemploiformation_checkbox.setGeometry(QtCore.QRect(120, 30, 131, 17))
        self.aeroemploiformation_checkbox.setChecked(True)
        self.aeroemploiformation_checkbox.setObjectName(_fromUtf8("aeroemploiformation_checkbox"))
        self.domain_combobox = QtGui.QComboBox(self.centralwidget)
        self.domain_combobox.setGeometry(QtCore.QRect(10, 140, 141, 22))
        self.domain_combobox.setObjectName(_fromUtf8("domain_combobox"))
        self.run_button = QtGui.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(16, 560, 230, 23))
        self.run_button.setObjectName(_fromUtf8("run_button"))
        self.apec_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.apec_checkbox.setGeometry(QtCore.QRect(20, 50, 91, 17))
        self.apec_checkbox.setChecked(True)
        self.apec_checkbox.setObjectName(_fromUtf8("apec_checkbox"))
        self.daterange_spinbox = QtGui.QSpinBox(self.centralwidget)
        self.daterange_spinbox.setGeometry(QtCore.QRect(10, 340, 141, 22))
        self.daterange_spinbox.setMaximum(40)
        self.daterange_spinbox.setProperty("value", 3)
        self.daterange_spinbox.setObjectName(_fromUtf8("daterange_spinbox"))
        self.keywords_entry = QtGui.QLineEdit(self.centralwidget)
        self.keywords_entry.setGeometry(QtCore.QRect(10, 190, 241, 20))
        self.keywords_entry.setObjectName(_fromUtf8("keywords_entry"))
        self.queries_entry = QtGui.QLineEdit(self.centralwidget)
        self.queries_entry.setGeometry(QtCore.QRect(10, 240, 241, 20))
        self.queries_entry.setObjectName(_fromUtf8("queries_entry"))
        self.log_label = QtGui.QLabel(self.centralwidget)
        self.log_label.setGeometry(QtCore.QRect(16, 420, 141, 16))
        self.log_label.setObjectName(_fromUtf8("log_label"))
        self.region_label = QtGui.QLabel(self.centralwidget)
        self.region_label.setGeometry(QtCore.QRect(16, 270, 131, 20))
        self.region_label.setObjectName(_fromUtf8("region_label"))
        self.monster_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.monster_checkbox.setGeometry(QtCore.QRect(120, 70, 131, 17))
        self.monster_checkbox.setChecked(True)
        self.monster_checkbox.setObjectName(_fromUtf8("monster_checkbox"))
        self.caoemploi_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.caoemploi_checkbox.setGeometry(QtCore.QRect(120, 50, 131, 17))
        self.caoemploi_checkbox.setChecked(True)
        self.caoemploi_checkbox.setObjectName(_fromUtf8("caoemploi_checkbox"))
        self.poleemploi_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.poleemploi_checkbox.setGeometry(QtCore.QRect(20, 90, 91, 17))
        self.poleemploi_checkbox.setChecked(True)
        self.poleemploi_checkbox.setObjectName(_fromUtf8("poleemploi_checkbox"))
        self.aerocontact_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.aerocontact_checkbox.setGeometry(QtCore.QRect(20, 30, 91, 17))
        self.aerocontact_checkbox.setChecked(True)
        self.aerocontact_checkbox.setObjectName(_fromUtf8("aerocontact_checkbox"))
        self.queries_label = QtGui.QLabel(self.centralwidget)
        self.queries_label.setGeometry(QtCore.QRect(16, 220, 121, 20))
        self.queries_label.setObjectName(_fromUtf8("queries_label"))
        self.log_text = QtGui.QTextBrowser(self.centralwidget)
        self.log_text.setGeometry(QtCore.QRect(10, 440, 241, 111))
        self.log_text.setObjectName(_fromUtf8("log_text"))
        self.open_in_browser_button = QtGui.QPushButton(self.centralwidget)
        self.open_in_browser_button.setEnabled(False)
        self.open_in_browser_button.setGeometry(QtCore.QRect(16, 590, 230, 23))
        self.open_in_browser_button.setObjectName(_fromUtf8("open_in_browser_button"))
        self.domain_label = QtGui.QLabel(self.centralwidget)
        self.domain_label.setGeometry(QtCore.QRect(16, 120, 131, 20))
        self.domain_label.setObjectName(_fromUtf8("domain_label"))
        self.job_boards_label = QtGui.QLabel(self.centralwidget)
        self.job_boards_label.setGeometry(QtCore.QRect(16, 10, 131, 16))
        self.job_boards_label.setObjectName(_fromUtf8("job_boards_label"))
        self.keywords_label = QtGui.QLabel(self.centralwidget)
        self.keywords_label.setGeometry(QtCore.QRect(16, 170, 111, 20))
        self.keywords_label.setObjectName(_fromUtf8("keywords_label"))
        self.indeed_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.indeed_checkbox.setGeometry(QtCore.QRect(20, 70, 91, 17))
        self.indeed_checkbox.setChecked(True)
        self.indeed_checkbox.setObjectName(_fromUtf8("indeed_checkbox"))
        self.mailing_list_entry = QtGui.QLineEdit(self.centralwidget)
        self.mailing_list_entry.setGeometry(QtCore.QRect(10, 390, 241, 20))
        self.mailing_list_entry.setInputMethodHints(QtCore.Qt.ImhNone)
        self.mailing_list_entry.setObjectName(_fromUtf8("mailing_list_entry"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuProgramme = QtGui.QMenu(self.menubar)
        self.menuProgramme.setObjectName(_fromUtf8("menuProgramme"))
        self.menuEdition = QtGui.QMenu(self.menubar)
        self.menuEdition.setObjectName(_fromUtf8("menuEdition"))
        MainWindow.setMenuBar(self.menubar)
        self.about_action = QtGui.QAction(MainWindow)
        self.about_action.setObjectName(_fromUtf8("about_action"))
        self.exit_action = QtGui.QAction(MainWindow)
        self.exit_action.setObjectName(_fromUtf8("exit_action"))
        self.reset_action = QtGui.QAction(MainWindow)
        self.reset_action.setObjectName(_fromUtf8("reset_action"))
        self.menuProgramme.addAction(self.about_action)
        self.menuProgramme.addAction(self.exit_action)
        self.menuEdition.addAction(self.reset_action)
        self.menubar.addAction(self.menuProgramme.menuAction())
        self.menubar.addAction(self.menuEdition.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Values for combobox
        region_list = tuple(toolbox.getconfigvalue("STATIC", "regions").split(','))
        domain_list = tuple(toolbox.getconfigvalue("STATIC", "domains").split(','))

        for element in region_list:
            self.region_combobox.addItem(element)

        for element in domain_list:
            self.domain_combobox.addItem(element)

        # Action attached to buttons
        self.about_action.triggered.connect(self.about_window)
        self.exit_action.triggered.connect(self.close)
        self.reset_action.triggered.connect(self.reset)
        self.open_in_browser_button.clicked.connect(self._open_in_browser)
        self.run_button.clicked.connect(self.run_program)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Job crawler", None))
        self.regionjob_checkbox.setText(_translate("MainWindow", "Region job", None))
        self.daterange_label.setText(_translate("MainWindow", "Plage de recherche", None))
        self.mailing_list_label.setText(_translate("MainWindow", "Votre E-mail (Facultatif)", None))
        self.aeroemploiformation_checkbox.setText(_translate("MainWindow", "Aero emploi formation", None))
        self.run_button.setText(_translate("MainWindow", "Lancer la recherche", None))
        self.apec_checkbox.setText(_translate("MainWindow", "APEC", None))
        self.daterange_spinbox.setSuffix(_translate("MainWindow", " jours", None))
        self.log_label.setText(_translate("MainWindow", "Status", None))
        self.region_label.setText(_translate("MainWindow", "Région", None))
        self.monster_checkbox.setText(_translate("MainWindow", "Monster", None))
        self.caoemploi_checkbox.setText(_translate("MainWindow", "CAO emploi", None))
        self.poleemploi_checkbox.setText(_translate("MainWindow", "Pôle emploi", None))
        self.aerocontact_checkbox.setText(_translate("MainWindow", "Aerocontact", None))
        self.queries_label.setText(_translate("MainWindow", "Critères de filtrage", None))
        self.open_in_browser_button.setText(_translate("MainWindow", "Ouvrir les annonces", None))
        self.domain_label.setText(_translate("MainWindow", "Domaine", None))
        self.job_boards_label.setText(_translate("MainWindow", "Job boards", None))
        self.keywords_label.setText(_translate("MainWindow", "Mots-clé de recherche", None))
        self.indeed_checkbox.setText(_translate("MainWindow", "Indeed", None))
        self.menuProgramme.setTitle(_translate("MainWindow", "Programme", None))
        self.menuEdition.setTitle(_translate("MainWindow", "Edition", None))
        self.about_action.setText(_translate("MainWindow", "A propos", None))
        self.exit_action.setText(_translate("MainWindow", "Quitter", None))
        self.reset_action.setText(_translate("MainWindow", "Initialiser", None))

    # Methods for class JobCrawlerUI
    def about_window(self):
        """Method to generate About window"""
        self.aw = About_window_ponctual.AboutWindowGUI()
        self.aw.show()

    def reset(self):
        """Method to reset main window"""
        self.log_text.clear()

    def close(self):
        """Method to close main window"""
        self.close()

    def _entries_retriever(self):
        """Method to get user entries"""
        self.ac = self.aerocontact_checkbox.isChecked()
        self.aefc = self.aeroemploiformation_checkbox.isChecked()
        self.apecc = self.apec_checkbox.isChecked()
        self.caoec = self.caoemploi_checkbox.isChecked()
        self.idc = self.indeed_checkbox.isChecked()
        self.mc = self.monster_checkbox.isChecked()
        self.poc = self.poleemploi_checkbox.isChecked()
        self.rjc = self.regionjob_checkbox.isChecked()
        self.domain = str(self.domain_combobox.currentText())
        self.keywords = tuple(self.keywords_entry.text().split(','))
        self.queries = tuple(str(self.queries_entry.text()).split(','))
        self.region = str(self.region_combobox.currentText())
        self.daterange = self.daterange_spinbox.value()

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
        self.log_text.append("Lancement du programme")
        self.log_text.append("Programme en cours ...")
        self._change_open_button_status(False)

        app.processEvents() # Window refresh

        try:
            self._entries_retriever()

            if self._entries_checker()[0]:
                self.log_text.setTextColor(QtGui.QColor("red"))
                for element in self._entries_checker()[1]:
                    self.log_text.append(element)
                self.log_text.setTextColor(QtGui.QColor("black"))
                self.log_text.append("Programme stoppé")

                return
            
            dbfile = toolbox.getconfigvalue("GENERAL", "dbfile")
            exclude_list = toolbox.getconfigvalue("GENERAL", "excludes").split(',')
            runapp = core.JobCrawlerCore(dbfile, exclude_list)

            self.new_links = runapp.run_program(acc=self.ac, aefc=self.aefc, apecc=self.apecc, caoec=self.caoec, ic=self.idc, mc=self.mc, poc=self.poc, rjc=self.rjc, domain=self.domain, keywords=self.keywords, queries=self.queries, region=self.region, daterange=self.daterange, db_management = True)

            if len(self.new_links) > 50:
                self.log_text.append("Trop d'annonces trouvées. Veuillez affiner vos critères")
                self.log_text.append("Fin du programme\n")
            else:
                self.log_text.append("{0} nouvelles annonces trouvées".format(len(self.new_links)))
                self.log_text.append("Fin du programme\n")
                self._change_open_button_status(True)
        except:
            self.log_text.append("Oups, quelque chose s'est mal passé")
            self.log_text.append("Veuillez contacter l'admin")
            self.log_text.append("Fin du programme\n")
            raise

class JobCrawlerGUI(QtGui.QMainWindow, JobCrawlerUI):
    def __init__(self, parent=None):
        super(JobCrawlerGUI, self).__init__(parent)
        self.setupUi(self)

### End of Classes ###

### Main program ###

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = JobCrawlerGUI()
    myapp.show()
    app.exec_()

### End of Main program ###
# -*- coding: utf-8 -*-

###############################################
# Job Crawler - Edit window                   #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

### External modules importation ###

import sys
import os
from PyQt4 import QtCore, QtGui

### End of external modules importation ###

### End of external modules importation ###

from jobcrawler.core import toolbox, profilesmanagement

### Custom modules importation ###

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

class EditProfileWindowUI(object):
    def setupUi(self, EditProfileWindow):
        """GUI building for Edit window"""
        EditProfileWindow.setObjectName(_fromUtf8("EditProfileWindow"))
        EditProfileWindow.resize(251, 490)
        EditProfileWindow.setMinimumSize(QtCore.QSize(250, 490))
        EditProfileWindow.setMaximumSize(QtCore.QSize(260, 490))
        self.centralwidget = QtGui.QWidget(EditProfileWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.regionjob_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.regionjob_checkbox.setGeometry(QtCore.QRect(110, 130, 131, 17))
        self.regionjob_checkbox.setChecked(True)
        self.regionjob_checkbox.setObjectName(_fromUtf8("regionjob_checkbox"))
        self.job_boards_label = QtGui.QLabel(self.centralwidget)
        self.job_boards_label.setGeometry(QtCore.QRect(6, 50, 131, 16))
        self.job_boards_label.setObjectName(_fromUtf8("job_boards_label"))
        self.caoemploi_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.caoemploi_checkbox.setGeometry(QtCore.QRect(110, 90, 131, 17))
        self.caoemploi_checkbox.setChecked(True)
        self.caoemploi_checkbox.setObjectName(_fromUtf8("caoemploi_checkbox"))
        self.monster_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.monster_checkbox.setGeometry(QtCore.QRect(110, 110, 131, 17))
        self.monster_checkbox.setChecked(True)
        self.monster_checkbox.setObjectName(_fromUtf8("monster_checkbox"))
        self.region_label = QtGui.QLabel(self.centralwidget)
        self.region_label.setGeometry(QtCore.QRect(10, 310, 131, 20))
        self.region_label.setObjectName(_fromUtf8("region_label"))
        self.queries_entry = QtGui.QLineEdit(self.centralwidget)
        self.queries_entry.setGeometry(QtCore.QRect(4, 280, 241, 20))
        self.queries_entry.setObjectName(_fromUtf8("queries_entry"))
        self.aeroemploiformation_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.aeroemploiformation_checkbox.setGeometry(QtCore.QRect(110, 70, 131, 17))
        self.aeroemploiformation_checkbox.setChecked(True)
        self.aeroemploiformation_checkbox.setObjectName(_fromUtf8("aeroemploiformation_checkbox"))
        self.mailing_list_label = QtGui.QLabel(self.centralwidget)
        self.mailing_list_label.setGeometry(QtCore.QRect(10, 410, 111, 20))
        self.mailing_list_label.setObjectName(_fromUtf8("mailing_list_label"))
        self.queries_label = QtGui.QLabel(self.centralwidget)
        self.queries_label.setGeometry(QtCore.QRect(10, 260, 121, 20))
        self.queries_label.setObjectName(_fromUtf8("queries_label"))
        self.daterange_label = QtGui.QLabel(self.centralwidget)
        self.daterange_label.setGeometry(QtCore.QRect(10, 360, 141, 20))
        self.daterange_label.setObjectName(_fromUtf8("daterange_label"))
        self.indeed_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.indeed_checkbox.setGeometry(QtCore.QRect(10, 110, 91, 17))
        self.indeed_checkbox.setChecked(True)
        self.indeed_checkbox.setObjectName(_fromUtf8("indeed_checkbox"))
        self.aerocontact_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.aerocontact_checkbox.setGeometry(QtCore.QRect(10, 70, 91, 17))
        self.aerocontact_checkbox.setChecked(True)
        self.aerocontact_checkbox.setObjectName(_fromUtf8("aerocontact_checkbox"))
        self.domain_combobox = QtGui.QComboBox(self.centralwidget)
        self.domain_combobox.setGeometry(QtCore.QRect(4, 180, 141, 22))
        self.domain_combobox.setObjectName(_fromUtf8("domain_combobox"))
        self.region_combobox = QtGui.QComboBox(self.centralwidget)
        self.region_combobox.setGeometry(QtCore.QRect(4, 330, 141, 22))
        self.region_combobox.setObjectName(_fromUtf8("region_combobox"))
        self.domain_label = QtGui.QLabel(self.centralwidget)
        self.domain_label.setGeometry(QtCore.QRect(10, 160, 131, 20))
        self.domain_label.setObjectName(_fromUtf8("domain_label"))
        self.daterange_spinbox = QtGui.QSpinBox(self.centralwidget)
        self.daterange_spinbox.setGeometry(QtCore.QRect(4, 380, 141, 22))
        self.daterange_spinbox.setMaximum(40)
        self.daterange_spinbox.setProperty("value", 3)
        self.daterange_spinbox.setObjectName(_fromUtf8("daterange_spinbox"))
        self.mailing_list_entry = QtGui.QLineEdit(self.centralwidget)
        self.mailing_list_entry.setGeometry(QtCore.QRect(4, 430, 241, 20))
        self.mailing_list_entry.setObjectName(_fromUtf8("mailing_list_entry"))
        self.keywords_entry = QtGui.QLineEdit(self.centralwidget)
        self.keywords_entry.setGeometry(QtCore.QRect(4, 230, 241, 20))
        self.keywords_entry.setObjectName(_fromUtf8("keywords_entry"))
        self.apec_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.apec_checkbox.setGeometry(QtCore.QRect(10, 90, 91, 17))
        self.apec_checkbox.setChecked(True)
        self.apec_checkbox.setObjectName(_fromUtf8("apec_checkbox"))
        self.keywords_label = QtGui.QLabel(self.centralwidget)
        self.keywords_label.setGeometry(QtCore.QRect(10, 210, 111, 20))
        self.keywords_label.setObjectName(_fromUtf8("keywords_label"))
        self.poleemploi_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.poleemploi_checkbox.setGeometry(QtCore.QRect(10, 130, 91, 17))
        self.poleemploi_checkbox.setChecked(True)
        self.poleemploi_checkbox.setObjectName(_fromUtf8("poleemploi_checkbox"))
        self.buttonbox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonbox.setGeometry(QtCore.QRect(10, 460, 231, 23))
        self.buttonbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonbox.setCenterButtons(True)
        self.buttonbox.setObjectName(_fromUtf8("buttonbox"))
        self.title_label = QtGui.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        EditProfileWindow.setCentralWidget(self.centralwidget)
        self.about_action = QtGui.QAction(EditProfileWindow)
        self.about_action.setObjectName(_fromUtf8("about_action"))
        self.exit_action = QtGui.QAction(EditProfileWindow)
        self.exit_action.setObjectName(_fromUtf8("exit_action"))
        self.reset_action = QtGui.QAction(EditProfileWindow)
        self.reset_action.setObjectName(_fromUtf8("reset_action"))

        self.retranslateUi(EditProfileWindow)
        QtCore.QMetaObject.connectSlotsByName(EditProfileWindow)

        # Values for combobox
        staticsxmlfile = "statics.xml"

        region_list = tuple(toolbox.xml_reader(staticsxmlfile, "regions").split(','))
        domain_list = tuple(toolbox.xml_reader(staticsxmlfile, "domains").split(','))

        for element in region_list:
            self.region_combobox.addItem(element)

        for element in domain_list:
            self.domain_combobox.addItem(element)

        # Action attached to buttons
        self.buttonbox.accepted.connect(self.accept)
        self.buttonbox.rejected.connect(self.reject)

    def retranslateUi(self, EditProfileWindow):
        EditProfileWindow.setWindowTitle(_translate("EditProfileWindow", "Editeur de profil", None))
        self.regionjob_checkbox.setText(_translate("EditProfileWindow", "Region job", None))
        self.job_boards_label.setText(_translate("EditProfileWindow", "Job boards", None))
        self.caoemploi_checkbox.setText(_translate("EditProfileWindow", "CAO emploi", None))
        self.monster_checkbox.setText(_translate("EditProfileWindow", "Monster", None))
        self.region_label.setText(_translate("EditProfileWindow", "Région", None))
        self.aeroemploiformation_checkbox.setText(_translate("EditProfileWindow", "Aero emploi formation", None))
        self.mailing_list_label.setText(_translate("EditProfileWindow", "Liste de diffusion", None))
        self.queries_label.setText(_translate("EditProfileWindow", "Critères de filtrage", None))
        self.daterange_label.setText(_translate("EditProfileWindow", "Plage de recherche", None))
        self.indeed_checkbox.setText(_translate("EditProfileWindow", "Indeed", None))
        self.aerocontact_checkbox.setText(_translate("EditProfileWindow", "Aerocontact", None))
        self.domain_label.setText(_translate("EditProfileWindow", "Domaine", None))
        self.daterange_spinbox.setSuffix(_translate("EditProfileWindow", " jours", None))
        self.apec_checkbox.setText(_translate("EditProfileWindow", "APEC", None))
        self.keywords_label.setText(_translate("EditProfileWindow", "Mots-clé de recherche", None))
        self.poleemploi_checkbox.setText(_translate("EditProfileWindow", "Pôle emploi", None))
        self.title_label.setText(_translate("EditProfileWindow", "Job Crawler\n"
"Editeur de profil", None))
        self.about_action.setText(_translate("EditProfileWindow", "A propos", None))
        self.exit_action.setText(_translate("EditProfileWindow", "Quitter", None))
        self.reset_action.setText(_translate("EditProfileWindow", "Initialiser", None))

    # Methods for class EditProfileWindowUI
    def _entries_retriever(self):
        """Method to get user entries"""
        self.acc = self.aerocontact_checkbox.isChecked()
        self.aefc = self.aeroemploiformation_checkbox.isChecked()
        self.apecc = self.apec_checkbox.isChecked()
        self.caoec = self.caoemploi_checkbox.isChecked()
        self.idc = self.indeed_checkbox.isChecked()
        self.mc = self.monster_checkbox.isChecked()
        self.poc = self.poleemploi_checkbox.isChecked()
        self.rjc = self.regionjob_checkbox.isChecked()
        self.domain = self.domain_combobox.currentText()
        self.keywords = self.keywords_entry.text()
        self.queries = self.queries_entry.text()
        self.region = self.region_combobox.currentText()
        self.daterange = self.daterange_spinbox.value()
        self.ml = self.mailing_list_entry.text()

    def accept(self):
        """Method to save search profile and exit"""
        self._entries_retriever()

        profilesmanagement.edit_profile(self.input_file, self.acc, self.aefc, self.apecc,\
                                        self.caoec, self.idc, self.mc, self.poc,\
                                        self.rjc, self.domain, self.keywords,\
                                        self.queries, self.region, self.daterange, self.ml)

        self.close()

    def reject(self):
        """Method cancel and quit without saving"""
        self.close()

class EditProfileWindowGUI(QtGui.QMainWindow, EditProfileWindowUI):
    def __init__(self, parent=None, input_file=None ):
        super(EditProfileWindowGUI, self).__init__(parent)
        self.setupUi(self)
        self._values_initializer(input_file)

    def _values_initializer(self, input_file):
        self.input_file = input_file

        staticsxmlfile = "statics.xml"
        profilepath = toolbox.xml_reader(staticsxmlfile, "profilespath")

        os.chdir(profilepath)

        if toolbox.xml_reader(input_file, "aerocontact") == "False":
            self.aerocontact_checkbox.setChecked(False)
        if toolbox.xml_reader(input_file, "aeroemploiformation") == "False":
            self.aeroemploiformation_checkbox.setChecked(False)
        if toolbox.xml_reader(input_file, "apec") == "False":
            self.apec_checkbox.setChecked(False)
        if toolbox.xml_reader(input_file, "caoemploi") == "False":
            self.caoemploi_checkbox.setChecked(False)
        if toolbox.xml_reader(input_file, "indeed") == "False":
            self.indeed_checkbox.setChecked(False)
        if toolbox.xml_reader(input_file, "monster") == "False":
            self.monster_checkbox.setChecked(False)
        if toolbox.xml_reader(input_file, "poleemploi") == "False":
            self.poleemploi_checkbox.setChecked(False)
        if toolbox.xml_reader(input_file, "regionjob") == "False":
            self.regionjob_checkbox.setChecked(False)

        self.domain_combobox.setCurrentIndex(self.domain_combobox.findText(toolbox.xml_reader(input_file, "domain")))
        self.keywords_entry.setText(toolbox.xml_reader(input_file, "keywords"))
        self.queries_entry.setText(toolbox.xml_reader(input_file, "queries"))
        self.region_combobox.setCurrentIndex(self.region_combobox.findText(toolbox.xml_reader(input_file, "region")))
        self.daterange_spinbox.setProperty("value", toolbox.xml_reader(input_file, "daterange"))
        self.mailing_list_entry.setText(toolbox.xml_reader(input_file, "mailinglist"))

        os.chdir("../.")

### End of classes ###

### Main program ###

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = EditProfileWindowGUI()
    myapp.show()
    app.exec_()

### End of Main program ###

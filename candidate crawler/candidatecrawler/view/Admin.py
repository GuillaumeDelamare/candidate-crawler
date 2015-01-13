# -*- coding: utf-8 -*-

### External modules importation ###

import sys
import os
from PyQt4 import QtCore, QtGui

### End of external modules importation ###

### End of external modules importation ###

from candidatecrawler.core import toolbox #, profilesmanagement
from ConfigParser import ConfigParser
#from candidatecrawler.view.window import Edit_profile_window

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

class AdminWindowUI(object):
    def setupUi(self, AdminWindow):
        """GUI building for Admin window"""
        
        AdminWindow.resize(410, 500)
        AdminWindow.setMinimumSize(QtCore.QSize(410, 500))
        AdminWindow.setMaximumSize(QtCore.QSize(410, 500))
        self.centralwidget = QtGui.QWidget(AdminWindow)
        
        self.buttonbox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonbox.setGeometry(QtCore.QRect(10, 470, 391, 23))
        self.buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonbox.setCenterButtons(True)
        
        self.title_label = QtGui.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(5, 15, 401, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.db_label = QtGui.QLabel(self.centralwidget)
        self.db_label.setGeometry(QtCore.QRect(10, 90, 311, 20))
        self.db_entry = QtGui.QLineEdit(self.centralwidget)
        self.db_entry.setGeometry(QtCore.QRect(10, 110, 311, 20))
        self.db_browse_button = QtGui.QPushButton(self.centralwidget)
        self.db_browse_button.setGeometry(QtCore.QRect(330, 110, 75, 23))
        
        self.excludes_label = QtGui.QLabel(self.centralwidget)
        self.excludes_label.setGeometry(QtCore.QRect(10, 140, 311, 16))
        
        self.excludes_entry = QtGui.QLineEdit(self.centralwidget)
        self.excludes_entry.setGeometry(QtCore.QRect(10, 160, 391, 20))
        
        self.profiles_label = QtGui.QLabel(self.centralwidget)
        self.profiles_label.setGeometry(QtCore.QRect(10, 210, 311, 16))
        
        self.profile_treewidget = QtGui.QTreeWidget(self.centralwidget)
        self.profile_treewidget.setGeometry(QtCore.QRect(10, 230, 391, 181))
        self.profile_treewidget.setColumnCount(1)
       
        self.profile_treewidget.headerItem().setText(0, _fromUtf8("1"))
        self.profile_treewidget.header().setVisible(False)
        
        self.refresh_button = QtGui.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(10, 420, 391, 23))
        
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 190, 391, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 450, 391, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

        # Content for tree view
        headers = ("Sélection d'une recherche sauvegardée", "Editer", "Supprimer")
        self.profile_treewidget.setColumnCount(len(headers))
        self.profile_treewidget.setHeaderLabels(headers)

#         ## Add Items:
#         staticsxmlfile = "statics.xml"
#         profilepath = toolbox.xml_reader(staticsxmlfile, "profilespath")
# 
#         for name in os.listdir(profilepath):
#             CustomTreeItem(self.profile_treewidget, name)

        ## Set Columns Width to match content:
        for column in range(self.profile_treewidget.columnCount()):
            self.profile_treewidget.resizeColumnToContents(column)

#         # Action attached to buttons
        self.db_browse_button.clicked.connect(lambda: self.open_file("db"))
#         self.buttonbox.accepted.connect(self.accept)
#         self.buttonbox.rejected.connect(self.reject)
#         self.refresh_button.clicked.connect(self.refresh)

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Administration", None))
        self.title_label.setText(_translate("AdminWindow", "Candidate Crawler \n""Administration", None))
        self.db_label.setText(_translate("AdminWindow", "Base de donnée des liens", None))
        self.db_browse_button.setText(_translate("AdminWindow", "Parcourir", None))
        self.excludes_label.setText(_translate("AdminWindow", "Liste des critères d\'exclusion", None))
        self.profiles_label.setText(_translate("AdminWindow", "Sélection d'une recherche sauvegardée", None))
        self.refresh_button.setText(_translate("AdminWindow", "Rafraichir", None))

    # Methods for class AdminWindowUI

    def open_file(self,usedentry):
        """Method to open directory.
           Use lambda function on browse button to know which entry has to be used"""
        used_entry = eval("self."+ usedentry + "_entry")
        initfile = used_entry.text()
        initpath = os.path.dirname(initfile)
        askedfile = QtGui.QFileDialog.getOpenFileName(self, 'Choisissez un fichier CSV', initpath,("Fichier CSV (*.csv*)"))
        used_entry.clear()
        used_entry.setText(askedfile)
 
        if used_entry.text() == "":
            used_entry.setText(initfile)
 
    def accept(self):
        """Method to save configuration file and exit"""
        write_dict = {}
        write_dict["dbfile"] = self.db_entry.text()
        write_dict["excludes"] = self.excludes_entry.text()
 
        toolbox.xml_writer(self.configxmlfile, self.configxmltempfile, write_dict, backup=True)
 
        self.close()
 
    def reject(self):
        """Method cancel and quit without saving"""
        self.close()
    
#     def refresh(self):
#         """Method to refresh profiles window"""
#         self.profile_treewidget.clear()
#  
#         staticsxmlfile = "statics.xml"
#         profilepath = toolbox.xml_reader(staticsxmlfile, "profilespath")
#  
#         for name in os.listdir(profilepath):
#             CustomTreeItem(self.profile_treewidget, name)

class AdminWindowGUI(QtGui.QMainWindow, AdminWindowUI):
    def __init__(self, parent=None):
        super(AdminWindowGUI, self).__init__(parent)
        self.setupUi(self)
 
        self.configinifile = "./config.ini"
        self.configxmltempfile = "Job_crawler_Config_temp.xml"
# 
#         self.db_entry.setText(toolbox.xml_reader(self.configxmlfile, "dbfile"))
#         self.excludes_entry.setText(toolbox.xml_reader(self.configxmlfile, "excludes"))
        config = ConfigParser()
        config.read(self.configinifile)
        self.db_entry.setText(config.get("GENERALPARAMETERS", "dbfile"))

# class CustomTreeItem(QtGui.QTreeWidgetItem):
#     '''Custom QTreeWidgetItem with Widgets'''
# 
#     def __init__(self, parent, name):
#         '''parent (QTreeWidget) : Item's QTreeWidget parent.
#            name   (str)         : Item's name'''
# 
#         ## Init super class (QtGui.QTreeWidgetItem)
#         super(CustomTreeItem, self).__init__(parent)
#         self.profile_tree = parent
# 
#         ## Column 0 - Text:
#         self.setText(0, name)
# 
#         ## Column 1 - Edit:
#         self.edit_button = QtGui.QPushButton(parent)
#         self.edit_button.setText("Editer")
#         parent.setItemWidget(self, 1, self.edit_button)
# 
#         ## Column 2 - Delete:
#         self.delete_button = QtGui.QPushButton(parent)
#         self.delete_button.setText("Supprimer")
#         parent.setItemWidget(self, 2, self.delete_button)
# 
#         ## Signals
#         parent.connect(self.edit_button, QtCore.SIGNAL("clicked()"), self.editbuttonpressed)
#         parent.connect(self.delete_button, QtCore.SIGNAL("clicked()"), self.deletebuttonpressed)
# 
#     @property
#     def name(self):
#         """Return name"""
#         return self.text(0)

#     def refresh(self):
#         """Method to refresh profiles window"""
#         self.profile_tree.clear()
# 
#         staticsxmlfile = "statics.xml"
#         profilepath = toolbox.xml_reader(staticsxmlfile, "profilespath")
# 
#         for name in os.listdir(profilepath):
#             CustomTreeItem(self.profile_tree, name)
#
#     def editbuttonpressed(self):
#         """Triggered when Edit's button pressed"""
#         self.ew = Edit_profile_window.EditProfileWindowGUI(parent=None, input_file=self.name)
#         self.ew.show()

#     def deletebuttonpressed(self):
#         """Triggered when Delete's button pressed"""
# 
#         msgBox = QtGui.QMessageBox()
#         msgBox.setIcon(QtGui.QMessageBox.Question)
#         msgBox.setText("Voulez-vous supprimer {0} ?".format(self.name))
#         msgBox.addButton(QtGui.QPushButton("Oui"), QtGui.QMessageBox.YesRole)
#         msgBox.addButton(QtGui.QPushButton("Non"), QtGui.QMessageBox.NoRole)
#         msgBox.exec_()
# 
#         reply = msgBox.buttonRole(msgBox.clickedButton())
# 
#         if reply == QtGui.QMessageBox.YesRole:
#             profilesmanagement.delete_profile(self.name)
#         else:
#             print ("No")
# 
#         self.refresh()

### End of classes ###

### Main program ###

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = AdminWindowGUI()
    myapp.show()
    app.exec_()

### End of Main program ###

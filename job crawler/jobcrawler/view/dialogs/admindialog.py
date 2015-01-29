# -*- coding: utf8 -*-
'''
Created on 29 janv. 2015

@author: Guillaume
'''

import os
from PyQt4.QtGui import QDialog, QPushButton, QLineEdit, QGroupBox,QHBoxLayout,\
                        QVBoxLayout, QFileDialog
from PyQt4.QtCore import Qt, pyqtSlot
from jobcrawler.core import toolbox

class AdminDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        
        self._create_components()
        self._place_components()
        self._create_controller()
        self._load_data()
        
        self.setWindowTitle(u"Panneau d'administration")
        
    def _create_components(self):
        self.database_gb = QGroupBox(u"Base de donées")
        self.exclude_gb = QGroupBox(u"Liste des critères d'exclusion")
        
        self.database_le = QLineEdit()
        self.exclude_le = QLineEdit()
        
        self.database_button = QPushButton("Parcourir")
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Annuler")
    
    def _place_components(self):
        database_layout = QHBoxLayout()
        database_layout.addWidget(self.database_le)
        database_layout.addWidget(self.database_button)
        
        self.database_gb.setLayout(database_layout)
        
        excude_layout = QHBoxLayout()
        excude_layout.addWidget(self.exclude_le)
        
        self.exclude_gb.setLayout(excude_layout)
        
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.ok_button, 0, Qt.AlignCenter)
        control_layout.addWidget(self.cancel_button, 0, Qt.AlignCenter)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.database_gb)
        main_layout.addWidget(self.exclude_gb)
        main_layout.addSpacing(10)
        main_layout.addLayout(control_layout)
        
        self.setLayout(main_layout)
        
    def _create_controller(self):
        self.cancel_button.clicked.connect(self.close)
        self.ok_button.clicked.connect(self.ok)
        self.database_button.clicked.connect(self.browse)
        
    def _load_data(self):
        dbfile = toolbox.getconfigvalue("GENERAL", "dbfile")
        excludes = toolbox.getconfigvalue("GENERAL", "excludes")
        
        self.database_le.setText(dbfile)
        self.exclude_le.setText(excludes)
    
    @pyqtSlot()
    def ok(self):
        dbfile = self.database_le.text()
        excludes = self.exclude_le.text()
        
        toolbox.writeconfigvalue("GENERAL", "dbfile", dbfile)
        toolbox.writeconfigvalue("GENERAL", "excludes", excludes)
        
        self.close()
        
    @pyqtSlot()
    def browse(self):
        path = str(self.database_le.text())
        path = os.path.dirname(path)
        askedfile = QFileDialog.getOpenFileName(self, 'Choisissez un fichier CSV', path,("Fichier CSV (*.csv*)"))
        
        if askedfile != "":
            self.database_le.setText(askedfile)

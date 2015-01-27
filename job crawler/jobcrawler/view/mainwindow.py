# -*- coding: utf8 -*-
'''
Created on 26 janv. 2015

@author: Guillaume
'''
from PyQt4.QtGui import QMainWindow, QHBoxLayout, QWidget, QGroupBox, QVBoxLayout, QCheckBox,\
    QLabel, QLineEdit, QPushButton, QSpinBox, QComboBox, QTextEdit, QMenu,\
    QAction
from jobcrawler.core import toolbox
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot
from jobcrawler.core.core import core
import threading
from unidecode import unidecode

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self._create_components()
        self._place_components()
        self._create_controller()
        
        self.setWindowTitle("Job Crawler")
    
    def _create_components(self):
        self.site_gb = QGroupBox(u"Choix des sites")
        self.param_gb = QGroupBox(u"Autres Paramètres")
        self.search_gb = QGroupBox(u"Mots-clé")
        self.log_gb = QGroupBox(u"Logs")

        self.apec_cb = QCheckBox(u"APEC")
        self.apec_cb.setDisabled(True)
        self.caoe_cb = QCheckBox(u"CAO Emploi")
        self.caoe_cb.setDisabled(True)
        self.inde_cb = QCheckBox(u"Indeed")
        self.mons_cb = QCheckBox(u"Monster Job")
        self.mons_cb.setDisabled(True)
        self.pole_cb = QCheckBox(u"Pole Enmploi")
        self.pole_cb.setDisabled(True)
        self.regi_cb = QCheckBox(u"Région Job")
        self.regi_cb.setDisabled(True)
        
        self.search_label = QLabel(u"Mots-clé de recherche")
        self.filter_label = QLabel(u"Critère de filtrage")
        self.region_label = QLabel(u"Région")
        self.daterange_label = QLabel(u"Plage de recherche")
        
        self.search_qle = QLineEdit()
        self.filter_qle = QLineEdit()
        
        self.start_button = QPushButton(u"Rechercher")
        self.stop_button = QPushButton(u"Stopper")
        self.stop_button.setDisabled(True)
        
        self.daterange_sb = QSpinBox()
        self.daterange_sb.setMaximum(40)
        self.daterange_sb.setProperty("value", 3)
        self.daterange_sb.setSuffix(u" Jours")
        
        self.region_cb = QComboBox()
        region_list = toolbox.getconfigvalue("STATIC", "regions").split(',')
        self.region_cb.addItems(region_list)
        
        self.log_te = QTextEdit() 
        
        self.file_menu = QMenu(u"Fichier")
        self.help_menu = QMenu(u"Aide")
        
    
    def _place_components(self):
        site_layout = QHBoxLayout()
        temp = QVBoxLayout()
        temp.addWidget(self.apec_cb)
        temp.addWidget(self.caoe_cb)
        temp.addWidget(self.inde_cb)
        site_layout.addLayout(temp)
        temp = QVBoxLayout()
        temp.addWidget(self.mons_cb)
        temp.addWidget(self.pole_cb)
        temp.addWidget(self.regi_cb)
        site_layout.addLayout(temp)
        self.site_gb.setLayout(site_layout)
        
        search_layout = QVBoxLayout()
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_qle)
        search_layout.addWidget(self.filter_label)
        search_layout.addWidget(self.filter_qle)
        self.search_gb.setLayout(search_layout)
        
        param_layout = QVBoxLayout()
        param_layout.addWidget(self.daterange_label)
        param_layout.addWidget(self.daterange_sb)
        param_layout.addWidget(self.region_label)
        param_layout.addWidget(self.region_cb)
        self.param_gb.setLayout(param_layout)
        
        log_layout = QVBoxLayout()
        log_layout.addWidget(self.log_te)
        self.log_gb.setLayout(log_layout)
        
        command_layout = QHBoxLayout()
        command_layout.addWidget(self.start_button)
        command_layout.addWidget(self.stop_button)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.site_gb)
        main_layout.addWidget(self.search_gb)
        main_layout.addWidget(self.param_gb)
        main_layout.addWidget(self.log_gb)
        main_layout.addLayout(command_layout)
        
        centralwidget = QWidget(self)
        centralwidget.setLayout(main_layout)
        self.setCentralWidget(centralwidget)
        
        menubar = self.menuBar()
        menubar.addMenu(self.file_menu)
        menubar.addMenu(self.help_menu)
    
    def _create_controller(self):
        exitAction = QAction('Quitter', self)        
        exitAction.setStatusTip('Quitter Job Crawler')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        self.file_menu.addAction(exitAction)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
    
    
    @pyqtSlot()
    def start(self):
        def run():
            self.start_button.setDisabled(True)
            self.stop_button.setEnabled(True)
            
            inde = self.inde_cb.isChecked()
            apec = self.apec_cb.isChecked()
            caoe = self.caoe_cb.isChecked()
            mons = self.mons_cb.isChecked()
            pole = self.pole_cb.isChecked()
            regi = self.regi_cb.isChecked()
            
            searchkeyword = unidecode(unicode(self.search_qle.text())).split(",")
            filterkeyword = unidecode(unicode(self.filter_qle.text())).split(",")
            
            daterange = self.daterange_sb.value()
            region = str(self.region_cb.currentText())
            
            dbpath = toolbox.getconfigvalue("GENERAL", "dbfile")
            excludelist = unidecode(toolbox.getconfigvalue("GENERAL", "excludes")).split(",")
            
            c = core(dbpath)
            c.found_annonce(searchkeyword, daterange, region, None, apec, caoe, inde, mons, pole, regi)
            c.exclude_annouces(excludelist)
            c.filter_announces(filterkeyword)
            
            self.stop_button.setDisabled(True)
            self.start_button.setEnabled(True)
        
        self.thread = threading.Thread(target=run)
        self.thread.start()
        
    
    @pyqtSlot()
    def stop(self):
        self.stop_button.setDisabled(True)
        self.start_button.setEnabled(True)
        
    
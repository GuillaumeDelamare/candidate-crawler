# -*- coding: utf8 -*-
'''
Created on 29 janv. 2015

@author: Guillaume
'''
from PyQt4.QtGui import QDialog, QLabel, QVBoxLayout, QFont, QPushButton, QHBoxLayout
from PyQt4.QtCore import Qt

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        
        self._create_components()
        self._place_components()
        self._create_controller()
        
        self.setWindowTitle(u"A propos de Job Crawler")
    
    def _create_components(self):
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.title = QLabel(u"Job Crawler\nA propos")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(font)
        
        self.description = QLabel(u"<p>Ce programme parcours différent job boards pour trouver de nouvelles annonces, à partir de listes de critères ou de domaines, avec choix des jobs board à utiliser et de la région.</p>" \
                                  u"<p>La recherche faite, l\'utilisateur peut ouvrir toutes les annonces dans son navigateur Internet et/ou se les faire envoyer par e-mail.</p>" \
                                  u"<p>Le programme exploite une base CSV pour stoquer les annonces parcourues.</p>")
        self.description.setAlignment(Qt.AlignJustify)
        self.description.setTextFormat(Qt.RichText)
        self.description.setScaledContents(False)
        self.description.setWordWrap(True)
        
        font = QFont()
        font.setPointSize(10)
        
        self.creator = QLabel(u"Créé par RIVES Yann et DELAMARE Guillaume")
        self.creator.setAlignment(Qt.AlignCenter)
        self.creator.setFont(font)
        
        self.ok_button = QPushButton("OK")
    
    def _place_components(self):
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.ok_button)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title)
        main_layout.addWidget(self.description)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.creator)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.ok_button, 0, Qt.AlignCenter)
        
        self.setLayout(main_layout)
    
    def _create_controller(self):
        self.ok_button.clicked.connect(self.close)
        
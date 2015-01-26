# -*- coding: utf8 -*-
'''
Created on 26 janv. 2015

@author: Guillaume
'''
from PyQt4.QtGui import QMainWindow, QLabel, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._create_view()
    
    def _create_view(self):
        keywords_label = QLabel("Hello world")
        
        qbox = QHBoxLayout()
        qbox.addWidget(keywords_label)
        
        centralwidget = QWidget(self)
        centralwidget.setLayout(qbox)
        self.setCentralWidget(centralwidget)

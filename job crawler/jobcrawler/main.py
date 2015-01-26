'''
Created on 26 janv. 2015

@author: Guillaume
'''

import sys
from jobcrawler.view.mainwindow import MainWindow
from PyQt4.QtGui import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    app.exec_()
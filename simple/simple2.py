#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【记录】折腾Python的PyQt4模块
http://www.crifan.com/python_module_pyqt4
 
Author:     Crifan Li
Version:    2013-01-04
Contact:    admin at crifan dot com
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()
            
def pyqtDemoTooltip():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    pyqtDemoTooltip()

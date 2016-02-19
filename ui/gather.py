# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gather.ui'
#
# Created: Fri Feb  5 16:42:06 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_gatherer(object):
    def setupUi(self, gatherer):
        gatherer.setObjectName(_fromUtf8("gatherer"))
        gatherer.resize(611, 405)
        self.centralwidget = QtGui.QWidget(gatherer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout.addWidget(self.startButton)
        self.iterationBar = QtGui.QProgressBar(self.centralwidget)
        self.iterationBar.setProperty("value", 0)
        self.iterationBar.setObjectName(_fromUtf8("iterationBar"))
        self.horizontalLayout.addWidget(self.iterationBar)
        self.sitesBar = QtGui.QProgressBar(self.centralwidget)
        self.sitesBar.setProperty("value", 0)
        self.sitesBar.setObjectName(_fromUtf8("sitesBar"))
        self.horizontalLayout.addWidget(self.sitesBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        gatherer.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(gatherer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        gatherer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(gatherer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        gatherer.setStatusBar(self.statusbar)

        self.retranslateUi(gatherer)
        QtCore.QMetaObject.connectSlotsByName(gatherer)

    def retranslateUi(self, gatherer):
        gatherer.setWindowTitle(_translate("gatherer", "Zbieracz", None))
        self.startButton.setText(_translate("gatherer", "Start", None))

from PyQt4 import QtWebKit

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'httpWidget.ui'
#
# Created: Fri Feb  5 15:20:33 2016
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

class Ui_HttpWidget(object):
    def setupUi(self, HttpWidget):
        HttpWidget.setObjectName(_fromUtf8("HttpWidget"))
        HttpWidget.resize(1406, 689)
        self.horizontalLayoutWidget = QtGui.QWidget(HttpWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1371, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.back = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.back.setObjectName(_fromUtf8("back"))
        self.horizontalLayout.addWidget(self.back)
        self.next = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.next.setObjectName(_fromUtf8("next"))
        self.horizontalLayout.addWidget(self.next)
        self.stop = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.horizontalLayout.addWidget(self.stop)
        self.reload = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.reload.setObjectName(_fromUtf8("reload"))
        self.horizontalLayout.addWidget(self.reload)
        self.url = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.url.setObjectName(_fromUtf8("url"))
        self.horizontalLayout.addWidget(self.url)
        self.webView = QtWebKit.QWebView(HttpWidget)
        self.webView.setGeometry(QtCore.QRect(10, 30, 1381, 651))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))

        self.retranslateUi(HttpWidget)
        QtCore.QMetaObject.connectSlotsByName(HttpWidget)

    def retranslateUi(self, HttpWidget):
        HttpWidget.setWindowTitle(_translate("HttpWidget", "Form", None))
        self.back.setText(_translate("HttpWidget", "back", None))
        self.next.setText(_translate("HttpWidget", "next", None))
        self.stop.setText(_translate("HttpWidget", "stop", None))
        self.reload.setText(_translate("HttpWidget", "reload", None))

from PyQt4 import QtWebKit

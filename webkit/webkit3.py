# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtCore, QtGui, QtWebKit
from gather import Ui_gatherer

class GatherAds(QtGui.QMainWindow):
    def __init__(self, parent=None):
        print "__init__"
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_gatherer()
        self.ui.setupUi(self)
        self.refreshSite = 3

        self.currentIndex = 0
        self.currentRefresh = 0
        self.sites = [{'url': 'http://1.uqian.me/goods/newannounces', 'site': 'uqian.me'},
              {'url': 'http://news.sina.com.cn/c/nd/2016-02-05/doc-ifxpfhzk8966961.shtml', 'site': 'sina.com.cn/'},
                      {'url': 'http://m.gmw.cn/gallery/18808982.html', 'site': 'toutiao.com'},
                  ]

        s = self.ui.webView.settings()
        s.setAttribute(QtWebKit.QWebSettings.AutoLoadImages, False)
        s.setAttribute(QtWebKit.QWebSettings.JavascriptCanOpenWindows, False)
        s.setAttribute(QtWebKit.QWebSettings.PluginsEnabled, False)

        QtCore.QObject.connect(self.ui.startButton,QtCore.SIGNAL("clicked()"), self.start)
        QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("loadFinished (bool)"), self.loadFinished)
        QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("loadProgress (int)"), self.loadProgress)

    def start(self):
        print "start"
        self.ui.startButton.setEnabled(False)
        nexturl = self.__getNextUrl()
        if nexturl:
            self.ui.webView.load(nexturl)

    def loadFinished(self):
        print "load Finished"
        page = self.ui.webView.page()
        frame = page.currentFrame()
        content = frame.toHtml()
        print u'Page content, got %s bytes' % len(content)

        # process the data here

        if self.currentRefresh < self.refreshSite:
            print 'Refresh +1'
            self.currentRefresh += 1
        else:
            print 'Index +1'
            self.currentRefresh = 0
            self.currentIndex += 1

            nexturl = self.__getNextUrl()
            if nexturl:
                self.ui.webView.load(nexturl)

    def loadProgress(self, progress):
        print "load process..."
        print progress

    def __getNextUrl(self):
        print "__getNextUrl"
        # set the progress bar of pages loaded
        progress_value = (float(self.currentIndex)/float(len(self.sites)))*100
        self.ui.sitesBar.setValue(progress_value)

        # set the progress bar of refreshes
        progress_value = (float(self.currentRefresh)/float(self.refreshSite))*100
        self.ui.iterationBar.setValue(progress_value)

        if len(self.sites) - 1 >= self.currentIndex:
            newurl = QtCore.QUrl(self.sites[self.currentIndex]['url'])
        else:
            print 'No next url'
            newurl = False

        return newurl


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GatherAds()
    myapp.show()
    sys.exit(app.exec_())

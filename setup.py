from setuptools import setup

APP = ['simple1.py']
#OPTIONS = {'argv_emulation': True, 'includes': ['sip', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui'],'excludes': ['PyQt4.QtDesigner', 'PyQt4.QtNetwork', 'PyQt4.QtOpenGL', 'PyQt4.QtScript', 'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtWebKit', 'PyQt4.QtXml', 'PyQt4.phonon']}
OPTIONS = {'argv_emulation': True, 'includes': []}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

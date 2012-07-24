# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyovpn.ui'
#
# Created: Wed Jun 20 11:30:52 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ovpn(object):
    def setupUi(self, ovpn):
        ovpn.setObjectName("ovpn")
        ovpn.resize(219, 228)
        ovpn.setMinimumSize(QtCore.QSize(219, 228))
        ovpn.setMaximumSize(QtCore.QSize(219, 228))
        self.centralwidget = QtGui.QWidget(ovpn)
        self.centralwidget.setObjectName("centralwidget")
        self.confEdit = QtGui.QLineEdit(self.centralwidget)
        self.confEdit.setGeometry(QtCore.QRect(20, 30, 181, 27))
        self.confEdit.setObjectName("confEdit")
        self.ovpnpass_Edit = QtGui.QLineEdit(self.centralwidget)
        self.ovpnpass_Edit.setGeometry(QtCore.QRect(20, 130, 181, 27))
        self.ovpnpass_Edit.setEchoMode(QtGui.QLineEdit.Password)
        self.ovpnpass_Edit.setObjectName("ovpnpass_Edit")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 62, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 191, 17))
        self.label_2.setObjectName("label_2")
        self.startBtn = QtGui.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(20, 170, 181, 41))
        self.startBtn.setObjectName("startBtn")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 191, 17))
        self.label_3.setObjectName("label_3")
        self.localpass_Edit = QtGui.QLineEdit(self.centralwidget)
        self.localpass_Edit.setGeometry(QtCore.QRect(20, 80, 181, 27))
        self.localpass_Edit.setEchoMode(QtGui.QLineEdit.Password)
        self.localpass_Edit.setObjectName("localpass_Edit")
        ovpn.setCentralWidget(self.centralwidget)

        self.retranslateUi(ovpn)
        QtCore.QMetaObject.connectSlotsByName(ovpn)

    def retranslateUi(self, ovpn):
        ovpn.setWindowTitle(QtGui.QApplication.translate("ovpn", "OpenVPN Client", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ovpn", "Conf. file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ovpn", "Open VPN password", None, QtGui.QApplication.UnicodeUTF8))
        self.startBtn.setText(QtGui.QApplication.translate("ovpn", "Start Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ovpn", "Login Password", None, QtGui.QApplication.UnicodeUTF8))


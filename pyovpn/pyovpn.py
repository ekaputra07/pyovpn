#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  PyOvpn - Simple Python Open VPN Client
#  Copyright (C) 2012 Eka Putra - ekaputra@balitechy.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys, os
import pickle

from PyQt4 import QtGui, QtCore
from pyovpn_window import Ui_ovpn
from pyovpn_threads import ConnectOvpn

PYNOTIFY_INSTALLED = True
try:
    import pynotify
except:
    PYNOTIFY_INSTALLED = False


class Ovpn(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Ovpn, self).__init__(parent=None)
        self.ui = Ui_ovpn()
        self.ui.setupUi(self)
        
        # Check if Python-notify installed
        if not PYNOTIFY_INSTALLED:
            QtGui.QMessageBox.warning(self,
                            'Warning!',
                            'You need python-notify library to run this program, which is not installed on your system.\n\n To install use : "apt-get install python-notify" on debian based system.',
                            QtGui.QMessageBox.Ok)
            sys.exit(0)   

        self.config_file = os.path.expanduser('~/.pyovpn')
        
        QtCore.QObject.connect(self.ui.startBtn, QtCore.SIGNAL("clicked()"), self.startOvpn)
        
        # Get last saved data, if exist, fill the form
        data = self.read_config()
        if data:
            self.ui.confEdit.setText(data['conf'])
            self.ui.localpass_Edit.setText(data['password'])
            self.ui.ovpnpass_Edit.setText(data['ovpnpass'])

        # Connection Thread
        self.ovpn_thread = ConnectOvpn()
        self.ovpn_thread.is_loading_connected.connect(self.set_button_status)


    def save_config(self, conf, password, ovpnpassword):
        """ Saving configuration submitted by user """
        
        data = {'conf':conf, 'password': password, 'ovpnpass': ovpnpassword}
        try:
            conffile = open(self.config_file, 'wb')
            pickle.dump(data, conffile, 1)
        except:
            conffile.close()
            return False
        else:
            conffile.close()
            return True
    
    def read_config(self):
        """ Read last saved configuration file """
        
        data = {}
        if os.path.isfile(self.config_file):
            try:
                conffile = open(self.config_file, 'rb')
                data = pickle.load(conffile)
            except:
                conffile.close()
                QtGui.QMessageBox.warning(self,
                            'Warning!',
                            'Failed to read saved cofiguration file.\nlocation: '+self.config_file,
                            QtGui.QMessageBox.Ok)
            else:
                conffile.close()
        return data
            
    def startOvpn(self):
        """ Starting Openvpn connection """
        if self.ovpn_thread.connected:
            self.ovpn_thread.terminate_ovpn()
            return
        else:
            conf = self.ui.confEdit.text()
            password = self.ui.localpass_Edit.text()
            ovpnpassword = self.ui.ovpnpass_Edit.text()
            
            if not conf or not ovpnpassword or not password:
                QtGui.QMessageBox.warning(self,
                            'Warning!', 
                            'Configuration file and Password must provided.',
                            QtGui.QMessageBox.Ok)
                return
            try:
                self.save_config(conf, password, ovpnpassword)
            except:
                QtGui.QMessageBox.warning(self,
                            'Warning!',
                            'Failed saving configuration.' ,
                            QtGui.QMessageBox.Ok)
            else:
                self.ovpn_thread.set_connection(conf, password, ovpnpassword)
                self.ovpn_thread.start()
            return

    def set_button_status(self, is_loading, is_connected):
        """ Set button text based on connection status """

        if is_loading and not is_connected:
            self.ui.startBtn.setText('Connecting...')
        elif not is_loading and is_connected:
            self.ui.startBtn.setText('Disconnect!')
        else:
            self.ui.startBtn.setText('Start Connection')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ovpn = Ovpn()
    ovpn.show()
    sys.exit(app.exec_())

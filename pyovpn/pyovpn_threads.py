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

from PyQt4 import QtCore
import pexpect
import pynotify

class Notif(object):
    """ Notification Class """

    def show(self, title, message, timeout=None):
        """Create notification message"""
        self.n = pynotify.Notification(title, message, 'pyovpn')
        if timeout:
            self.n.set_timeout(timeout)
        self.n.show()   
    
    def close(self):
        self.n.close()    


class ConnectOvpn(QtCore.QThread):
    is_loading_connected = QtCore.pyqtSignal(bool, bool)
    connected = False

    def run(self):
        self.notif = Notif()

        self.is_loading_connected.emit(True, False)
        self.child = pexpect.spawn('sudo openvpn --config %s' % str(self.conf))

        i = self.child.expect([pexpect.TIMEOUT, 'password for'], timeout=1)
        if i == 1:
            self.child.sendline(self.password)

        i = self.child.expect([pexpect.TIMEOUT, 'Enter Private Key Password:'], timeout=1)
        if i == 1:
            self.notif.show('PyOvpn', 'Connecting to server. Please wait...')
            self.child.sendline(self.ovpnpassword)

        i = self.child.expect([pexpect.TIMEOUT, 'Initialization Sequence Completed'])
        if i == 0:
            self.notif.close()
            self.notif.show('PyOvpn', 'Failed connecting to server!')
            self.is_loading_connected.emit(False, False)
            self.connected = False
        elif i == 1:
            self.notif.close()
            self.notif.show('PyOvpn', 'Connection Established.') 
            self.is_loading_connected.emit(False, True)
            self.connected = True      

    def terminate_ovpn(self):
        self.notif.close()
        self.notif.show('PyOvpn', 'Disconnected from server.')

        if self.connected:
            self.child.sendintr()
            self.child.terminate()
            self.connected = False
            self.is_loading_connected.emit(False, False)
        return

    def set_connection(self, conf, password, ovpnpassword):
        self.conf = conf
        self.password = str(password)
        self.ovpnpassword = str(ovpnpassword)

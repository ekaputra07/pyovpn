#!/bin/bash

echo "Deleting all installed files..."
cat $HOME/.pyovpn.install.log | xargs rm -rf

echo "Deleting installer log file..."
rm $HOME/.pyovpn.install.log

echo "PyOvpn successfuly removed from system..."

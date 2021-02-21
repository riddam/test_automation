#!/bin/bash -xe
# download and install latest chromedriver for linux.
# required for selenium to drive a Chrome browser.

install_dir="/usr/local/bin"
# Shell script for debian platform
apt-get update
apt-get install -y unzip xvfb libxi6 libgconf-2-4
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip -O /tmp/chromedriver_linux64.zip
unzip /tmp/chromedriver_linux64.zip
mv /tmp/chromedriver /usr/bin/chromedriver
chown root:root /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver
exit 0

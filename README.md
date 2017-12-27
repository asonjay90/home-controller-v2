# home-controller-v2

##Steps to install dependencies:

###Setup libcec for HDMI Control:
```
wget http://packages.namniart.com/repos/namniart.key -O - | sudo apt-key add -
sudo sh -c 'echo "deb http://packages.namniart.com/repos/pi wheezy main" > /etc/apt/sources.list.d/libcec.list'
sudo apt-get update
sudo apt-get install python-dev build-essential libcec-dev cec-utils
```
###The Following packages are required:
```
pip install cec
pip install flask
pip install pychromecast
pip install phue
```

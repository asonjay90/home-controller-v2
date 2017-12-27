# home-controller-v2
Helps me to control many of my IOT devices in an awesome way.

## Steps to install dependencies:

### Setup libcec for HDMI Control:
```
wget http://packages.namniart.com/repos/namniart.key -O - | sudo apt-key add -
sudo sh -c 'echo "deb http://packages.namniart.com/repos/pi wheezy main" > /etc/apt/sources.list.d/libcec.list'
sudo apt-get update
sudo apt-get install python-dev build-essential libcec-dev cec-utils
```
### The Following packages are required:
```
pip install cec
pip install flask
pip install pychromecast
pip install phue
```
### Dont forget to setup the Flask App:
```
export FLASK_APP=[home-controller-root]/flask-app.py
```
### And then run it with:
```
python -m flask run --host=0.0.0.0
```

After opening port 5000, you should be able to setup IFTTT to control your stuff!

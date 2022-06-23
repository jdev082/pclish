# PCLISH - Python Command Line Shell
# Installation Script

sudo pip install pyinstaller
rm -rf /tmp/pclish
sudo rm -rf /usr/bin/pclish
sudo rm -rf /usr/bin/pclish_dir
git clone https://github.com/JaydenDev/pclish /tmp/pclish
pyinstaller /tmp/pclish/pclish.py
sudo mkdir /usr/bin/pclish_dir
sudo mv /tmp/pclish/dist/pclish/* /usr/bin/pclish_dir
sudo ln -sf /usr/bin/pclish_dir/pclish /usr/bin/pclish
sudo chmod +x /usr/bin/pclish




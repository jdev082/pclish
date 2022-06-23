# PCLISH - Python Command Line Shell
# Installation Script

pip install pyinstaller
rm -rf /tmp/pclish
git clone https://github.com/JaydenDev/pclish /tmp/pclish
python -m pyinstaller /tmp/pclish/pclish.py
sudo mkdir /usr/bin/pclish_dir
sudo mv /tmp/pclish/dist/pclish/* /usr/bin/pclish_dir
sudo ln -sf /usr/bin/pclish_dir/pclish /usr/bin/pclish
sudo chmod +x /usr/bin/pclish




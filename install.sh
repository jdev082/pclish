# PCLISH - Python Command Line Shell
# Installation Script

echo Cloning Repo to /tmp/pclish-installer/files
git clone https://tildegit.org/jaydenmw/pclish ~/.tmp/pclish-installer/files
rm ~/.tmp/pclish-installer/files/LICENSE
echo Installing...
mv /tmp/pclish-installer/files/* ~/.local/bin
echo Making shell executable
chmod +x ~/.local/bin/shell.py
echo Installation Complete




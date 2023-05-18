# PCLISH - Python Command Line Shell
# Installation Script

rm -rf $HOME/.local/bin/pclish_dir/
sudo pip install pyinstaller
rm -rf /tmp/pclish
sudo rm -rf $HOME/.local/bin/pclish
sudo rm -rf $HOME/.local/bin/pclish_dir
git clone https://github.com/JaydenDev/pclish /tmp/pclish
mkdir $HOME/.local/bin/pclish_dir
pyinstaller /tmp/pclish/pclish.py --distpath=/tmp/pclish_dir
echo "If you said yes to deleting the output directory, you must re-run the installer and say no."
mv /tmp/pclish_dir/pclish $HOME/.local/bin/pclish_dir
ln -sf $HOME/.local/bin/pclish_dir/pclish/pclish $HOME/.local/bin/pclish
chmod +x $HOME/.local/bin/pclish
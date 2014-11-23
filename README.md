
## Procedure
```bash
set -v
set -e
sudo apt-get install -y git
mkdir ~/src
(cd ~/src;
 git clone https://github.com/jayrambhia/Install-OpenCV.git;
 cd ./Install-OpenCV/Ubuntu/;
 sudo /bin/bash ./opencv_latest.sh) # slow
sudo apt-get install -y python-matplotlib
sudo apt-get install -y python-liblas
sudo apt-get install -y python-scipy
```


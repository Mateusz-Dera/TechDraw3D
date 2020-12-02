# Mateusz Dera
DIRECTORY="$(cd "$(dirname "$0")" && pwd -P)/$(basename "$1")"

#sudo docker run -it --rm -v $DIRECTORY:/root qnzhou/pymesh bash
sudo docker run -it --rm -v $DIRECTORY:/root qnzhou/pymesh python3 ./main.py

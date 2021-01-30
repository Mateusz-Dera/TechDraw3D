# TechDraw3D
# Copyright © 2020-2021 Tomasz Nowak, Mateusz Dera, Jakub Schwarz

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>


echo "Supported distros:"
echo "Ubuntu 20.04"
echo "Fedora 32"

if hash rpm 2>/dev/null; then
    echo "Installation type Fedora"
    sudo dnf install snapd blender python3 python3-pip
    sudo ln -s /var/lib/snapd/snap /snap
    sudo snap install docker
    sudo groupadd docker
    sudo usermod -aG docker $USER
elif hash apt 2>/dev/null; then
    echo "Installation type Ubuntu"
    sudo apt-get -y install blender python3 python3-pip docker-io
    sudo groupadd docker
    sudo usermod -aG docker $USER
else
    echo "Not supported distro"
    exit 1
fi

echo "Install python libs"
sudo python3 -m pip install -r ./requirements.txt

echo "Installation finished!"

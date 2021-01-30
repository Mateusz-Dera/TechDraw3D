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

DIRECTORY="$(cd "$(dirname "$0")" && pwd -P)/$(basename "$1")"

#sudo docker run -it --rm -v $DIRECTORY:/root qnzhou/pymesh bash
# echo $1
sudo docker run -it --rm -v $DIRECTORY:/root qnzhou/pymesh python3 ./main.py


blender -b --python "$(dirname $(readlink -f $0))/type.py" $1 $2 &

PID=$!
echo PID
tail --pid=$PID -f /dev/null

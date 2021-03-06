# TechDraw3D
# Copyright © 2020 Tomasz Nowak, Mateusz Dera, Jakub Schwarz

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

rm -r ./libs/mesher/extrude/tmp/*
rm -r ./libs/mesher/boolean/tmp/*
rm -r ./libs/mesher/boolean/export/*

if [[ ! -d ./libs/mesher/face/tmp ]] ; then
    mkdir ./libs/mesher/face/tmp
fi
if [[ ! -d ./libs/mesher/extrude/tmp ]] ; then
    mkdir ./libs/mesher/extrude/tmp
fi
if [[ ! -d ./libs/mesher/boolean/tmp ]] ; then
    mkdir ./libs/mesher/boolean/tmp
fi
if [[ ! -d ./libs/mesher/boolean/export ]] ; then
    mkdir ./libs/mesher/boolean/export
fi

blender -b --python "$(dirname $(readlink -f $0))/main.py"  &

PID=$!
echo PID
tail --pid=$PID -f /dev/null
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

import sys
import logging
import argparse
import textwrap

_logger = logging.getLogger(__name__)

# Tworzenie oraz konfiguracja parsera argumentów.
def make_parser():
    parser = argparse.ArgumentParser(prog = "TechDraw3D")
    parser.description = "Aplikacja przetwarzająca wybrane formaty rysunków technicznych do modelu 3D."
    parser.epilog = "Miłego korzystania. Autorzy: Tomasz Nowak, Mateusz Dera, Jakub Schwarz."
    

    parser.add_argument('-dwg2svg', '--dwg2svg', metavar="plik.dwg", help="Konwersja pliku DWG na SVG.", type=argparse.FileType('r'), required=False)
    parser.add_argument('-dwg2dxf', '--dwg2dxf', metavar="plik.dwg", help="Konwersja pliku DWG na DXF.", type=argparse.FileType('r'), required=False)
    parser.add_argument('-dxf2svg', '--dxf2svg', metavar="plik.dxf", help="Konwersja pliku DXF na SVG.", type=argparse.FileType('r'), required=False)
    parser.add_argument('-make_walls', '--make_walls', metavar="plik.svg", help="Rozbicie pliku SVG na ściany", type=argparse.FileType('r'), required=False)
    parser.add_argument('-viewobj', '--viewobj', metavar="plik.obj",help="Podgląd pliku OBJ.", type=argparse.FileType('r'), required=False)
    parser.add_argument('-makeobj', '--makeobj', help="Tworzenie obiektu 3D.", action='store_true', required=False)
    parser.add_argument('-do_all', '--do_all', metavar="plik.dwg", help="Tworzenie obiektu 3D z pliku DWG", type=argparse.FileType('r'), required=False)

    return parser
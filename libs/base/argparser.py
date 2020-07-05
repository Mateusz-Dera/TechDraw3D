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
    parser.add_argument('-viewobj', '--viewobj', metavar="plik.obj",help="Podgląd pliku OBJ.", type=argparse.FileType('r'), required=False)
    parser.add_argument('-makeobj', '--makeobj', help="Tworzenie obiektu 3D.", action='store_true', required=False)

    return parser
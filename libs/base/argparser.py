import sys
import logging
import argparse

_logger = logging.getLogger(__name__)

# Tworzenie oraz konfiguracja parsera argumentów.
def make_parser():
    parser = argparse.ArgumentParser(prog = "TechDraw3D")
    parser.description = "Aplikacja przetwarzająca wybrane formaty rysunków technicznych do modelu 3D."

    parser.add_argument('-dwg2svg', '--dwg2svg', help="Konwersja pliku DWG na SVG.", type=argparse.FileType('r'), required=False)
    parser.add_argument('-dwg2dxf', '--dwg2dxf', help="Konwersja pliku DWG na DXF.", type=argparse.FileType('r'), required=False)
    parser.add_argument('-viewobj', '--viewobj', help="Podgląd pliku OBJ.", type=argparse.FileType('r'), required=False)

    return parser
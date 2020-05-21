import sys
import logging
import argparse

_logger = logging.getLogger(__name__)

# Tworzenie oraz konfiguracja parsera argumentów.
def make_parser():
    parser = argparse.ArgumentParser(prog = "TechDraw3D")
    parser.description = "Aplikacja przetwarzająca wybrane formaty rysunków technicznych do modelu 3D."

    parser.add_argument('-f', '--file', help="DWG file", type=argparse.FileType('r'), required=True)

    return parser
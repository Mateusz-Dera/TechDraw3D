# Libs
from sys import platform
import logging
import runpy
import subprocess
import os.path

# My modules
from libs.extruder.svg import SVG
from libs.extruder.dwginput import DWGInput
from libs.extruder.dxfinput import DXFInput
from libs.base import logger, args, argparser
from libs.faceplacer.faceplacer_runner import run_faceplacer as rf

# CLI
from simple_term_menu import TerminalMenu
import time

def main():
    main_menu_title = "TechDraw3D\n"
    main_menu_items = ["Konwertuj DWG na inny format", "Konwertuj DWG na obiekt 3D", "O programie", "Wyjście"]
    main_menu_cursor = "< > "
    main_menu_cursor_style = ("fg_red", "bg_black")
    main_menu_style = ("bg_black", "fg_red", "bold")
    main_menu_exit = False

    main_menu = TerminalMenu(menu_entries=main_menu_items,
                             title=main_menu_title,
                             menu_cursor=main_menu_cursor,
                             menu_cursor_style=main_menu_cursor_style,
                             menu_highlight_style=main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    edit_menu_title = "Konwertuj DWG na ...\n"
    edit_menu_items = ["DXF", "SVG", "Powrót do menu głównego"]
    edit_menu_back = False
    edit_menu = TerminalMenu(edit_menu_items,
                             edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)
# /home/jschwarz/Projekty/Prywatne/TechDraw3D/assets/dwg/P001.dwg
# /home/jschwarz/Projekty/Prywatne/TechDraw3D/assets/dwg
    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            while not edit_menu_back:
                edit_sel = edit_menu.show()
                if edit_sel == 0:
                    print("Podaj lokalizacje pliku np.: /home/dummy_user/plik.dwg")
                    file = input("Lokalizacja: ")
                    
                    if os.path.isfile(file):
                        print("Konwertowanie na dxf")
                        dwg = DWGInput()
                        dwg.dwg2dxf_converter(file) 
                        print("Plik dostępny w katalogu: ")
                        print(file.replace("dwg", "dxf"))
                        time.sleep(5)
                    else: 
                        print("Błędna nazwa pliku!")
                        time.sleep(2)
                        # edit_menu_back = True
        
                elif edit_sel == 1:
                    print("Podaj lokalizacje pliku np.: /home/dummy_user/plik.dwg")
                    file = input("Lokalizacja: ")
                    
                    if os.path.isfile(file):
                        print("Konwertowanie na dxf")
                        dwg = DWGInput()
                        dxf = DXFInput()
                        dwg.dwg2dxf_converter(file)
                        dxf.dxf2svg_converter(file.replace("dwg", "dxf"))
                        print("Plik dostępny w katalogu: ")
                        print(file.replace("dwg", "svg"))
                        time.sleep(5)
                    else: 
                        print("Błędna nazwa pliku!")
                        time.sleep(2)
                elif edit_sel == 2:
                    edit_menu_back = True
                    print("Powrót do menu głównego")
            edit_menu_back = False
        elif main_sel == 1:
            print("Konwertuj DWG na plik 3D")
            print("Podaj lokalizacje pliku np.: /home/dummy_user/plik.dwg")
            file = input("Lokalizacja: ")
            
            if os.path.isfile(file):
                dwg = DWGInput()
                dxf = DXFInput()
                dwg.dwg2dxf_converter(file)
                dxf.dxf2svg_converter(file.replace("dwg", "dxf"))

                svg = SVG(file.replace("dxf", "svg"))
                svg.split_svg()
                svg.save_walls()

                rf()
                print("Plik dostępny w katalogu: ")
                print("./assets/obj/export/export.obj")
                time.sleep(5)
            else: 
                print("Błędna nazwa pliku!")
                time.sleep(2)

            time.sleep(5)
        elif main_sel == 2:
            print("O programie")
            time.sleep(5)
        elif main_sel == 3:
            main_menu_exit = True
            print("Dziękujemy za skorzystanie z programu TechDraw3D")


if __name__ == "__main__":
    main()
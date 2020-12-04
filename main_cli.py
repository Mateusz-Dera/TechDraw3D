# Libs
from sys import platform
import logging
import runpy
import subprocess
import os.path

# My modules
import pyvista

from libs.extruder.svg import SVG
from libs.extruder.dwginput import DWGInput
from libs.extruder.dxfinput import DXFInput
from libs.base import logger, args, argparser

# CLI
from simple_term_menu import TerminalMenu
import time

def main():
    main_menu_title = "TechDraw3D\n"
    main_menu_items = ["Konwerter formatów", "Konwertuj DWG na obiekt 3D", "O programie", "Wyjście"]
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

    edit_menu_title = "Konwertuj ...\n"
    edit_menu_items = ["DWG -> DXF", "DWG -> SVG", "DXF -> SVG", "Powrót do menu głównego"]
    edit_menu_back = False
    edit_menu = TerminalMenu(edit_menu_items,
                             edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    about_menu_title = "\n"
    about_menu_items = ["Powrót"]
    about_menu_back = False
    about_menu = TerminalMenu(about_menu_items,
                             about_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=False)
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
                        print("Konwertowanie DWG na DXF")
                        dwg = DWGInput()
                        dwg.dwg2dxf_converter(file) 
                        print("Plik dostępny w katalogu: ")
                        print(file.replace("dwg", "dxf"))
                        time.sleep(10)
                    else: 
                        print("Błędna nazwa pliku!")
                        time.sleep(2)
                        # edit_menu_back = True
        
                elif edit_sel == 1:
                    print("Podaj lokalizacje pliku np.: /home/dummy_user/plik.dwg")
                    file = input("Lokalizacja: ")
                    
                    if os.path.isfile(file):
                        print("Konwertowanie DWG na SVG")
                        dwg = DWGInput()
                        dxf = DXFInput()
                        dwg.dwg2dxf_converter(file)
                        dxf.dxf2svg_converter(file.replace("dwg", "dxf"))
                        print("Plik dostępny w katalogu: ")
                        print(file.replace("dwg", "svg"))
                        time.sleep(10)
                    else: 
                        print("Błędna nazwa pliku!")
                        time.sleep(2)
                elif edit_sel == 2:
                    print("Podaj lokalizacje pliku np.: /home/dummy_user/plik.dxf")
                    file = input("Lokalizacja: ")
                    
                    if os.path.isfile(file):
                        print("Konwertowanie DXF na SVG")

                        dxf = DXFInput()
                        dxf.dxf2svg_converter(file)

                        print("Plik dostępny w katalogu: ")
                        print(file.replace("dxf", "svg"))
                        time.sleep(10)
                    else: 
                        print("Błędna nazwa pliku!")
                        time.sleep(2)
                elif edit_sel == 3:
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
                
                svg = SVG(file.replace("dwg", "svg"))
                svg.split_svg()
                svg.save_walls()

                process = subprocess.Popen(['sh', "./libs/mesher/face/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate()

                process = subprocess.Popen(['sh', "./libs/mesher/extrude/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate()

                process = subprocess.Popen(['sh', "./libs/mesher/boolean/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate()

                print("Plik dostępny w katalogu: ")
                print("./libs/mesher/boolean/export/mesh.obj")
                mesh = pyvista.read(os.path.abspath("./libs/mesher/boolean/export/mesh.obj"))
                cpos = mesh.plot()
                time.sleep(5)
            else: 
                print("Błędna nazwa pliku!")
                time.sleep(2)

            time.sleep(5)
        elif main_sel == 2:
            while not about_menu_back:
                print(chr(27)+'[2j')
                print('\033c')
                print('\x1bc')
                
                print("""    TechDraw3D
    Wersja: 0.1

    Autorzy:
    Tomasz Nowak
    Mateusz Dera
    Jakub Schwarz

    2020""")
                about_sel = about_menu.show()
                if about_sel == 0:
                    about_menu_back = True
        elif main_sel == 3:
            main_menu_exit = True
            print("Dziękujemy za skorzystanie z programu TechDraw3D")


if __name__ == "__main__":
    main()
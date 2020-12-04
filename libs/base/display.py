import sys
import pyvista

if len(sys.argv) == 1:
    print("Brak argumentów. Podaj ścieżkę do pliku .obj.")
    exit(1)

mesh = pyvista.read(sys.argv[1])
cpos = mesh.plot()
import pyvista

mesh = pyvista.read("mesh.obj") 
cpos = mesh.plot()
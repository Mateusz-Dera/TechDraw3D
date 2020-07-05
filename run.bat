cd C:\TechDraw3D\
"C:\Program Files\Blender Foundation\Blender 2.82\blender.exe" -b --python part0.py
"C:\Program Files\Blender Foundation\Blender 2.82\blender.exe" -b --python part1.py
"C:\Program Files\Blender Foundation\Blender 2.82\blender.exe" -b --python part1.5.py
docker run -v "C:\TechDraw3D":/root -it pymesh/pymesh python -c "import os; os.system('python ./part2.py')"
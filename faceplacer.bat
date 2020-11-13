start /w /b "" "C:\Program Files\Blender Foundation\Blender 2.83\blender.exe" -b --python ./libs/faceplacer/part0.py
start /w /b "" "C:\Program Files\Blender Foundation\Blender 2.83\blender.exe" -b --python ./libs/faceplacer/part1.py
start /w /b "" "C:\Program Files\Blender Foundation\Blender 2.83\blender.exe" -b --python ./libs/faceplacer/part1.5.py
docker run -v %cd%:/root -it pymesh/pymesh python -c "import os; os.system('python ./libs/faceplacer/part2.py')"
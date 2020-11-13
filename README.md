# TechDraw3D
Aplikacja przetwarzająca wybrane formaty rysunków technicznych do modelu 3D oraz plików gotowych do użycia w maszynach CNC i drukarkach 3D.

 - ###### Autorzy
 Tomasz Nowak
 Mateusz Dera
 Jakub Schwarz
 - ###### Wersja
 0.1

## Wymagania
- python 3.7

## Instalacja
### Pierwsze kroki
Instalacja zaleśności wymaganych do zainstalowania i skompilowania bibliotek wymaganych przez program TechDraw3D: PyMesh i bpy

#####  Fedora
```shell
sudo dnf install eigen3-devel gmp-devel mpfr-devel boost-devel boost-thread tbb-devel cmake json-devel subversion libpng-devel
```
#####  Ubuntu
```shell
sudo apt install eigen3-devel gmp-devel mpfr-devel boost-devel boost-thread tbb-devel cmake json-devel subversion libpng-devel
```

### Repozytorium TechDraw
Należy sklonować repozytorium TechDraw do katalogu z którego ma być uruchamiany program.
```shell
git clone https://github.com/Mateusz-Dera/TechDraw3D.git
```

### Instalacja wymaganych bibliotek
1. Instalujemy wymagane biblioteki pythona z pliku requirements.txt
```shell
pip install -r requirements.txt
```
**Instalacja bibliotek może potrwać nawet około 30 minut z powodu instalacji biblioteki bpy**

2. Po instalacji bibliotek dla pythona wraz z biblioteką bpy, nastąpił czas na instalację biblioteki PyMesh, która wymaga ręcznej kompilacji.

	Tworzymy na dysku komputera katalog do którego sklonujemy repozytorium PyMesh
```shell
mkdir PyMesh
cd PyMesh
```
Następnie klonujemy repozytorium i wchodzimy do katalogu
```shell
git clone https://github.com/PyMesh/PyMesh.git
cd PyMesh/
```
Inicjujemy submoduły dla PyMesh
```shell
git submodule update --init
```

	Następnie eksportujemy zmienną środowiskową potrzebną do kompilacji PyMesh
```shell
export PYMESH_PATH=$(pwd)
```
Czas przystąpić do kompilacji. Poniższe dwa polecenia najpierw skompilują nam biblioteke PyMesh a następnie zainstalują ją w systemie.
```shell
./setup.py build
./setup.py install
```
**Czas kompilacji i instalacji biblioteki PyMesh może trwać nawet i 15-20 minut.**

## Uruchomienie
Program obecnie działa w trybie konsolowym. W celu uruchomienia programu wystarczy przejść do katalogu z naszym programem, a następnie z poziomu pythona uruchomić program np.:
```shell
python3 main_cli.py
```

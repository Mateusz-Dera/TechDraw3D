# Mateusz Dera

echo "Supported distros:"
echo "Ubuntu 20.04"
echo "Fedora 32"

if hash rpm 2>/dev/null; then
    echo "Installation type Fedora"
    sudo dnf install snapd blender python3 python3-pip
    sudo ln -s /var/lib/snapd/snap /snap
    sudo snap install docker
elif hash apt 2>/dev/null; then
    echo "Installation type Ubuntu"
    sudo apt-get -y install blender python3 python3-pip docker
else
    echo "Not supported distro"
    exit 1
fi

sudo python3 -m pip install pyvista simple-term-menu svgpathtools dxf2svg ezdxf

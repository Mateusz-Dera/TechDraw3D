# Mateusz Dera

echo "Supported distros:"
echo "Ubuntu 20.04"
echo "Fedora 32"

if hash rpm 2>/dev/null; then
    echo "Installation type Fedora"
    sudo dnf install snapd blender python3 python3-pip
    sudo ln -s /var/lib/snapd/snap /snap
elif hash apt 2>/dev/null; then
    echo "Installation type Ubuntu"
    sudo apt-get -y install snapd blender python3 python3-pip
else
    echo "Not supported distro"
    exit 1
fi

sudo snap install docker
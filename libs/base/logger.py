# TechDraw3D
# Copyright © 2020 Tomasz Nowak, Mateusz Dera, Jakub Schwarz

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from sys import platform
import logging
import os

def configure_logging(mode):

    # Wybór ścieżki w zależności od systemu.
    if platform == "win32":
        logpath = "logs/debug.log"
    
    if platform == "linux":
        logpath = "logs/debug.log"

    try:
        logging.basicConfig(level=mode,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M',
            filename=logpath,
            filemode='a')

    except FileNotFoundError as e:
        # Tworzenie folderu logs w sytuacji, gdyby został usunięty.
        if not os.path.isdir(logpath[:-10]):
            os.mkdir(logpath[:-10])

        open(logpath, 'a').close()

        logging.basicConfig(level=mode,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M',
            filename=logpath,
            filemode='a')

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(mode)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)



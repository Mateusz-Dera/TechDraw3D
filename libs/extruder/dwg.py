# TechDraw3D
# Copyright © 2020-2021 Tomasz Nowak, Mateusz Dera, Jakub Schwarz

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
from io import BytesIO

import logging


_logger = logging.getLogger(__name__)


class DWG():
    def __validate(self, file):
        try:
            open(file, "rb")
            return True
        except IOError:
            print ("Error: File does not appear to exist.")
        return False

    def __init__(self, dwg):
        if self.__validate(dwg):
            file = open(dwg, 'rb')
            self.dwg = BytesIO(file.read()).getvalue()
            
            _logger.debug("Create instance of DWG File")
        else:
            raise IOError("Error: File %s does not appear to exist." % dwg)

    def get_dwg(self):
        return self.dwg
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

import sys
import logging

_logger = logging.getLogger(__name__)

def paramArgsSimple():
    if len(sys.argv) > 1:
        _logger.info("Parse arguments: " +str(sys.argv))

        if str(sys.argv[1]) in ('INFO', 'info'):
            return 20
        if str(sys.argv[1]) in ('debug', 'DEBUG'):
            return 10
    return 20

def paramArgsAdvanced():
    pass
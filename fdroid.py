#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# fdroid.py - part of the FDroid server tools
# Copyright (C) 2010-12, Ciaran Gultnieks, ciaran@ciarang.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

commands = [
        "build",
        "update",
        "checkupdates",
        "import",
        "rewritemeta",
        "scanner",
        "statsupdate"]

def main():

    if len(sys.argv) <= 1:
        print "Specify a command. Valid commands are:"
        for command in commands:
            print "  " + command
        sys.exit(0)

    command = sys.argv[1]
    if not command in commands:
        print "Command '" + command + "' not recognised"
        sys.exit(1)

    # Trick optparse into displaying the right usage when --help is used.
    sys.argv[0] += ' ' + command

    del sys.argv[1]
    mod = __import__(command)
    mod.main()
    sys.exit(0)

if __name__ == "__main__":
    main()

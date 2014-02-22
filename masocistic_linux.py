#!/usr/bin/env python
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#################################################################################
# Originally written by  sangyye https://bitbucket.org/sangyye
# Modified    by         Silas Cutler
#
#################################################################################

import os
import sys

def write_bash(fname):
    bash = "\nfunction command_not_found_handle {\n\t/usr/games/sl\n}"
    with open( fname, "a") as data:
        print >> data, bash

def write_sudo(fname, user):
    sudo = user + "\t ALL=NOPASSWD: /usr/games/sl"
    with open( fname, "a") as data:
        print >> data, sudo

def test_system():
    if os.path.exists("/usr/bin/sudo") and os.path.exists("/etc/sudoers"):
        return 1
    else:
        return 0

def test_sl():
    if os.path.exists("/usr/games/sl"):
        return 1
    else:
        return 0

def warning():
    print "\t\tWARNING!"
    print "This script will not destroy your system, but "
    print "is likely to annoy the users."
    print "If you enter a command that is not known "
    print "by the bash it will execute /usr/games/sl"
    anwser = raw_input("Are your sure you want This?(Y/N) ")
    if anwser.lower() == 'y':
        return 1
    else:
        return 0

def shelp():
    print sys.argv[0] + " Options"
    print "Options:"
    print "\tinstall - install Masochistic Linux"
    print "\thelp - print this help"

def install_all():
    if not test_system():
        print "Something is wrong with your sudo install!"
        sys.exit(1)
    if not test_sl():
        print "sl is not under /usr/games"
        sys.exit(1)
    if warning():
        print "Which user do you want to change?: "
        i = 1
        users = os.listdir("/home")
        for user in users:
            print str(i) + ". " + user
            i += 1
        user_nr = int(raw_input("Nr.: "))
        write_bash("/home/" + users[user_nr - 1] + "/.bashrc")
        write_sudo("/etc/sudoers", users[user_nr -1])
        print "Now your system is Masochistic Linux please restart bash"
    else:
        print "Your system are save :-)"

def main():
    if os.geteuid() != 0:
        print "You must be root to run this script."
        sys.exit(1)
    if len(sys.argv) <= 1:
        print "Missing an argument"
        shelp()
    elif sys.argv[1] == "install":
        install_all()
    elif sys.argv[1] == "help":
        shelp()
    else:
        print "Command " + sys.argv[1] +" unknow"
        shelp()

if __name__ == '__main__':
    main()

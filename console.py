#!/usr/bin/python3
"""
contains the entry point of the command interpreter
command interpreter should implement:
    quit and EOF to exit the program
    help (this action is provided by default by cmd but you should
    keep it updated and documented as you work through tasks)
    a custom prompt: (hbnb)
    an empty line + ENTER shouldn’t execute anything
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    class definition
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        help for quit
        """
        print("Quit command to exit the program\n")
    """
    EOF
    """
    def do_EOF(self, line):
        """
        signifies end of Command line Interface
        """
        return True
    """
    remove implementation of cmd.emptyline
    """
    def emptyline(self):
        """
        returns False
        """
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()

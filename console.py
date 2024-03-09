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

from models.base_model import BaseModel
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
    """
    Creates a new instance of BaseModel
    saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
    If the class name is missing, print ** class name missing ** (ex: $ create)
    If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
    """
    def do_create(self):
        """
        Creates a new instance of BaseModel
        """
        if not BaseModel:
            print("** class name missing **")
        if BaseModel is None:
            print("print ** class doesn't exist **")

        my_inst = BaseModel()
        my_inst.save()
        print(my_inst.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

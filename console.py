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

import uuid
import shlex
import sys
from models import storage
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
    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            my_class = globals().get(class_name, None)
            if my_class is not None:
                my_inst = my_class()
                my_inst.save()
                print(my_inst.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234
        If the class name is missing, print ** class name missing ** (ex: $ show)
        If the class name doesn’t exist, print
        ** class doesn't exist ** (ex: $ show MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        ins_id = args[1]
        try:
            my_class = globals().get(class_name, None)
            if my_class is not None:
                my_inst = my_class()
                my_inst.id = ins_id
                if hasattr(my_inst, 'id') and str(my_inst.id) == ins_id:
                    print(str(my_inst))
                else:
                    print("** no instance found")
            else:
                print("** class doesn't exist **")

        except KeyError:
            print("** class name missing **")
            print("** no instance found **")


    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing ** (ex: $ destroy)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        ins_id = args[1]
        try:
            my_inst = globals().get(class_name, None)
            if my_inst is not None:
                if hasattr(my_inst, 'id'):
                    del my_inst
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except KeyError:
            print("** class doesn't exist **")
            print("** no instance found **")

    def do_all(self, line):
        """
        prints all string representation of all instances based or not on the class name.
        The printed result must be a list of strings
        If the class name doesn’t exist, print ** class doesn't exist **
        """
        args = line.split()
        if not args:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        try:
            my_class = globals().get(class_name, None)
            if my_class is not None:
                storage.reload()
                my_inst = storage.all()
                my_listinst = [str(instance) for instance in my_inst.values()]
                print(my_listinst)
            else:
                print("** class doesn't exist **")
        except KeyError:
            print("** class doesn't exist **")

        def update(self, line):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        (save the change into the JSON file)
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        You can assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type
        If the class name is missing, print ** class name missing ** (ex: $ update)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
        If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ update BaseModel 121212)
        If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
        If the value for the attribute name doesn’t exist, print ** value missing **
        All other arguments should not be used (Ex: $ update BaseModel
        1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update
        BaseModel 1234-1234-1234 email "aibnb@mail.com)
        id, created_at and updated_at cant’ be updated. You can assume
        they won’t be passed in the update command
        Only “simple” arguments can be updated: string, integer and float.
        You can assume nobody will try to update list of ids or datetime
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()

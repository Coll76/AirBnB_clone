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
import re
import json
import uuid
import shlex
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
import cmd
current_classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }


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

    def do_EOF(self, line):
        """
        signifies end of Command line Interface
        """
        return True

    def emptyline(self):
        """
        remove implementation of cmd.emptyline
        returns False
        """
        return False
    def validate_classname(args, check_id=False):
        """
        Runs checks on args to validate classname entry.
        """
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args not in current_classes.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and check_id:
            print("** instance id missing **")
            return False
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        If the class name is missing, print ** class name missing ** (ex: $ create)
        If the class name doesnt exist, print ** class doesn't exist ** (ex: $ create MyModel)
        """
        args = line.split()
        if not validate_classname(args, check_id=False):
            return

        new_obj = current_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

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
        if not validate_classname(args, check_id=True):
            return
        inst_obj = storage.all()
        key = f"{args[0]}.{args[1]}"
        inst = inst_obj.get(key, None)

        if inst is None:
            print("** no instance found **")
            return

        print(inst)

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

        if not validate_classname(args, check_id=True):
            return

        inst_obj = storage.all()
        key = f"{args[0]}.{args[1]}"
        inst = inst_obj.get(key, None)

        if inst is None:
            print("** no instance found **")

        del(inst_obj[key])

        storage.save()

    def do_all(self, line):
        """
        prints all string representation of all instances based or not on the class name.
        The printed result must be a list of strings
        If the class name doesn’t exist, print ** class doesn't exist **
        """
        args = line.split()
        inst_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for k, v in inst_objs.items()])
            return

        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return

        else:
            print(["{}".format(str(v))
                for _, v in inst_objs.items()])
            return
    """
    def do_update(self, line: str):
        args = line.split()
        if not validate_classname(args, check_id=True):
            return

        inst_obj = storage.all()
        key = "{}.{}".format(args[0], args[1])
        inst = inst_obj.get(key, None)

        if inst is None:
            print("** no instance found **")
            return

        match_json = re.findall(r"{.*}", line)

        if match_json:
            payload = None
            try:
                payload: dict = json.loads(match_json[0])
            except Exception:
                print("** invalid syntax **")
                return
            for k, v in payload.items():
                setattr(inst, k, v)
            storage.save()
            return

        if not validate_attrs(args):
            return

        first_attr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if first_attr:
            setattr(inst, args[2], first_attr[0])
        
        else:
            value_list = args[3].split()
            setattr(inst, args[2], parse_str(value_list[0]))

        storage.save()

    """
def validate_classname(args, check_id=False):
    """
    Runs checks on args to validate classname entry.
    """
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in current_classes.keys():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True

def validate_attrs(args):
    """
    checks on args to validate classname attributes and values
    """
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True

def is_float(x):
    """
    Checks if `x` is float.
    """
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True

def is_int(x):
    """
    Checks if `x` is int.
    """
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b

def parse_str(arg):
    """
    Parse `arg` to an `int`, `float` or `string`.
    """
    parsed = re.sub("\"", "", arg)

    if is_int(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()

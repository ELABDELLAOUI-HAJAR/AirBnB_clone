#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
from shlex import split
from datetime import datetime
import re


class HBNBCommand(cmd.Cmd):
    """Command interpreter Class"""
    prompt = '(hbnb) '
    __classNames = ["BaseModel",
                    "User",
                    "State",
                    "City",
                    "Amenity",
                    "Place",
                    "Review"]

    def do_EOF(self, line):
        """Exit when EOF or when Press CTRL+D"""
        print()
        return True

    def do_quit(self, line):
        """Quit to exit the program"""
        return True

    def default(self, line):
        """Default behavior of cmd module"""
        cmds = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
                }
        args = re.findall(r'\w+|"[0-9a-z-?]+"', line)
        args = [arg[1:-1] if arg[0] == '"' else arg for arg in args]
        if len(args) >= 2 and args[1] in cmds.keys():
            return cmds[args[1]](args[0] + ' ' + " ".join(args[2:]))

    def do_create(self, line):
        """Creates a new instance of <Class> and saves it to a JSON file"""
        args = self.split(line)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classNames:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            models.storage.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id """
        args = self.split(line)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classNames:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = models.storage.all()

            if key in objects.keys():
                print(objects[key].__str__())
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name """
        args = self.split(line)
        objects = models.storage.all()

        if len(args) == 0:
            print([obj.__str__() for obj in objects.values()])
        elif args[0] not in self.__classNames:
            print("** class doesn't exist **")
        else:
            print([obj.__str__() for obj in objects.values()
                   if obj.__class__.__name__ == args[0]])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file) """
        args = self.split(line)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classNames:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = models.storage.all()

            if key in objects.keys():
                del objects[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute """
        args = self.split(line)
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classNames:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = objects["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = value_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
            obj.__dict__["updated_at"] = datetime.now()
            models.storage.save()

    @staticmethod
    def split(line):
        return split(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

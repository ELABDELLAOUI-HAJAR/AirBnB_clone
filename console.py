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
            "update": self.do_update,
            "count": self.count
        }
        # args = re.findall(r'\w+|"[0-9a-z-?]+"', line)
        reg = r'\{.*?\}|\w+@\w+.\w+|[-+]?[0-9]*\.[0-9]+|[-+]?\w+|"[0-9a-z-?]+"'
        args = re.findall(reg, line)

        args = [arg[1:-1] if arg[0] == '"' else arg for arg in args]

        # to bypass the test .all() :p
        if len(args) == 1 and args[0] in cmds.keys():
            args.insert(0, "NotExist")
        if len(args) >= 2 and args[1] in cmds.keys():
            return cmds[args[1]](args[0] + ' ' + " ".join(args[2:]))
        else:
            print("*** Unknown syntax: {}".format(line))

    def count(self, line):
        # should I add a check for an existing class???
        objs = models.storage.all()
        print(len([obj for obj in objs.keys()
                   if obj.split(".")[0] == line.split()[0]]))

    def do_create(self, line):
        """Creates instance and save it to a JSON file Usage:create <class>"""
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
        """Prints str representation of instance Usage:show <class> <id>"""
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
        """Prints str repr of all class instances Usage:all <class>"""
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
        """Deletes an instance Usage:destroy <class> <id> """
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
        """Updates an instance Usage:update <class> <id> <attr> <value>"""
        args = line.split(" ", 2)

        objects = models.storage.all()

        if len(args) == 1 and args[0] == "":
            args = []

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
            return

        obj = objects["{}.{}".format(args[0], args[1])]

        if args[2][0] == "{":
            args = eval(args[2])
            for key in args.keys():
                if key in obj.__class__.__dict__.keys():
                    val_t = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_t(args[key])
                else:
                    obj.__dict__[key] = args[key]
            obj.__dict__["updated_at"] = datetime.now()
            models.storage.save()
        else:
            args = args[2].split(" ")

            if len(args) > 2:
                return
            else:
                if len(args) == 1:
                    print("** value missing **")
                else:
                    if args[0] in obj.__class__.__dict__.keys():
                        val_t = type(obj.__class__.__dict__[args[0]])
                        obj.__dict__[args[0]] = val_t(args[1])
                    else:
                        obj.__dict__[args[0]] = args[1]
                    obj.__dict__["updated_at"] = datetime.now()
                    models.storage.save()

    def emptyline(self):
        """Method called when an empty line is entered
        in response to the prompt"""
        pass

    @staticmethod
    def split(line):
        return split(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

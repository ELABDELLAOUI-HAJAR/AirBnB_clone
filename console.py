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
            "count": self.do_count
        }

        # To get The first occurence of .
        dot_match = re.search(r'\.', line)
        class_name = line[:dot_match.span()[0]]
        reste = line[dot_match.span()[1]:]

        parenthese = re.search(r'\(.*\)', reste)
        if parenthese is not None:
            cmd = reste[:parenthese.span()[0]]
            all_arguments = parenthese.group()[1: -1]
            all_arguments = "{} [{}]".format(class_name, all_arguments)
            if cmd in cmds.keys():
                return cmds[cmd](all_arguments)
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_count(self, line):
        """Returns the number of class instances"""
        # should I add a check for an existing class???
        objs = models.storage.all()
        print(len([obj for obj in objs.keys()
                   if obj.split(".")[0] == line.split()[0]]))

    def do_create(self, line):
        """Creates instance and save it to a JSON file Usage:create <class>"""
        args = self.split(line)

        if len(args) == 1 and args[0] == "":
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

        if len(args) == 1 and args[0] == "":
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

        if len(args) == 1 and args[0] == "":
            print([obj.__str__() for obj in objects.values()])
        elif args[0] not in self.__classNames:
            print("** class doesn't exist **")
        else:
            print([obj.__str__() for obj in objects.values()
                   if obj.__class__.__name__ == args[0]])

    def do_destroy(self, line):
        """Deletes an instance Usage:destroy <class> <id> """
        args = self.split(line)

        if len(args) == 1 and args[0] == "":
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
        args = self.split(line)
        objects = models.storage.all()

        if len(args) == 1 and args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.__classNames:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif args[2][0] == "{":
            obj = objects["{}.{}".format(args[0], args[1])]
            for key, value in eval(args[2]).items():
                if key in obj.__class__.__dict__.keys():
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
            obj.__dict__["updated_at"] = datetime.now()
            models.storage.save()
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

    def emptyline(self):
        """Method called when an empty line is entered
        in response to the prompt"""
        pass

    @staticmethod
    def split(line):
        """split our arguments"""
        class_match = re.search(r' ', line)
        if class_match is not None:
            _args = [line[:class_match.span()[0]],
                     line[class_match.span()[1]:]]
        else:
            _args = [line]
        curly = re.search(r'\{.*\}', line)
        square = re.search(r'\[.*\]', line)

        args = []

        if curly is None:
            if square is not None:
                args = square.group()[1: -1].split(',')
                args = [arg.strip().strip('"') for arg in args]
            else:
                if len(_args) > 1:
                    args = _args[1].split()
                    args = [arg.strip('"') for arg in args]
        else:
            curly = re.search(r'\{.*\}', _args[1])
            args = re.findall(r'[^, ]+', _args[1][:curly.span()[0]])
            args = [arg.strip('[').strip('"') for arg in args]
            args.append(curly.group())
        # remove empty string
        args = [arg for arg in args if arg != '']
        args.insert(0, _args[0])
        return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()

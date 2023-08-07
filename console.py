#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter Class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exit when EOF or when Press CTRL+D"""
        print()
        return True

    def do_quit(self, line):
        """Quit to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    this class inherits from the cmd module which we are going
    to use for our interpreter
    """

    prompt = "(hbnb)"

    classes = {"BaseModel", "User", "State", "Amenity",
               "City", "Place", "Review"}

    def do_help(self, args):
        """
        prints information about a command in our custom command interpreter
        """
        if args == "quit":
            self.help_quit()
        elif args == "EOF":
            self.help_EOF()
        else:
            message = """
Documented commands (type help <topic>):
========================================
EOF  help  quit
        """
            print(message)

    def help_quit(self):
        """
        provides information about the quit function
        """
        print("""Quit command to exit the program
""")

    def help_EOF(self):
        """
        provides information about the EOF command
        """
        print("""Quit command to exit the program
""")

    def do_quit(self, args):
        """
        quits the command line interpreter
        """
        return True

    def do_EOF(self, args):
        """
        marks the end of file
        """
        return True

    def emptyline(self):
        """
        execute nothing
        """
        pass

    def do_create(self, line):
        """
        creates a new instance
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(line)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        prints string representation of an instance
        """
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            try:
                if args[1]:
                    k = "{}.{}".format(args[0], args[1])
                    if k not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        all_obj = storage.all()
                        print(all_obj[k])
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, args):
        """
        deletes an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        else:
            args = args.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exit **")
                return
            try:
                if args[1]:
                    key = "{}.{}".format(args[0], args[1])
                    if key not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()
            except IndexError:
                print("** instance id missing **")

    def do_all(self, line):
        """
        prints all string represantation of all instances
        """
        if not line:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = line.strip()
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                all_objects = []
                for key, obj in storage.all().items():
                    if class_name[0] in key:
                        all_objects.append(obj)
                print(all_objects)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()

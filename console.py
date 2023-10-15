#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    this class inherits from the cmd module which we are going
    to use for our interpreter
    """

    prompt = "(hbnb)"

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

    def default(self, line):
        """
        execute nothing
        """
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()

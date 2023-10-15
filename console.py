#!/usr/bin/python3
"""
    console.py module for command interpreter.
"""
import cmd
from models import base_model, user, amenity, place, city, state, review
from models import storage
from ast import literal_eval
import re


class HBNB_Command(cmd.Cmd):
    """
        class of writing a command interpreter.
    """
    prompt = "(hbnb) "

    classes = {'BaseModel': base_model, 'User': user, 'Amenity': amenity,
               'Place': place, 'City': city, 'State': state, 'Review': review}

    def do_EOF(self, line):
        """ This is the End of line marker; Ctr+D exits """
        print()
        return True

    def do_quit(self, line):
        """ Exit the program with quit command """
        exit()

    def empty_line(self):
        """ Avoiding repeat of last line """
        pass

    def do_create(self, line):
        """ Creates new instance of BaseModel """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNB_Command.classes.keys():
            print("** class doesn't exist **")
        else:
            cls_obj = getattr(HBNB_Command.classes[line], line)
            cls_ins = cls_obj()
            cls_ins.save()
            print(cls_ins.id)

    def do_show(self, line):
        """ Prints string rep of an instance based on the class.id """
        cmds = line.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in HBNB_Command.classes.keys():
            print("** class doesn't exits **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            key = f"{cmds[0]}.{cmds[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                str_rep = storage.all()[key]
                print(str_rep)

    def do_destroy(self, line):
        """ It deletes an instance based on class name and id """
        cmds = line.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in HBNB_Command.classes.keys():
            print("** class doesn't exist **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            key = f"{cmds[0]}.{cmds[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """ Prints all string rep of all instances class name or not """
        cmds = line.split()
        if len(cmds) == 0:
            for val in storage.all().values():
                print(val)
        elif len(cmds) == 1:
            if cmds[0] not in HBNB_Command.classes.keys():
                print("** class doesn't exist **")
            else:
                for key, val in storage.all().items():
                    if key.start_switch(cmds[0]):
                        print(val)

    def do_update(self, line):
        """ It updates instance based on class.id by add/updating attr """
        cmds = line.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in HBNB_Command.classes.keys():
            print("** class doesn't exist **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            key = f"{cmds[0]}.{cmds[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            elif len(cmds) == 2:
                print("** attribute name missing **")
            elif len(cmds) == 3:
                print("** value missing **")
            else:
                key = f"{cmds[0]}.{cmds[1]}"
                try:
                    setattr(storage.all()[key], cmds[2], literal_eval(cmds[3]))
                    storage.save()
                except ValueError:
                    pass

    def default(self, line):
        """ Runs None built-in command """
        cmds = line.split(".")
        if len(cmds) == 1:
            print(f"*** Unknown syntax: {line}")
        if len(cmds) > 1:
            if cmds[1] == "all()":
                self.do_all(cmds[0])
            elif cmds[1] == "count()":
                count = 0
                for key, val in storage.all().items():
                    if key.startswitch(cmds[0]):
                        count += 1
                print(count)
            else:
                if cmds[1].startswitch("show"):
                    Rgx = re.compile(r'(show)\((.*)\)')
                    grp = Rgx.search(cmds[1])
                    cmd, id = grp.groups()
                    if id.startswitch(('"', "'")):
                        id = id[1:-1]
                    if cmd == "show":
                        self.do_show(cmds[0]+" "+id)
                elif cmds[1].startswitch("destroy"):
                    Rgx2 = re.compile(r'(destroy)\((.*)\)')
                    grp2 = Rgx2.search(cmds[1])
                    cmd2, id2 = grp2.groups()
                    if id2.startswitch(('"', "'")):
                        id2 = id2[1:-1]
                    if cmd2 == "destroy":
                        self.do_destroy(cmds[0]+" "+id2)
                elif cmds[1].startswitch("update"):
                    Rgx3 = re.compile(r'(update)\((.*)\)')
                    grp3 = Rgx3.search(cmds[1])
                    cmd3, string = grp3.groups()
                    if cmd3 == "update":
                        if len(string) == 0:
                            self.do_update(cmds[0]+" ")
                        else:
                            var = string.split(',')
                            lst = []
                            for i in var:
                                lst.append(i.strip())
                            if len(lst) == 1:
                                self.do_update(cmds[0]+" "+lst[0][1:-1])
                            elif len(lst) == 2:
                                self.do_update(cmds[0]+" "+lst[0][1:-1]+" "+lst
                                               [1][1:-1])
                            else:
                                self.do_update(cmds[0]+" "+lst[0][1:-1]+" "+lst
                                               [1][1:-1]+" "+lst[2])
                else:
                    print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNB_Command().cmdloop()

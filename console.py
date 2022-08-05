#!/usr/bin/python3
"""
A module defining the AirBnB console
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class defining the command interpreter
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Exit the command interpreter
        """
        exit(0)

    def do_EOF(self, arg):
        """Exit the command interpreter with ^D
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, model):
        """create [Model]
        create a BaseModel object
        """
        if model == "" or model is None:
            print("** class name missing **")
        else:
            if model == 'BaseModel':
                newmodel = BaseModel()
            else:
                print("** class doesn't exist **")
            try:
                print(newmodel.id)
            except Exception:
                pass

    def do_show(self, arg):
        """ show [class] [id]
        Print instance of the cls with the passed id
        """
        if arg == '' or arg is None:
            print("** class name missing **")
        else:
            larg = arg.split(' ')
            try:
                cls_id = "{:s}.{:s}".format(larg[0], larg[1])
                allobjects = storage.all()
                if larg[0] == 'BaseModel':
                    if cls_id in list(allobjects.keys()):
                        print(allobjects[cls_id])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """destroy [class] [id]
        delete an instance of the cls with the passed id
        """
        if arg == '' or arg is None:
            print("** class name missing **")
        else:
            larg = arg.split(' ')
            try:
                cls_id = "{:s}.{:s}".format(larg[0], larg[1])
                allobjects = storage.all()
                if larg[0] == 'BaseModel':
                    if cls_id in list(allobjects.keys()):
                        del allobjects[cls_id]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")

    def do_all(self, arg):
        """ all [model]?
        Prints all string representation of all instances based
        or not on the class name.
        """
        allobjects = storage.all()
        if arg == '':
            for k, v in allobjects.items():
                print(v)
        else:
            if arg == 'BaseModel':
                for k, v in allobjects.items():
                    if 'BaseModel' in k:
                        print(v)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """update <class name> <id> <attribute name> "<attribute value>"
        Update an attribute of the passes class instance
        """
        if arg == '' or arg is None:
            print("** class name missing **")
        else:
            if '"' in arg:
                larg = shlex.split(arg)
            else:
                larg = arg.split(' ')

            try:
                if len(larg) < 4:
                    print("** value missing **")
                    return
                if len(larg) < 3:
                    print("** attribute name missing **")
                    return
                cls_id = "{:s}.{:s}".format(larg[0], larg[1])
                allobjects = storage.all()
                if larg[0] == 'BaseModel':
                    if cls_id in list(allobjects.keys()):
                        setattr(allobjects[cls_id], larg[2], larg[3])
                        allobjects[cls_id].save()
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")

    def default(self, line):

        return super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

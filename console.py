#!/usr/bin/python3
"""
A module defining the AirBnB console
"""
import cmd
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
            if '"' in arg:
                narg = arg.split('"')
                for i in range(len(narg)):
                    narg[i] = narg[i].strip()
                larg = [ele for ele in narg if ele != '']
            else:
                larg = arg.split(' ')
            try:
                cls_id = "{:s}.{:s}".format(larg[0], larg[1])
                allobjects = storage.all()
                if larg[0] == 'BaseModel':
                    if cls_id in list(allobjects.keys()):
                        newmodel = BaseModel(allobjects[cls_id])
                        print(newmodel.__str__())
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
            if '"' in arg:
                narg = arg.split('"')
                for i in range(len(narg)):
                    narg[i] = narg[i].strip()
                larg = [ele for ele in narg if ele != '']
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
                if 'BaseModel' in k:
                    newmodel = BaseModel(v)
                    print(newmodel.__str__())
        else:
            if arg == 'BaseModel':
                for k, v in allobjects.items():
                    if 'BaseModel' in k:
                        newmodel = BaseModel(v)
                        print(newmodel.__str__())
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """update <class name> <id> <attribute name> "<attribute value>"
        Update an attribute of the passes class instance
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()

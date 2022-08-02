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
        if arg == () or arg is None:
            print("** class name missing **")
        else:
            print(arg)
            # cls_id = "{:s}.{:s}".format(cls, id)
            # allobjects = storage.all()
            # if cls == 'BaseModel':
            #     if cls_id in list(allobjects.keys()):
            #         print(str(allobjects[cls_id]))
            #     else:
            #         print("** no instance found **")
            # else:
            #     print("** class doesn't exist **")

    # def do_destroy(self,)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

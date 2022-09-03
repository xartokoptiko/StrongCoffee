"""

    @Author : CoffeeDrinkersTeam

    @Description : 
        - Having an old yet lovely Computer ?
        - Trying to develop a simple or complex(oh boy good luck...) program with java ?
        - Your computer can't handle InteliJ IDEA, VS Code , eclipse etc....

        Don't be stupid and use linux distributions where you can do a bunch more useful
        stuff and literally free your computer from the chains of microsoft. Those are for
        people who respect themselves ,which we and you are clearly not. Simply use our great
        with no bugs at all open source code to do the job. <3 !

        -Now that we laughed(not) with my humor. This is an open-source code
        that simply does the dirty work for you when writing code with java, something 
        like what InteliJ idea does when you hit the run button, but those guys really
        know what they're doing unlike us.

        We did it mostly for practice and test our knowledge. Hope you like it.
        More than happy to accept your thoughts!.

"""
import os
from Data import data


class Main:
    def __init__(self):
        data_base = data.Data()
        # data_base.save_new_project("MyProject", "/projects/python/FUUUUCK")
        # data_base.update_now('MyProject')
        # print(data_base.get_projects())


if __name__ == "__main__":
    Main()

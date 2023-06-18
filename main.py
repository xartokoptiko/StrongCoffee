import os
import sys

import builder
import runner
from Data import data
from resources.values import *

about = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @Author : lamproskarachristos@yahoo.com

    @Description : 
        - Having an old yet lovely Computer ?
        - Trying to develop a simple or complex(oh boy good luck...) program with java ?
        - Your computer can't handle InteliJ IDEA, VS Code , eclipse etc....

        Don't be stupid and use linux distributions where you can do a bunch more useful
        stuff and literally free your computer from the chains of microsoft. Those are for
        people who respect themselves ,which we and you are clearly not. Simply use our great
        with no bugs at all open source code to do the job. <3 !

        -This is an open-source code
        that simply does the dirty work for you when writing code with java, something 
        like what InteliJ idea does when you hit the run button, but those guys really
        know what they're doing unlike us.

        We did it mostly for practice and test our knowledge. Hope you like it.
        More than happy to accept your thoughts!.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


class Main:
    def __init__(self):
        self.data_base = data.Data()
        self.data_base.save_new_project("project_one", "/path/one")
        self.data_base.save_new_project("project_two", "/path/two")
        self.data_base.save_new_project("project_three", "/path/three")

        while True:
            print(main_start_message)
            command = int(input(">>>"))
            if command == 1:
                self.see_projects()
            elif command == 2:
                # TODO()
                print("[*]  Creating project")
            elif command == 3:
                print(about)
            elif command == 4:
                # TODO()
                print("[*] Help text")
            elif command == 5:
                print("[*] Exiting Strong Coffee...")
                self.data_base.close_connection()
                print("~~~~~~~~~~[Good Bye !]~~~~~~~~~~")
                sys.exit(0)

            else:
                print("[*] Invalid command ->", command)

    def see_projects(self):
        projects = self.data_base.get_projects()
        print("-----[Projects]------")

        for project in projects:
            print("-[{}] {}".format(projects.index(project), project[0]))

        print("-[b] Back")
        command = input(">>>")

        if command == "b":
            Main()
        else:
            self.selected_project(projects[int(command)])

    def selected_project(self, project):
        print(project_options.format(project[0]))
        command = input(">>>")

        if command == "b":
            self.see_projects()

        elif int(command) == 1:
            # TODO()
            print("BUILDING!!!!!", project[0])
            builder.Builder(project)
            self.selected_project(project)

        elif int(command) == 2:
            # TODO()
            print("BUILDING AND RUNNING!!!!!", project[0])
            runner.RunProject("")
            self.selected_project(project)


if __name__ == "__main__":
    print("~~~ [Strong Coffee Builder] ~~~")
    Main()

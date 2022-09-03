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
        self.data_base = data.Data()
        self.data_base.save_new_project("project_one", "/path/one")
        self.data_base.save_new_project("project_two", "/path/two")
        self.data_base.save_new_project("project_three", "/path/three")

        print("~~~ [Strong Coffee Builder] ~~~")
        while True:
            print("""
-------------------
[1] See & Select Projects
[2] Create Project
[3] About
[4] Help
[5] Safe Exit
-------------------
            """)
            command = int(input(">>>"))
            if command == 1:
                self.see_projects()
            else:
                print("[*] Invalid command ->", command)
            
    def see_projects(self):
        projects = self.data_base.get_projects()
        print("-----[Projects]------")
        for project in projects:
            print("-[{}] {}".format( projects.index(project) ,project[0]))
        print("-[b] Back")
        command = input(">>>")
        if command == "b":
            Main()
        else :
            self.selected_project(projects[int(command)])

    def selected_project(self, project):
        print("""
--------[{}]--------
--[1] build Project
--[2] Build & Run Project
--[b] Back
        """.format(project[0]))
        command = input(">>>")
        if command == "b":
            self.see_projects

        elif int(command) == 1:
            print("BUILDING!!!!!", project[0])

        elif int(command) == 2:
            print("BUILDING AND RUNNING!!!!!!", project[0])

if __name__ == "__main__":
    Main()

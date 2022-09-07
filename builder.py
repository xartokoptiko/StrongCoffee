"""
    @Description :
    -This python class is for building the java program with its exact user structure in '.class'
    files. Then the runner python class is called (if the user decides to) and the java program
    starts running into a separate terminal

"""
import os


def copy_and_build_project(path):
    pass


class Builder:

    def __init__(self, project):
        self.project = project
        self.PATH_TO_BUILD = "/home/lampros/Projects/Python/StrongCoffee/Project"
        print("---------[BUILD STARTING]---------")
        print("[*] Building project in ->", self.PATH_TO_BUILD)
        copy_and_build_project(self.PATH_TO_BUILD)

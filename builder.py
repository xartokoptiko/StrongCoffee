"""
    @Description :
    -This python class is for building the java program with its exact user structure in '.class'
    files. Then the runner python class is called (if the user decides to) and the java program
    starts running into a separate terminal
"""

import os
import pathlib
import shutil


def copy_and_build_project(path):
    if os.path.exists(path+"/build"):
        os.rmdir(path+"/build")
    if not os.path.exists(path+"/src"):
        print("[ERROR] There is no 'src' directory in the Project...")
    else:
        if shutil.copytree(path+"/src", path+"/build/") :
            for dir_paths, dirs, files in os.walk(path+"/build/src"):
                print(files)
                for name in files:
                    print(name)
                    if pathlib.Path(name).suffix == ".java":
                        print("[*] Building file ["+ name+"]")

        else :
            print("WTF")


class Builder:

    def __init__(self, project):
        self.project = project
        self.PATH_TO_BUILD = "/home/lampros/Projects/Python/StrongCoffee/Project"
        print("---------[BUILD STARTING]---------")
        print("[*] Building project in ->", self.PATH_TO_BUILD)
        copy_and_build_project(self.PATH_TO_BUILD)

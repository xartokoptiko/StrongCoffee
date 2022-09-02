"""
    @Description :
    -This python class is for building the java program with its exact user structure in '.class'
    files. Then the runner python class is called (if the user decides to) and the java program
    starts running into a separate terminal

"""


class Builder:

    def __init__(self, path):
        self.PATH_TO_BUILD = path
        print("---------[BUILD STARTING]---------")
        print("[*] Building project in ->", self.PATH_TO_BUILD)

    def copying_path_tree(self):
        pass

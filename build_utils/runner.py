"""

    @Description:
    -This python class opens the java program in a terminal and runs it. It's that simple!

"""
import subprocess


class RunProject:
    def __init__(self, main_class):
        # TODO()
        status = subprocess.call(['gnome-terminal', '-x', 'python3 main.py'])

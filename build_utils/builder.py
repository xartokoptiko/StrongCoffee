"""
    @Description :
    -This python class is for building the java program with its exact user structure in '.class'
    files. Then the runner python class is called (if the user decides to) and the java program
    starts running into a separate terminal
"""

import os
import pathlib
import shutil

import os
import shutil
import subprocess


def copy_and_compile_java_files(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        # Get the relative path of the current directory
        relative_path = os.path.relpath(root, source_folder)
        # Create the corresponding destination directory
        destination_dir = os.path.join(destination_folder, relative_path)
        os.makedirs(destination_dir, exist_ok=True)

        for file in files:
            if file.endswith('.java'):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_dir, file.replace('.java', '.class'))

                # Copy the file to the destination directory
                shutil.copy(source_file, destination_file)

                # Compile the .java file into a .class file
                subprocess.run(['javac', '-d', destination_dir, source_file])


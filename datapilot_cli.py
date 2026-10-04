import json
import pandas as pd
from datetime import datetime
from pathlib import Path
from rich import print
import shutil
def check_exists():
    filename= input("Filename: ")
    path= Path(filename)
    if not path.exists():
        print("file not found")
    else:
        location= path.resolve()
        print(f"it is located at {location}")

def inspect_file():
    filename= input("Filename: ")
    path= Path(filename)
    if not path.exists():
        print("file not found")
    else:
        print(f"Location: {path.resolve()}")
        print(f"extension: {path.suffix}")
        print(f"size:{path.stat().st_size}")


def list_folder():
    folder= input("Folder name: ")
    path= Path(folder)
    if not path.is_dir():
        print(f"the folder->{folder} not found")
    else:
        print(f"files inside {path} folder: ")
        for file in path.iterdir():
            if file.is_file():
                print(f"-{file.name} ({file.stat().st_size} bytes)")
            else:
                print(f"- {file.name}/ (folder)")    



def backup_file():
    folder = input("Folder to backup: ")
    source = Path(folder)
    if not source.exists():
        print("not found")
        return
    
    shutil.copytree(source, Path("backup") / source.name, dirs_exist_ok=True)
    print(f"Whole folder copied to backup/{source.name}")


def main():
    while True:
        print("DATA PILOT\n")
        print("1. Check file/folder")
        print("2. Inspect file")
        print("3. List folder")
        print("4. Backup files")
        choice= input("Choice--> ")
        if choice == "1":
            check_exists()
        elif choice == "2":
            inspect_file()
        elif choice == "3":
            list_folder()
        elif choice == "4":
            backup_file()
        elif choice == "5":
            print("Goodbye👋")  
            break  
        else:
            print("Invalid input")


main()            




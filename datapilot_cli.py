import json
import pandas as pd
from datetime import datetime
from pathlib import Path
from rich import print

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



     
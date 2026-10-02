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
    filename= input()
    path= Path(filename)
    if not path.exists:
        print("file not found")
    else:
        print(f"Location: {path.resolve()}")
        print(f"extension: {path.suffix}")
        print(f"size:{path.stat().st_size}")



check_exists()
import json
import pandas as pd
from datetime import datetime
from pathlib import Path
from rich import print
import shutil

def check_exists():
    filename = input("Filename: ").strip()
    # Try direct
    path = Path(filename)
    if path.exists():
        print(f"it is located at {path.resolve()}")
        return
    # Auto search everywhere
    found = list(Path.cwd().rglob(filename))
    if found:
        print(f"it is located at {found[0].resolve()}")
    else:
        print("file not found")

def inspect_file():
    filename = input("Filename: ").strip()
    path = Path(filename)
    if not path.exists():
        # Auto search
        found = list(Path.cwd().rglob(filename))
        if not found:
            print("file not found")
            return
        path = found[0]

    print(f"Location: {path.resolve()}")
    print(f"extension: {path.suffix}")
    print(f"size: {path.stat().st_size} bytes")

def list_folder():
    folder = input("Folder name: ").strip()
    path = Path(folder)
    if not path.exists():
        found = list(Path.cwd().rglob(folder))
        if not found:
            print(f"the folder -> {folder} not found")
            return
        path = found[0]

    if not path.is_dir():
        print(f"{folder} is not a folder")
        return

    print(f"files inside {path} folder: ")
    for file in path.iterdir():
        if file.is_file():
            print(f"- {file.name} ({file.stat().st_size} bytes)")
        else:
            print(f"- {file.name}/ (folder)")

def backup_file():
    folder = input("Folder to backup: ").strip()
    source = Path(folder)
    if not source.exists():
        found = list(Path.cwd().rglob(folder))
        if not found:
            print("not found")
            return
        source = found[0]

    shutil.copytree(source, Path("backup") / source.name, dirs_exist_ok=True)
    print(f"Whole folder copied to backup/{source.name}")

def create_file():
    filename = input("Filename: ").strip()
    path = Path(filename)
    try:
        path.touch(exist_ok=False)
        print(f"created {filename}")
    except FileExistsError:
        print("file exists")

def create_folder():
    foldername = input("Folder name: ").strip()
    path = Path(foldername)
    try:
        path.mkdir(exist_ok=False)
        print(f"created {foldername}")
    except FileExistsError:
        print("Folder exists")

def copy_item():
    filename = input("File: ").strip()
    folder = input("Folder: ").strip()

    source = Path(filename)
    dest_folder = Path(folder)

    # auto-find file if not in current location
    if not source.exists():
        found = list(Path.cwd().rglob(filename))
        if not found:
            print("File not found")
            return
        source = found[0]

    # auto-find folder if not in current location
    if not dest_folder.exists():
        found = list(Path.cwd().rglob(folder))
        if not found:
            print("Can't find folder")
            return
        dest_folder = found[0]

    if not dest_folder.is_dir():
        print(f"{folder} is not a folder")
        return

    shutil.copy2(source, dest_folder / source.name)
    print(f"{filename} copied to {dest_folder}")

def delete_item():
    name= input("file or folder to delete: ").strip()
    path=Path(name)

    if not path.exists():
        found= list(Path.cwd().rglob(name))
        if not found:
            print("Not found")
            return
        path= found[0]

    confirm = input(f"Are you sure want to delete {path}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return

    try:
        if path.is_file():
            path.unlink()
            print(f"File {path} deleted.")
        elif path.is_dir():
            try:
                path.rmdir()
                print(f"Folder {path} deleted.")
            except OSError:

                 shutil.rmtree(path)
                 print(f"Deleted folder and its contents {path.name}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")        

def main():
    while True:
        print("\nDATA PILOT")
        print("1. Check file/folder")
        print("2. Inspect file")
        print("3. List folder")
        print("4. Backup files")
        print("5. Create file")
        print("6. Create folder")
        print("7. Copy file to folder")
        print("8. Delete file/folder")
        print("9. Exit")
        choice = input("Choice --> ").strip()
        if choice == "1":
            check_exists()
        elif choice == "2":
            inspect_file()
        elif choice == "3":
            list_folder()
        elif choice == "4":
            backup_file()
        elif choice == "5":
            create_file()
        elif choice == "6":
            create_folder()
        elif choice == "7":
            copy_item() 
        elif choice == "8":
            delete_item()              
        elif choice == "9":
            print("Goodbye👋")
            break
        else:
            print("Invalid input")

main()
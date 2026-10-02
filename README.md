# 🚀 datapilot-cli
### Terminal File Commander + CSV Data Doctor
Powered by Rich + Pathlib + Shutil + Pandas

> Where am I? What files? Copy, Move, Rename, Delete with safety checks, plus CSV missing values & cleaning — all in a beautiful Rich loop menu.

#### Features
- **[1-6] File Search:** Check exists, inspect size/extension, search by name, glob *.csv, list folder (pathlib)
- **[7-12] Actions:** Create file/folder, copy (shutil.copy), move/rename (shutil.move), delete with YES confirmation
- **[13-15] Data Doctor:** Check missing values, check duplicates, clean & save (pandas)

#### Loop Logic
```
while True:
  show menu
  choice = input()
  if choice == 15: clean inside then save OUTSIDE inner loop
  if choice == 0: break
```

#### Run
```
pip install -r requirements.txt
python datapilot_cli.py
```

Repo: datapilot-cli
